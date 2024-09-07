import unittest
import torch
from recommender.recommender import encode_book, encode_preference, BookRecommendationModel
from recommender.database_model import Book, Preference

class TestBookRecommender(unittest.TestCase):

    def setUp(self):
        # Setup theme, period, and style maps for testing
        self.theme_map = {'fiction': 0, 'non-fiction': 1}
        self.period_map = {'modern': 0, 'classic': 1}
        self.style_map = {'prose': 0, 'poetry': 1}

        # Setup sample books and preferences for testing
        self.book = Book(id=1, title='Test Book', author='Author A', theme='fiction', period='modern', style='prose')
        self.preference = Preference(id=1, theme='fiction', period='modern', style='prose')

        # Create a recommendation model instance
        self.model = BookRecommendationModel(input_size=136)  # Assuming input vector size is 136 (68 for user + 68 for book)

    def test_encode_book_return_when_size_less_than_68(self):
        # Test encoding a book
        encoded_book = encode_book(self.book, self.theme_map, self.period_map, self.style_map)
        self.assertEqual(encoded_book, None)

    def test_encode_book_return_when_size_less_than_68(self):
        # Test encoding a book
        encoded_book = encode_book(self.book, self.theme_map, self.period_map, self.style_map)
        expected_encoding = [1, 0, 1, 0, 1, 0 ]  # one-hot encoded vector for theme, period, and style
        self.assertEqual(encoded_book, expected_encoding)

    def test_encode_preference(self):
        # Test encoding a user preference
        encoded_preference = encode_preference(self.preference, self.theme_map, self.period_map, self.style_map)
        expected_encoding = [1, 0, 1, 0, 1, 0]  # one-hot encoded vector for theme, period, and style
        self.assertEqual(encoded_preference, expected_encoding)

    def test_model_output_size(self):
        # Test that the model output is a scalar (single value prediction)
        user_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample user vector (68 elements)
        book_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample book vector (68 elements)
        input_vector = torch.cat([user_vector, book_vector], dim=0)  # Concatenated input

        # Make a prediction
        prediction = self.model(input_vector)
        self.assertEqual(prediction.shape, torch.Size([1]))  # Output should be a scalar value

    def test_model_prediction_range(self):
        # Test that the model's predictions are in the range [0, 1] after applying sigmoid
        user_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample user vector (68 elements)
        book_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample book vector (68 elements)
        input_vector = torch.cat([user_vector, book_vector], dim=0)  # Concatenated input

        # Make a prediction
        prediction = self.model(input_vector)
        self.assertTrue(0 <= prediction.item() <= 1)  # Ensure prediction is within [0, 1]

    def test_model_training_step(self):
        # Test a single training step
        user_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample user vector
        book_vector = torch.FloatTensor([1, 0, 1, 0, 1, 0] * 11 + [0] * 2)  # Sample book vector
        input_vector = torch.cat([user_vector, book_vector], dim=0)

        # Target = 1 (since we assume the user prefers this book)
        target = torch.FloatTensor([1])

        # Optimizer and loss function
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
        loss_fn = torch.nn.BCELoss()

        # Forward pass
        optimizer.zero_grad()
        prediction = self.model(input_vector)
        loss = loss_fn(prediction, target)

        # Backward pass
        loss.backward()
        optimizer.step()

        # Check that the loss is a valid scalar
        self.assertIsInstance(loss.item(), float)

if __name__ == "__main__":
    unittest.main()
