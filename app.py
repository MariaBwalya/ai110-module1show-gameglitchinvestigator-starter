import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score, get_final_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

# -------------------------
# Difficulty selection
# -------------------------
difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# -------------------------
# SAFE SESSION STATE INIT
# -------------------------
if "secret" not in st.session_state:
    st.session_state.secret = None

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

# -------------------------
# Reset on difficulty change
# -------------------------
if st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = None
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []

# Ensure secret exists AFTER difficulty is known
if st.session_state.secret is None:
    st.session_state.secret = random.randint(low, high)

# -------------------------
# Game over handling
# -------------------------
st.subheader("Make a guess")

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")

    col_a, col_b = st.columns(2)
    col_a.metric("Game Score", st.session_state.score)
    col_b.metric("Final Score", get_final_score(st.session_state.score))
    st.stop()

# -------------------------
# Input
# -------------------------
raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)

with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# -------------------------
# New game logic
# -------------------------
if new_game:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

# -------------------------
# Submit guess logic
# -------------------------
if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        # Validate range
        if not (low <= guess_int <= high):
            st.error(f"Please enter a number between {low} and {high} for {difficulty} mode.")
        else:
            st.session_state.history.append(guess_int)

            outcome, message = check_guess(guess_int, st.session_state.secret)

            if show_hint:
                st.warning(message)

            score_before = st.session_state.score
            st.session_state.score = max(
                0,
                update_score(
                    current_score=st.session_state.score,
                    outcome=outcome,
                    attempt_number=st.session_state.attempts,
                )
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"

                win_points = st.session_state.score - score_before

                st.success(f"You won! The secret was {st.session_state.secret}.")

                col_a, col_b = st.columns(2)
                col_a.metric("Game Score", win_points)
                col_b.metric("Final Score", st.session_state.score)

            else:
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"

                    st.error(f"Out of attempts! The secret was {st.session_state.secret}.")

                    col_a, col_b = st.columns(2)
                    col_a.metric("Game Score", st.session_state.score)
                    col_b.metric("Final Score", get_final_score(st.session_state.score))

# -------------------------
# INFO BAR (FIXED - NO st.empty)
# -------------------------
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts} | "
    f"Score: {st.session_state.score}"
)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")