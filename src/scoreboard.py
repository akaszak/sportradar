import uuid
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Match:
    home_team: str
    away_team: str
    home_score: int = 0
    away_score: int = 0
    creation_order: int = 0  # Track when the match was added

    def __str__(self) -> str:
        return f"{self.home_team} {self.home_score} - {self.away_team} {self.away_score}"

    @property
    def total_score(self) -> int:
        return self.home_score + self.away_score

class ScoreBoard:
    def __init__(self):
        self.matches: Dict[str, Match] = {}
        self._next_order = 0  # Counter for creation order
    
    def _has_active_match(self, team1: str, team2: str) -> bool:
        """Check if there's an active match between the given teams."""
        for match in self.matches.values():
            if (match.home_team == team1 and match.away_team == team2) or \
               (match.home_team == team2 and match.away_team == team1):
                return True
        return False
    
    def start_match(self, home_team: str, away_team: str) -> str:
        if not home_team or not away_team:
            raise ValueError("Team names cannot be empty")
        
        if home_team == away_team:
            raise ValueError("Home and away teams cannot be the same")
        
        if self._has_active_match(home_team, away_team):
            raise ValueError(f"Match between {home_team} and {away_team} already exists")
        
        match_id = str(uuid.uuid4())
        self.matches[match_id] = Match(
            home_team=home_team,
            away_team=away_team,
            creation_order=self._next_order
        )
        self._next_order += 1
        
        return match_id
    
    def finish_match(self, match_id: str) -> None:
        if match_id not in self.matches:
            raise KeyError(f"Match with ID {match_id} not found")
        del self.matches[match_id]
    
    def update_score(self, match_id: str, home_score: int, away_score: int) -> None:
        if match_id not in self.matches:
            raise KeyError(f"Match with ID {match_id} not found")
        
        # Validate that scores are integers
        if not isinstance(home_score, int) or not isinstance(away_score, int):
            raise TypeError("Scores must be integers")
        
        if home_score < 0 or away_score < 0:
            raise ValueError("Scores cannot be negative")
        
        match = self.matches[match_id]
        
        # Check if either score is being decreased
        if home_score < match.home_score or away_score < match.away_score:
            raise ValueError("Scores cannot be decreased")
        
        match.home_score = home_score
        match.away_score = away_score
    
    def get_summary(self) -> List[Match]:
        # Get all active matches
        active_matches = [match for match in self.matches.values()]
        
        # Sort by total score (descending) and then by creation order (most recent first)
        return sorted(
            active_matches,
            key=lambda x: (x.total_score, x.creation_order),
            reverse=True
        ) 