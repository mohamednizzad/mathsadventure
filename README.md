# Math Adventure - Educational Game

A fun and educational math game designed for students in grades 1-5, built with Pygame.

## Features

- Progressive difficulty levels matching grades 1-5
- Interactive and engaging gameplay
- Various math operations (addition, subtraction, multiplication, division)
- Colorful graphics and sound effects
- Score tracking and achievements

## Requirements

- Python 3.7+
- Pygame

## Installation

1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python src/main.py
```

## Testing

```bash
python -m pytest tests/
```

## Project Structure

```
.
├── src/
│   ├── main.py
│   ├── game.py
│   ├── levels.py
│   └── utils.py
├── tests/
│   ├── test_game.py
│   └── test_levels.py
├── assets/
│   ├── fonts/
│   ├── images/
│   └── sounds/
├── requirements.txt
└── README.md
```