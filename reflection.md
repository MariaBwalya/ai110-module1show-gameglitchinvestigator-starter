💭 Reflection: Game Glitch Investigator
1. What was broken when you started?

The first time I ran the game, it glitched slightly because the entry input box was missing. I had to refresh the page before it appeared. After that, the general layout of the game looked fine and it was easy to navigate, so at first it seemed like everything would work normally.

However, after testing, I noticed several issues in the gameplay logic. One major bug was the incorrect hint system. For example, when the secret number was 2 and I guessed 1, the game said “Go Lower” instead of guiding me higher. Similarly, when the secret number was 16 and I guessed 20, it said “Go Higher” instead of telling me to go lower. This showed that the hint logic was reversed.

I also noticed that the attempt counter was not working correctly. Even though the game displayed “Attempts Left: 8,” the number did not properly decrease after guesses in some cases. When I tested with the secret number 97 and submitted guesses, the attempts sometimes behaved incorrectly, showing inconsistent updates like “8 - 1” and even affecting the score (e.g., score becoming -5).

Another issue was that the game accepted guesses outside the expected range (1–100) without proper validation.

Bug Reproduction Log
Input	Expected Behavior	Actual Behavior	Console Output / Error
Secret number = 2, Guess = 1	Game should display “Go Higher” because 1 is less than 2	Game displayed “Go Lower”	No console errors observed
Secret number = 16, Guess = 20	Game should display “Go Lower” because 20 is greater than 16	Game displayed “Go Higher”	No console errors observed
Guess outside range (0 or 100)	Game should reject input and ask for valid number (1–100)	Game accepted input and still gave hints	No console errors observed
Secret number = 97, multiple guesses	Attempts should decrease by 1 per guess	Attempts did not update correctly and score showed -5	No console errors observed
2. How did you use AI as a teammate?

I used ChatGPT, Claude, and GitHub Copilot during this project. I used ChatGPT mostly at the beginning to help set up the project and understand the commands needed to run it. I then used Claude and Copilot more for debugging, understanding the logic, and helping fix issues in the code.

One correct AI suggestion came from Claude, which pointed out that the difficulty settings were unbalanced. It showed that the “Hard” mode had a smaller range than “Normal,” which actually made it easier instead of harder. I verified this by testing both modes and noticing that Hard was indeed easier to guess. After adjusting the range, I tested again and confirmed that it was now more difficult as expected.

One misleading suggestion happened during setup. ChatGPT suggested installing Streamlit and gave general troubleshooting steps when the project wasn’t running. However, the real issue was not Streamlit itself but that my Python version (3.13.13) was not being recognized properly. After several failed attempts, I discovered that the correct fix was running the command using py instead of python, which resolved the issue. I verified this by successfully running the project afterward.

3. Debugging and testing your fixes

I decided a bug was fixed when I could no longer reproduce it after applying a change. I also used AI to generate test cases for each bug, then manually tested them in the game to confirm whether the fix worked.

One test I ran was checking the hint logic. I used the developer debug information to view the secret number, then tested guesses both above and below it. For example, when the secret number was 2, guessing 1 correctly produced “Go Higher,” and when the secret number was 16, guessing 20 correctly produced “Go Lower.” This confirmed that the hint logic was fixed.

AI also helped me design test cases that I added into test_bugs.py. For example, I tested invalid inputs outside the range to confirm that the game should reject guesses like 0 or 100 depending on the difficulty rules. This helped me verify that fixes were actually working and not just visually correct.

4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script every time the user interacts with the app. For example, every time I made a guess, the whole program restarted in the background. Because of this, normal variables reset unless they are stored properly.

Session state is what allows Streamlit to remember important information between reruns. It stores values like the secret number, attempts left, and score so that the game continues properly instead of resetting every time. Without session state, the game would not be playable because it would forget everything after each interaction.

5. Looking ahead: your developer habits

One habit I want to reuse in future projects is writing structured bug cases before fixing issues. Documenting inputs, expected behavior, and actual behavior helped me clearly understand what was wrong and made debugging more effective.

Next time I work with AI, I would provide more specific context when describing bugs. I noticed that when I gave broad descriptions, it sometimes took longer for AI to identify the exact issue. Being more precise would improve the accuracy and speed of suggestions.

This project changed how I think about AI-generated code because I realized it is not always correct even when it sounds confident. Some suggestions were useful, but others were misleading or incomplete, so I learned that I always need to test and verify results instead of accepting them blindly.