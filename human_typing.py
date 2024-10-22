import pyautogui
import time
import random

# Define the initial body of text (can be replaced later by user input)
text = """Input the text you want the script to type out here."""

# Typing speed control
base_typing_speed = 0.1  # Base typing speed (average delay per character)
punctuation_pause = 0.6  # Longer pause after punctuation
fatigue_factor = 0.001  # How much to slow down typing speed over time
thinking_pause = random.uniform(2, 5)  # Occasional thinking pauses

# Initial delay to allow you to focus the cursor on the document
initial_delay = 5  # seconds
print(f"Starting in {initial_delay} seconds...")
time.sleep(initial_delay)

def simulate_typing_fatigue(current_speed):
    """Gradually slow down typing speed to simulate fatigue."""
    return current_speed + fatigue_factor

def make_typo(word):
    """Introduce a typo by replacing a random character in the word."""
    if len(word) > 1:
        typo_index = random.randint(0, len(word) - 1)
        typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        word_with_typo = word[:typo_index] + typo_char + word[typo_index + 1:]
        return word_with_typo
    return word

def introduce_capitalization_error(word):
    """Introduce random capitalization error."""
    error_index = random.randint(0, len(word) - 1)
    wrong_case_word = word[:error_index] + word[error_index].upper() + word[error_index + 1:]
    return wrong_case_word

def substitute_word():
    """Return a random substitute word to simulate human rethinking."""
    substitutes = ['alternative', 'solution', 'consideration', 'debate', 'thought']
    return random.choice(substitutes)

def type_word(word, typo_chance=0.2, cap_error_chance=0.1, leave_misspelled_chance=0.1, substitution_chance=0.05):
    """Types a word with possible typos, capitalization errors, and corrections."""
    typo_made = False
    cap_error_made = False

    # Random word substitution
    if random.random() < substitution_chance:
        word = substitute_word()

    # Random capitalization error
    if random.random() < cap_error_chance:
        word_with_cap_error = introduce_capitalization_error(word)
        for char in word_with_cap_error:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(base_typing_speed * 0.8, base_typing_speed * 1.2))
        cap_error_made = True
        
        # Correct capitalization error
        if cap_error_made:
            pyautogui.typewrite('\b' * len(word_with_cap_error))
            time.sleep(random.uniform(0.2, 0.4))  # Pause after backspacing
            for char in word:
                pyautogui.typewrite(char)
                time.sleep(random.uniform(base_typing_speed * 0.8, base_typing_speed * 1.2))
        return
    
    # Introduce typo randomly
    if random.random() < typo_chance:
        typo_word = make_typo(word)
        for char in typo_word:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(base_typing_speed * 0.8, base_typing_speed * 1.2))
        typo_made = True

        # Correct the typo or leave it uncorrected
        if typo_made and random.random() > leave_misspelled_chance:
            pyautogui.typewrite('\b' * len(typo_word))
            time.sleep(random.uniform(0.3, 0.6))  # Pause after backspacing
            for char in word:
                pyautogui.typewrite(char)
                time.sleep(random.uniform(base_typing_speed * 0.8, base_typing_speed * 1.2))
        else:
            return  # Leave the typo uncorrected
    else:
        # Type the word normally
        for char in word:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(base_typing_speed * 0.8, base_typing_speed * 1.2))

def simulate_typing(text):
    """Simulates typing the entire text with random pauses, mistakes, and distractions."""
    words = text.split(' ')
    current_speed = base_typing_speed
    
    for i, word in enumerate(words):
        # Adjust typing speed for fatigue
        current_speed = simulate_typing_fatigue(current_speed)
        
        type_word(word)

        # Add a space after each word
        pyautogui.typewrite(' ')
        time.sleep(random.uniform(0.05, 0.3))  # Random pause between words

        # Longer pause after punctuation
        if word.endswith(('.', '!', '?')):
            time.sleep(punctuation_pause + random.uniform(0.2, 0.5))

        # Occasional thinking pause (longer hesitation)
        if random.random() < 0.05:  # 5% chance of a longer "thinking" pause
            time.sleep(random.uniform(2.0, 5.0))  # Simulate longer "thinking" pauses

        # Simulate word repetition error and correction
        if random.random() < 0.02:  # 2% chance of repeating a word
            pyautogui.typewrite(word + " ")
            time.sleep(0.1)
            pyautogui.typewrite('\b' * (len(word) + 1))  # Backspace the repeated word

# Start typing the first body of text
simulate_typing(text)

# Allow user to input new text and continue typing
while True:
    new_text = input("Enter a new body of text to type, or type 'exit' to quit: ")

    if new_text.lower() == 'exit':
        print("Exiting the typing simulation.")
        break
    
    # Type the new body of text
    simulate_typing(new_text)
