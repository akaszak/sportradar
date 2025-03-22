import pytest
from src.scoreboard import ScoreBoard

def test_start_match():
    scoreboard = ScoreBoard()
    match_id = scoreboard.start_match("Mexico", "Canada")
    
    assert match_id is not None
    assert isinstance(match_id, str)
    assert len(match_id) > 0

def test_start_match_with_empty_teams():
    scoreboard = ScoreBoard()
    
    with pytest.raises(ValueError):
        scoreboard.start_match("", "Canada")
    
    with pytest.raises(ValueError):
        scoreboard.start_match("Mexico", "")
    
    with pytest.raises(ValueError):
        scoreboard.start_match("", "")

def test_start_match_with_same_team():
    scoreboard = ScoreBoard()
    
    with pytest.raises(ValueError):
        scoreboard.start_match("Mexico", "Mexico")

def test_finish_match():
    scoreboard = ScoreBoard()
    match_id = scoreboard.start_match("Mexico", "Canada")
    
    scoreboard.finish_match(match_id)
    assert match_id not in scoreboard.matches

def test_finish_nonexistent_match():
    scoreboard = ScoreBoard()
    
    with pytest.raises(KeyError):
        scoreboard.finish_match("nonexistent_id")

def test_update_score():
    scoreboard = ScoreBoard()
    match_id = scoreboard.start_match("Mexico", "Canada")
    
    scoreboard.update_score(match_id, 0, 5)
    match = scoreboard.matches[match_id]
    assert match.home_score == 0
    assert match.away_score == 5

def test_update_score_nonexistent_match():
    scoreboard = ScoreBoard()
    
    with pytest.raises(KeyError):
        scoreboard.update_score("nonexistent_id", 0, 5)

def test_update_score_negative():
    scoreboard = ScoreBoard()
    match_id = scoreboard.start_match("Mexico", "Canada")
    
    with pytest.raises(ValueError):
        scoreboard.update_score(match_id, -1, 0)
    
    with pytest.raises(ValueError):
        scoreboard.update_score(match_id, 0, -1)

def test_get_summary():
    scoreboard = ScoreBoard()
    
    # Start matches with different scores
    match1_id = scoreboard.start_match("Mexico", "Canada")
    match2_id = scoreboard.start_match("Spain", "Brazil")
    match3_id = scoreboard.start_match("Germany", "France")
    
    # Update scores
    scoreboard.update_score(match1_id, 0, 5)  # Total: 5
    scoreboard.update_score(match2_id, 10, 2)  # Total: 12
    scoreboard.update_score(match3_id, 2, 2)  # Total: 4
    
    # Get summary
    summary = scoreboard.get_summary()
    
    # Verify order: highest total score first
    assert len(summary) == 3
    assert summary[0].home_team == "Spain"  # Highest score (12)
    assert summary[1].home_team == "Mexico"  # Second highest (5)
    assert summary[2].home_team == "Germany"  # Lowest score (4)

def test_get_summary_with_same_total_score():
    scoreboard = ScoreBoard()
    
    # Start matches with same total scores
    match1_id = scoreboard.start_match("Mexico", "Canada")
    match2_id = scoreboard.start_match("Spain", "Brazil")
    
    # Update scores to have same total
    scoreboard.update_score(match1_id, 3, 2)  # Total: 5
    scoreboard.update_score(match2_id, 4, 1)  # Total: 5
    
    # Get summary
    summary = scoreboard.get_summary()
    
    # Verify both matches are included
    assert len(summary) == 2
    assert all(match.home_score + match.away_score == 5 for match in summary)

def test_get_summary_with_finished_matches():
    scoreboard = ScoreBoard()
    
    # Start and update matches
    match1_id = scoreboard.start_match("Mexico", "Canada")
    match2_id = scoreboard.start_match("Spain", "Brazil")
    
    scoreboard.update_score(match1_id, 0, 5)
    scoreboard.update_score(match2_id, 10, 2)
    
    # Finish one match
    scoreboard.finish_match(match1_id)
    
    # Get summary
    summary = scoreboard.get_summary()
    
    # Verify only active matches are included
    assert len(summary) == 1
    assert summary[0].home_team == "Spain" 