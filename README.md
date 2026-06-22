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

1. The user opens the game and is shown a guessing interface with a selected difficulty (Easy, Normal, or Hard). The game displays the valid range (for example, 1–100 in Normal mode), along with the number of attempts allowed and current score.
2. The user enters an initial guess (for example, guess = 1). The game responds with a hint like “Go Higher” if the secret number is larger, or “Go Lower” if the guess is too high.
3. The user continues guessing (for example, guess = 20 or guess = 38), and the game consistently updates the hint correctly based on the comparison with the secret number.
4. After each valid guess, the attempt counter decreases correctly and the score updates based on performance. The info bar reflects the current attempts left and score in real time
5. If the user eventually enters the correct number (for example, guess = 97), the game displays a win message, triggers a success state, and shows the final score.
6. If the user runs out of attempts before guessing correctly, the game ends with a “Game Over” message and reveals the secret number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results
This project was tested using both Streamlit gameplay and automated pytest tests.
```

pytest tests/
======================================= test session starts =======================================
platform win32 -- Python 3.13.7, pytest-9.1.0, pluggy-1.6.0 -- C:\Users\themb\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\themb\OneDrive\Documents\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 23 items                                                                                 

tests/test_game_logic.py::test_winning_guess PASSED                                          [  4%]
tests/test_game_logic.py::test_too_high_returns_lower_hint PASSED                            [  8%]
tests/test_game_logic.py::test_too_low_returns_higher_hint PASSED                            [ 13%]
tests/test_game_logic.py::test_hint_works_with_string_secret PASSED                          [ 17%]
tests/test_game_logic.py::test_hint_works_with_string_secret_low PASSED                      [ 21%]
tests/test_game_logic.py::test_easy_range_validation PASSED                                  [ 26%]
tests/test_game_logic.py::test_hard_range_validation PASSED                                  [ 30%]
tests/test_game_logic.py::test_hard_upper_bound_is_150 PASSED                                [ 34%]
tests/test_game_logic.py::test_hard_is_larger_than_normal PASSED                             [ 39%]
tests/test_game_logic.py::test_new_game_state_is_playing PASSED                              [ 43%]
tests/test_game_logic.py::test_new_game_state_within_range PASSED                            [ 47%]
tests/test_game_logic.py::test_win_first_attempt_score PASSED                                [ 52%]
tests/test_game_logic.py::test_win_later_attempt_less_score PASSED                           [ 56%]
tests/test_game_logic.py::test_win_score_floor PASSED                                        [ 60%]
tests/test_game_logic.py::test_penalty_applies_to_too_high PASSED                            [ 65%]
tests/test_game_logic.py::test_penalty_applies_to_too_low PASSED                             [ 69%]
tests/test_game_logic.py::test_penalties_are_equal PASSED                                    [ 73%]
tests/test_game_logic.py::test_score_never_negative PASSED                                   [ 78%]
tests/test_game_logic.py::test_multiple_penalties_stay_zero PASSED                           [ 82%]
tests/test_game_logic.py::test_final_score_clamps_negative PASSED                            [ 86%]
tests/test_game_logic.py::test_final_score_positive PASSED                                   [ 91%]
tests/test_game_logic.py::test_info_bar_shows_attempts_initially PASSED                      [ 95%]
tests/test_game_logic.py::test_info_bar_updates_after_guess PASSED                           [100%]

======================================= 23 passed in 1.06s ========================================




## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
