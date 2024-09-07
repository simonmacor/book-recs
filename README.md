[![CI](https://github.com/simonmacor/book-recs/actions/workflows/ci.yml/badge.svg)](https://github.com/simonmacor/book-recs/actions/workflows/ci.yml)
# Book Recommender System

This project implements a book recommendation system based on user preferences, such as theme, period of the author, and literary style. It is built using **SQLAlchemy** for database management and **PyTorch** for training the neural network model that recommends books to users. **Alembic** is used for database migrations.

## Prerequisites

To run this project, you need the following installed on your machine:

- **Python 3.8+**
- **pip** (to install Python dependencies)
- **Docker** and **Docker Compose** (to run the application in a containerized environment)
- **virtualenv** (optional but recommended)

## Project Setup

### Step 1: Clone the Project

```bash
git clone https://github.com/your-username/book-recommender.git
cd book-recommender
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It is recommended to use a virtual environment to isolate the project dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate  # For Linux/Mac
# Or for Windows
# .venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the dependencies listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

The project uses **PostgreSQL** as its database, managed via Docker. See the **`docker-compose.yml`** and modify it according to your needs.

### Step 5: Start containers

To start PostgreSQL and the Python app, use Docker Compose:

```bash
docker-compose up --build
```

This will start both PostgreSQL and the Python application in separate containers.

### Step 6: Apply Migrations

Alembic is used for managing database schema changes. To set up Alembic:

```bash
   docker-compose exec app alembic upgrade head
   ```


## Using the Recommendation Script

The **`recommender/recommender.py`** file is the main script for the recommendation system. Here's how to run it inside the Docker container:

```bash
docker-compose exec app python -m recommender.recommender
```

This will train the model using user preferences and provide book recommendations.

### Explanation of the Recommendation Model

The model uses a neural network to match books with user preferences. It encodes each book and user preference into a vector, then concatenates these vectors to predict whether a user will like a given book.

The model uses PyTorch and has three main layers:
- **Layer 1**: A linear layer to reduce the input dimension.
- **Layer 2**: A second linear layer to learn more compact representations.
- **Output Layer**: A final layer with a sigmoid activation function to predict the likelihood of a match between the user and the book.

## Unit Tests

Unit tests are defined in the **`tests/test_recommender.py`** file and verify the correct functioning of the models and the recommendation system.

### Running Unit Tests with `unittest`

You can run the unit tests inside the Docker container using `unittest` as follows:

```bash
docker-compose exec app python -m unittest discover -s tests
```
