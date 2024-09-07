"""insert data

Revision ID: c7e8775fcc4b
Revises: c3393229da11
Create Date: 2024-09-04 22:20:45.754520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7e8775fcc4b'
down_revision: Union[str, None] = 'c3393229da11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
               INSERT INTO books (title, author, theme, period, style) VALUES
('The Iliad', 'Homer', 'Epic Poetry', '8th Century BC', 'Ancient Greek'),
('Divine Comedy', 'Dante Alighieri', 'Classic', '14th Century', 'Italian Renaissance'),
('Hamlet', 'William Shakespeare', 'Theatre', '16th Century', 'Elizabethan'),
('The Prince', 'Niccolò Machiavelli', 'Philosophy', '16th Century', 'Renaissance'),
('Don Quixote', 'Miguel de Cervantes', 'Classic', '17th Century', 'Spanish Golden Age'),
('Paradise Lost', 'John Milton', 'Epic Poetry', '17th Century', 'English Renaissance'),
('Candide', 'Voltaire', 'Philosophy', '18th Century', 'Enlightenment'),
('Les Misérables', 'Victor Hugo', 'Classic', '19th Century', 'Romanticism'),
('Moby-Dick', 'Herman Melville', 'Classic', '19th Century', 'American Renaissance'),
('War and Peace', 'Leo Tolstoy', 'Historical', '19th Century', 'Russian Realism'),
('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophy', '19th Century', 'Russian Realism'),
('The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 'Classic', '19th Century', 'Detective Fiction'),
('Dracula', 'Bram Stoker', 'Classic', '19th Century', 'Gothic Fiction'),
('Pride and Prejudice', 'Jane Austen', 'Classic', '19th Century', 'Regency'),
('Faust', 'Johann Wolfgang von Goethe', 'Theatre', '19th Century', 'German Romanticism'),
('Madame Bovary', 'Gustave Flaubert', 'Classic', '19th Century', 'Realism'),
('Great Expectations', 'Charles Dickens', 'Classic', '19th Century', 'Victorian'),
('The Odyssey', 'Homer', 'Epic Poetry', '8th Century BC', 'Ancient Greek'),
('Beowulf', 'Unknown', 'Epic Poetry', '10th Century', 'Old English'),
('The Canterbury Tales', 'Geoffrey Chaucer', 'Classic', '14th Century', 'Middle English'),
('The Divine Comedy', 'Dante Alighieri', 'Classic', '14th Century', 'Italian Renaissance'),
('The Tale of Genji', 'Murasaki Shikibu', 'Classic', '11th Century', 'Heian Period'),
('Gulliver’s Travels', 'Jonathan Swift', 'Classic', '18th Century', 'Satire'),
('Frankenstein', 'Mary Shelley', 'Science Fiction', '19th Century', 'Gothic Fiction'),
('Wuthering Heights', 'Emily Brontë', 'Classic', '19th Century', 'Gothic Fiction'),
('Jane Eyre', 'Charlotte Brontë', 'Classic', '19th Century', 'Gothic Fiction'),
('The Hunchback of Notre-Dame', 'Victor Hugo', 'Classic', '19th Century', 'Romanticism'),
('Crime and Punishment', 'Fyodor Dostoevsky', 'Philosophy', '19th Century', 'Russian Realism'),
('The Count of Monte Cristo', 'Alexandre Dumas', 'Classic', '19th Century', 'Historical Fiction'),
('The Scarlet Letter', 'Nathaniel Hawthorne', 'Classic', '19th Century', 'American Renaissance'),
('Treasure Island', 'Robert Louis Stevenson', 'Classic', '19th Century', 'Adventure'),
('Anna Karenina', 'Leo Tolstoy', 'Classic', '19th Century', 'Russian Realism'),
('The Three Musketeers', 'Alexandre Dumas', 'Classic', '19th Century', 'Historical Fiction'),
('The Picture of Dorian Gray', 'Oscar Wilde', 'Classic', '19th Century', 'Gothic Fiction'),
('Heart of Darkness', 'Joseph Conrad', 'Classic', '20th Century', 'Modernism'),
('Ulysses', 'James Joyce', 'Classic', '20th Century', 'Modernism'),
('To the Lighthouse', 'Virginia Woolf', 'Classic', '20th Century', 'Modernism'),
('1984', 'George Orwell', 'Science Fiction', '20th Century', 'Dystopian'),
('Brave New World', 'Aldous Huxley', 'Science Fiction', '20th Century', 'Dystopian'),
('The Lord of the Rings', 'J.R.R. Tolkien', 'Heroic Fantasy', '20th Century', 'Fantasy'),
('The Hobbit', 'J.R.R. Tolkien', 'Heroic Fantasy', '20th Century', 'Fantasy'),
('The Catcher in the Rye', 'J.D. Salinger', 'Classic', '20th Century', 'Realism'),
('One Hundred Years of Solitude', 'Gabriel García Márquez', 'Classic', '20th Century', 'Magic Realism'),
('Lolita', 'Vladimir Nabokov', 'Classic', '20th Century', 'Modernism'),
('Catch-22', 'Joseph Heller', 'Classic', '20th Century', 'Satire'),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', '20th Century', 'Jazz Age'),
('The Sound and the Fury', 'William Faulkner', 'Classic', '20th Century', 'Modernism'),
('Slaughterhouse-Five', 'Kurt Vonnegut', 'Science Fiction', '20th Century', 'Anti-war'),
('Brave New World', 'Aldous Huxley', 'Science Fiction', '20th Century', 'Dystopian'),
('The War of the Worlds', 'H.G. Wells', 'Science Fiction', '19th Century', 'Science Fiction'),
('The Time Machine', 'H.G. Wells', 'Science Fiction', '19th Century', 'Science Fiction'),
('Fahrenheit 451', 'Ray Bradbury', 'Science Fiction', '20th Century', 'Dystopian'),
('The Old Man and the Sea', 'Ernest Hemingway', 'Classic', '20th Century', 'Realism'),
('For Whom the Bell Tolls', 'Ernest Hemingway', 'Classic', '20th Century', 'War Novel'),
('Dune', 'Frank Herbert', 'Science Fiction', '20th Century', 'Space Opera'),
('The Stranger', 'Albert Camus', 'Philosophy', '20th Century', 'Existentialism'),
('Animal Farm', 'George Orwell', 'Classic', '20th Century', 'Political Satire'),
('On the Road', 'Jack Kerouac', 'Classic', '20th Century', 'Beat Generation'),
('The Grapes of Wrath', 'John Steinbeck', 'Classic', '20th Century', 'Social Realism'),
('Beloved', 'Toni Morrison', 'Classic', '20th Century', 'Historical Fiction'),
('Midnight’s Children', 'Salman Rushdie', 'Classic', '20th Century', 'Magic Realism'),
('The Name of the Rose', 'Umberto Eco', 'Historical', '20th Century', 'Historical Fiction'),
('The Handmaid’s Tale', 'Margaret Atwood', 'Science Fiction', '20th Century', 'Dystopian'),
('The Road', 'Cormac McCarthy', 'Science Fiction', '21st Century', 'Post-apocalyptic'),
('Harry Potter and the Philosopher’s Stone', 'J.K. Rowling', 'Heroic Fantasy', '20th Century', 'Fantasy'),
('The Hunger Games', 'Suzanne Collins', 'Science Fiction', '21st Century', 'Dystopian'),
('Twilight', 'Stephenie Meyer', 'Heroic Fantasy', '21st Century', 'Fantasy Romance'),
('The Book Thief', 'Markus Zusak', 'Historical', '21st Century', 'Historical Fiction'),
('Life of Pi', 'Yann Martel', 'Philosophy', '21st Century', 'Adventure Fiction'),
('The Da Vinci Code', 'Dan Brown', 'Historical', '21st Century', 'Mystery Thriller'),
('The Kite Runner', 'Khaled Hosseini', 'Classic', '21st Century', 'Historical Fiction'),
('Shantaram', 'Gregory David Roberts', 'Biographical', '21st Century', 'Autobiographical Fiction'),
('The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Classic', '21st Century', 'Crime Fiction'),
('The Road', 'Cormac McCarthy', 'Science Fiction', '21st Century', 'Post-apocalyptic'),
('The Night Circus', 'Erin Morgenstern', 'Heroic Fantasy', '21st Century', 'Fantasy'),
('A Game of Thrones', 'George R.R. Martin', 'Heroic Fantasy', '20th Century', 'Epic Fantasy'),
('The Alchemist', 'Paulo Coelho', 'Philosophy', '20th Century', 'Adventure Fiction'),
('The Girl on the Train', 'Paula Hawkins', 'Classic', '21st Century', 'Psychological Thriller'),
('Gone Girl', 'Gillian Flynn', 'Classic', '21st Century', 'Psychological Thriller'),
('The Fault in Our Stars', 'John Green', 'Classic', '21st Century', 'Young Adult Fiction'),
('The Shining', 'Stephen King', 'Horror', '20th Century', 'Gothic Fiction'),
('Carrie', 'Stephen King', 'Horror', '20th Century', 'Gothic Fiction'),
('The Stand', 'Stephen King', 'Science Fiction', '20th Century', 'Post-apocalyptic'),
('The Wind-Up Bird Chronicle', 'Haruki Murakami', 'Classic', '20th Century', 'Magic Realism'),
('Kafka on the Shore', 'Haruki Murakami', 'Philosophy', '21st Century', 'Magic Realism'),
('Norwegian Wood', 'Haruki Murakami', 'Classic', '20th Century', 'Romance'),
('The Shadow of the Wind', 'Carlos Ruiz Zafón', 'Classic', '21st Century', 'Historical Fiction'),
('The Pillars of the Earth', 'Ken Follett', 'Historical', '2 user0th Century', 'Historical Fiction'),
('The Power of Now', 'Eckhart Tolle', 'Philosophy', '21st Century', 'Spirituality'),
('The Road Less Traveled', 'M. Scott Peck', 'Philosophy', '20th Century', 'Psychology'),
('The Secret', 'Rhonda Byrne', 'Philosophy', '21st Century', 'Self-help'),
('The Name of the Wind', 'Patrick Rothfuss', 'Heroic Fantasy', '21st Century', 'Epic Fantasy'),
('The Wise Man’s Fear', 'Patrick Rothfuss', 'Heroic Fantasy', '21st Century', 'Epic Fantasy');
               ''')
    op.execute('''
                INSERT INTO users (username, email) VALUES 
                ('Bruce Wayne', 'bruce.wayne@gotham.city'),
                ('Peter Parker', 'peter.parker@marvel');
    ''')

    op.execute('''
                INSERT INTO preferences (user_id, theme, period, style) VALUES 
                ((SELECT id FROM users WHERE email = 'bruce.wayne@gotham.city'), 'Heroic Fantasy', '19th Century', 'Epic Fantasy'),
                ((SELECT id FROM users WHERE email = 'peter.parker@marvel'), 'Classic', '19th Century', 'Russian Realism');
        ''')

def downgrade() -> None:
    pass
