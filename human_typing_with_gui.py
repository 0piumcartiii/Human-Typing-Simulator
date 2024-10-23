import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import random

# Function to simulate typing with fatigue
def simulate_typing_fatigue(current_speed, fatigue_factor):
    """Gradually slow down typing speed to simulate fatigue."""
    return current_speed + fatigue_factor

# Function to introduce typos
def make_typo(word):
    """Introduce a typo by replacing a random character in the word."""
    if len(word) > 1:
        typo_index = random.randint(0, len(word) - 1)
        typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        word_with_typo = word[:typo_index] + typo_char + word[typo_index + 1:]
        return word_with_typo
    return word

# Main typing simulation function
def simulate_typing(text, base_typing_speed, typo_chance, pause_after_punctuation, fatigue_factor, thinking_pause):
    words = text.split(' ')
    current_speed = base_typing_speed
    
    for i, word in enumerate(words):
        # Adjust typing speed for fatigue
        current_speed = simulate_typing_fatigue(current_speed, fatigue_factor)
        
        if random.random() < typo_chance:
            word = make_typo(word)
        
        # Type the word with some variability in speed
        for char in word:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(current_speed * 0.8, current_speed * 1.2))
        
        # Type space after each word
        pyautogui.typewrite(' ')
        time.sleep(random.uniform(0.05, 0.3))  # Random pause between words

        # Pause after punctuation
        if word.endswith(('.', '!', '?')):
            time.sleep(pause_after_punctuation + random.uniform(0.2, 0.5))

        # Occasional thinking pause
        if random.random() < 0.05:  # 5% chance of a longer pause
            time.sleep(random.uniform(thinking_pause[0], thinking_pause[1]))

# Tkinter GUI setup
def create_gui():
    root = tk.Tk()
    root.title("Human-Like Typing Simulation")

    # Typing speed input
    ttk.Label(root, text="Typing Speed (seconds/char):").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
    typing_speed_slider = ttk.Scale(root, from_=0.01, to=0.5, value=0.1, orient=tk.HORIZONTAL)
    typing_speed_slider.grid(row=0, column=1, padx=10, pady=5)

    # Typo chance input
    ttk.Label(root, text="Typo Chance (0.0 to 1.0):").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    typo_chance_slider = ttk.Scale(root, from_=0.0, to=1.0, value=0.2, orient=tk.HORIZONTAL)
    typo_chance_slider.grid(row=1, column=1, padx=10, pady=5)

    # Pause after punctuation input
    ttk.Label(root, text="Pause After Punctuation (seconds):").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    punctuation_pause_entry = ttk.Entry(root)
    punctuation_pause_entry.grid(row=2, column=1, padx=10, pady=5)
    punctuation_pause_entry.insert(0, "0.6")

    # Fatigue factor input
    ttk.Label(root, text="Fatigue Factor:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    fatigue_factor_slider = ttk.Scale(root, from_=0.0, to=0.01, value=0.001, orient=tk.HORIZONTAL)
    fatigue_factor_slider.grid(row=3, column=1, padx=10, pady=5)

    # Thinking pause range
    ttk.Label(root, text="Thinking Pause Range (min, max seconds):").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    min_thinking_pause = ttk.Entry(root)
    min_thinking_pause.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
    min_thinking_pause.insert(0, "2.0")
    
    max_thinking_pause = ttk.Entry(root)
    max_thinking_pause.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)
    max_thinking_pause.insert(0, "5.0")

    # Initial delay input
    ttk.Label(root, text="Initial Delay (seconds):").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    initial_delay_entry = ttk.Entry(root)
    initial_delay_entry.grid(row=5, column=1, padx=10, pady=5)
    initial_delay_entry.insert(0, "5")

    # Text input for the body of text
    ttk.Label(root, text="Text to Type:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    text_input = tk.Text(root, width=50, height=10)
    text_input.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

    # Start button
    def on_start():
        # Retrieve user input values
        typing_speed = typing_speed_slider.get()
        typo_chance = typo_chance_slider.get()
        pause_after_punctuation = float(punctuation_pause_entry.get())
        fatigue_factor = fatigue_factor_slider.get()
        thinking_pause = [float(min_thinking_pause.get()), float(max_thinking_pause.get())]
        initial_delay = int(initial_delay_entry.get())
        text = text_input.get("1.0", tk.END).strip()

        # Initial delay before typing starts
        time.sleep(initial_delay)

        # Start typing the text
        simulate_typing(text, typing_speed, typo_chance, pause_after_punctuation, fatigue_factor, thinking_pause)

    start_button = ttk.Button(root, text="Start Typing", command=on_start)
    start_button.grid(row=8, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == '__main__':
    create_gui()
