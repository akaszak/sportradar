import uuid
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Match:
    home_team: str
    away_team: str
    home_score: int = 0
    away_score: int = 0

class ScoreBoard:
    def __init__(self):
        self.matches: Dict[str, Match] = {}
    
    def start_match(self, home_team: str, away_team: str) -> str:
        if not home_team or not away_team:
            raise ValueError("Team names cannot be empty")
        
        if home_team == away_team:
            raise ValueError("Home and away teams cannot be the same")
        
        match_id = str(uuid.uuid4())
        self.matches[match_id] = Match(
            home_team=home_team,
            away_team=away_team
        )
        
        return match_id
    
    def finish_match(self, match_id: str) -> None:
        if match_id not in self.matches:
            raise KeyError(f"Match with ID {match_id} not found")
        del self.matches[match_id]
    
    def update_score(self, match_id: str, home_score: int, away_score: int) -> None:
        if match_id not in self.matches:
            raise KeyError(f"Match with ID {match_id} not found")
        
        if home_score < 0 or away_score < 0:
            raise ValueError("Scores cannot be negative")
        
        match = self.matches[match_id]
        match.home_score = home_score
        match.away_score = away_score
    
    def get_summary(self) -> List[Match]:
        # Get all active matches
        active_matches = [match for match in self.matches.values()]
        
        # Sort by total score (descending)
        return sorted(
            active_matches,
            key=lambda x: x.home_score + x.away_score,
            reverse=True
        ) 