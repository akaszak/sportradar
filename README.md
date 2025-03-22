# Football World Cup Score Board

A simple library to manage and display football match scores for the World Cup.

## Features

- Start a new match
- Update match scores
- Finish a match
- Get a summary of matches in progress, sorted by total score and most recently started

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.scoreboard import ScoreBoard

# Create a new scoreboard
scoreboard = ScoreBoard()

# Start a new match
match_id = scoreboard.start_match("Mexico", "Canada")

# Update score
scoreboard.update_score(match_id, 0, 5)

# Get summary of matches in progress
summary = scoreboard.get_summary()
```

## Development

To run tests:
```bash
pytest
``` 