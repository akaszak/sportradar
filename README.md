# Football World Cup Score Board

A simple library to manage and display football match scores for the World Cup.

## Features

- Start a new match
- Update match scores
- Finish a match
- Get a summary of matches in progress, sorted by total score and most recently started

## Assumptions
*Keep it simple. Stick to the requirements and try to implement the simplest solution
you can possibly think of that works and don't forget about edge cases.
Use an in-memory store solution (for example just use collections to store the
information you might require).
*We are NOT looking for a REST API, a Web Service or Microservice. Just a simple
implementation.
*Focus on Quality. Get a quick feedback loop by writing comprehensive tests, pay
attention to OO design, Clean Code and adherence to SOLID principles.
*Approach. Code the solution according to your standards. Please share your
solution with a link to a source control repository (e.g. GitHub, GitLab,
BitBucket) as we would like you to see your progress (your commit history is
important)
*Add a README.md file where you can make notes of any assumption or things you
would like to mention to us about your solution.
*If the implementation is in a frontend language, then it must follow all of the above
guidelines and additionally you should apply the suggestions below:
*If it is written it in a specific UI framework or library then we would
suggest writing the simplest component/s to serve the described
functionality. Please don’t spend time making it look good.
*If it is written in plain JavaScript then we would suggest implementing the
solution as a simple service or module.

## Implementation highlights
As it is very simple and well within what AI-enhanced tools can do, most of the code has been automatically generated. It was then fine-tuned, tested and bugfixed to ensure alignment with task requirements.

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