import os
import torch
import torch.nn as nn
import torch.optim as optim
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, distinct
from sqlalchemy.orm import sessionmaker
from typing import Dict, List, Type
from .database_model import Book, User, Preference


def encode_book(book: Type[Book], theme_map: Dict[str, int], period_map: Dict[str, int], style_map: Dict[str, int]) -> None|List[int]:
    theme_vector = [1 if theme_map.get(book.theme, -1) == i else 0 for i in range(len(theme_map))]
    period_vector = [1 if period_map.get(book.period, -1) == i else 0 for i in range(len(period_map))]
    style_vector = [1 if style_map.get(book.style, -1) == i else 0 for i in range(len(style_map))]
    encoded_vector = theme_vector + period_vector + style_vector
    return encoded_vector


def encode_preference(preference: Preference, theme_map: Dict[str, int], period_map: Dict[str, int], style_map: Dict[str, int]) -> List[int]:
    theme_vector = [1 if theme_map.get(preference.theme, -1) == i else 0 for i in range(len(theme_map))]
    period_vector = [1 if period_map.get(preference.period, -1) == i else 0 for i in range(len(period_map))]
    style_vector = [1 if style_map.get(preference.style, -1) == i else 0 for i in range(len(style_map))]
    return theme_vector + period_vector + style_vector


class BookRecommendationModel(nn.Module):
    def __init__(self, input_size: int):
        super(BookRecommendationModel, self).__init__()
        self.layer1 = nn.Linear(input_size, 8)  # Ajuster pour la taille concaténée
        self.layer2 = nn.Linear(8, 4)
        self.output_layer = nn.Linear(4, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.sigmoid(self.output_layer(x))
        return x


if __name__ == "__main__":
    load_dotenv()
    engine = create_engine(os.getenv('DSN'))
    Session = sessionmaker(bind=engine)
    session = Session()

    themes = session.execute(select(distinct(Book.theme))).scalars().all()
    periods = session.execute(select(distinct(Book.period))).scalars().all()
    styles = session.execute(select(distinct(Book.style))).scalars().all()

    theme_map = {theme: i for i, theme in enumerate(themes)}
    period_map = {period: i for i, period in enumerate(periods)}
    style_map = {style: i for i, style in enumerate(styles)}

    books = session.query(Book).all()
    users = session.query(User).all()

    book_vectors = {book.id: encode_book(book, theme_map, period_map, style_map) for book in books}
    user_vectors = {user.id: encode_preference(user.preferences, theme_map, period_map, style_map) for user in users}

    input_size = len(next(iter(user_vectors.values()))) + len(next(iter(book_vectors.values())))
    model = BookRecommendationModel(input_size=input_size)

    # Optimiseur et fonction de perte
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.BCELoss()

    # Entraînement
    num_epochs = 10
    for epoch in range(num_epochs):
        model.train()
        optimizer.zero_grad()

        for user in users:
            user_vector = torch.FloatTensor(user_vectors[user.id])

            for book in books:
                book_vector = torch.FloatTensor(book_vectors[book.id])

                input_vector = torch.cat([user_vector, book_vector], dim=0)

                # Target = 1 if book match user preferences
                target = 1 if (user.preferences.theme == book.theme or
                               user.preferences.period == book.period or
                               user.preferences.style == book.style) else 0

                target = torch.FloatTensor([target])

                # Prédiction
                prediction = model(input_vector)

                # Loss computing
                loss = loss_fn(prediction, target)

                # Backpropagation weight update
                loss.backward()
                optimizer.step()

        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

    session.close()
