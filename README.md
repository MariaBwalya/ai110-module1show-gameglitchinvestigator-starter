# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ x] Describe the game's purpose.
A number-guessing game where the player selects a difficulty (Easy, Normal, Hard), then tries to guess a randomly generated secret number within a limited number of attempts. Each guess gives feedback (“Go Higher” or “Go Lower”), and the player earns or loses score based on performance until they either guess correctly or run out of attempts.
- [ x] Detail which bugs you found.
1. Reversed hint logic — The game gave incorrect directional hints. For example, when the secret number was 2 and the guess was 1, the game incorrectly said “Go Lower” instead of guiding the player higher. Similarly, when the secret number was 16 and the guess was 20, it incorrectly said “Go Higher” instead of telling the player to go lower.
2. Attempts not updating correctly — The attempts counter did not consistently decrease after each guess. In some cases, even though guesses were submitted, “Attempts Left: 8” remained unchanged, and the scoring system showed inconsistent updates (e.g., score becoming -5 unexpectedly after a guess like 97).
3. Out-of-range guesses accepted — The game allowed invalid inputs outside the expected range (1–100) and still processed them instead of rejecting them with proper validation.
4. New Game state inconsistency — Clicking “New Game” refreshed the page and displayed a game-over message instead of fully resetting into a fresh playable state.
5. Inconsistent repeated-guess behavior — Entering the same guess multiple times caused inconsistent feedback, where hints alternated between “Go Higher” and “Go Lower” even though the input did not change.
- [x ] Explain what fixes you applied.
1. Corrected hint logic direction — Fixed the comparison logic so that guesses lower than the secret number now correctly return “Go Higher,” and guesses higher return “Go Lower.”
2. Fixed attempt tracking logic — Ensured that the attempt counter properly increments once per valid guess and updates consistently across all game states.
3 . Added input validation for range — Implemented a check that rejects guesses outside the valid difficulty range (1–100), preventing invalid inputs from affecting game logic.
4. Improved New Game reset behavior — Updated the reset logic so that starting a new game properly resets the secret number, attempts, score, and game status instead of partially resetting state.
5. Stabilized game state handling for repeated inputs — Adjusted logic so repeated guesses no longer cause inconsistent or alternating feedback.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```

pytest tests/
======================================= test session starts =======================================
platform win32 -- Python 3.13.7, pytest-9.1.0, pluggy-1.6.0 -- C:\Users\themb\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\themb\OneDrive\Documents\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 24 items                                                                                 

tests/test_game_logic.py::test_winning_guess PASSED                                          [  4%]
tests/test_game_logic.py::test_too_high_message_tells_player_to_go_lower PASSED              [  8%]
tests/test_game_logic.py::test_too_low_message_tells_player_to_go_higher PASSED              [ 12%]
tests/test_game_logic.py::test_too_high_message_correct_when_secret_is_string PASSED         [ 16%]
tests/test_game_logic.py::test_too_low_message_correct_when_secret_is_string PASSED          [ 20%]
tests/test_game_logic.py::test_easy_rejects_guess_above_range PASSED                         [ 25%]
tests/test_game_logic.py::test_hard_rejects_guess_above_range PASSED                         [ 29%]
tests/test_game_logic.py::test_hard_range_upper_bound_is_150 PASSED                          [ 33%]
tests/test_game_logic.py::test_hard_range_is_larger_than_normal PASSED                       [ 37%]
tests/test_game_logic.py::test_new_game_state_resets_status_to_playing PASSED                [ 41%]
tests/test_game_logic.py::test_new_game_state_respects_difficulty_range PASSED               [ 45%]
tests/test_game_logic.py::test_win_on_first_attempt_gives_100_points PASSED                  [ 50%]
tests/test_game_logic.py::test_win_on_later_attempt_scores_less PASSED                       [ 54%]
tests/test_game_logic.py::test_win_score_floor_is_10 PASSED                                  [ 58%]
tests/test_game_logic.py::test_too_high_on_even_attempt_deducts_points PASSED                [ 62%]
tests/test_game_logic.py::test_too_high_on_odd_attempt_deducts_points PASSED                 [ 66%]
tests/test_game_logic.py::test_too_high_and_too_low_penalize_equally PASSED                  [ 70%]
tests/test_game_logic.py::test_wrong_guess_score_never_goes_below_zero PASSED                [ 75%]
tests/test_game_logic.py::test_multiple_wrong_guesses_stay_at_zero PASSED                    [ 79%]
tests/test_game_logic.py::test_final_score_clamps_negative_to_zero PASSED                    [ 83%]
tests/test_game_logic.py::test_final_score_preserves_positive_score PASSED                   [ 87%]
tests/test_game_logic.py::test_final_score_is_zero_when_raw_is_zero PASSED                   [ 91%]
tests/test_game_logic.py::test_info_bar_shows_correct_attempts_before_any_guess PASSED       [ 95%]
tests/test_game_logic.py::test_info_bar_decrements_immediately_after_submit PASSED           [100%]

======================================= 24 passed in 2.46s ========================================



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
