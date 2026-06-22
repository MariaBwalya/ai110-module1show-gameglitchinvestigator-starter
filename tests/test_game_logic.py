from logic_utils import (
    check_guess,
    update_score,
    get_final_score,
    get_range_for_difficulty,
    build_new_game_state,
)

from streamlit.testing.v1 import AppTest


# -----------------------------
# check_guess basics
# -----------------------------

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


# -----------------------------
# Bug 1: Hint correctness
# -----------------------------

def test_too_high_returns_lower_hint():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower()

def test_too_low_returns_higher_hint():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower()

def test_hint_works_with_string_secret():
    outcome, message = check_guess(80, "50")
    assert outcome == "Too High"
    assert "lower" in message.lower()

def test_hint_works_with_string_secret_low():
    outcome, message = check_guess(13, "20")
    assert outcome == "Too Low"
    assert "higher" in message.lower()


# -----------------------------
# Bug 2: Range validation
# -----------------------------

def test_easy_range_validation():
    low, high = get_range_for_difficulty("Easy")
    assert 25 > high  # confirms 25 is outside range

def test_hard_range_validation():
    low, high = get_range_for_difficulty("Hard")
    assert 200 > high


# -----------------------------
# Bug 3: Difficulty scaling
# -----------------------------

def test_hard_upper_bound_is_150():
    _, high = get_range_for_difficulty("Hard")
    assert high == 150

def test_hard_is_larger_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high


# -----------------------------
# Bug 4: New game state reset
# -----------------------------

def test_new_game_state_is_playing():
    state = build_new_game_state("Normal")
    assert state["status"] == "playing"

def test_new_game_state_within_range():
    state = build_new_game_state("Easy")
    _, high = get_range_for_difficulty("Easy")
    assert state["secret"] <= high


# -----------------------------
# Bug 5: Scoring logic
# -----------------------------

def test_win_first_attempt_score():
    score = update_score(0, "Win", 1)
    assert score == 100

def test_win_later_attempt_less_score():
    score1 = update_score(0, "Win", 1)
    score5 = update_score(0, "Win", 5)
    assert score5 < score1

def test_win_score_floor():
    score = update_score(0, "Win", 20)
    assert score == 10

def test_penalty_applies_to_too_high():
    score = update_score(50, "Too High", 2)
    assert score < 50

def test_penalty_applies_to_too_low():
    score = update_score(50, "Too Low", 2)
    assert score < 50

def test_penalties_are_equal():
    high = update_score(50, "Too High", 2)
    low = update_score(50, "Too Low", 2)
    assert high == low

def test_score_never_negative():
    raw = update_score(0, "Too Low", 1)
    assert max(0, raw) == 0

def test_multiple_penalties_stay_zero():
    score = 0
    for attempt in range(5):
        score = max(0, update_score(score, "Too Low", attempt))
    assert score == 0

def test_final_score_clamps_negative():
    assert get_final_score(-25) == 0

def test_final_score_positive():
    assert get_final_score(80) == 80


# -----------------------------
# Bug 6: Streamlit UI (AppTest)
# -----------------------------

def test_info_bar_shows_attempts_initially():
    at = AppTest.from_file("app.py").run()
    assert at.info
    assert "Attempts left:" in at.info[0].value


def test_info_bar_updates_after_guess():
    at = AppTest.from_file("app.py").run()

    at.text_input[0].set_value("50")
    at.button[0].click().run()

    assert at.info
    assert "Attempts left:" in at.info[0].value