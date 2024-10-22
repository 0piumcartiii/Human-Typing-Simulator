# Human-Like Typing Simulation in Python

This Python script simulates human-like typing behavior by introducing randomness, mistakes, fatigue, and other natural typing behaviors. The simulation can be used to automate typing in any document (like Google Docs) while mimicking real human typing patterns.

## Features

- **Typing Fatigue**: Gradual slowing of typing speed over time to mimic fatigue.
- **Random Typos**: Introduces typos, some of which are corrected, while others are left uncorrected.
- **Capitalization Errors**: Occasionally makes random capitalization mistakes, some of which are fixed.
- **Word Repetition**: Simulates typing a word twice by mistake and then correcting it.
- **Word Substitution**: Randomly substitutes words with similar ones to simulate rethinking.
- **Pauses**: Varying pauses between words and sentences, with longer pauses after punctuation and occasional "thinking" pauses.
- **Dynamic User Input**: After the first block of text, users can input new text to continue typing.

## Installation

### Prerequisites

- Python 3.x
- `pyautogui` library

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/human-typing-simulation.git
    ```

2. Navigate into the project directory:
    ```bash
    cd human-typing-simulation
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python human_typing.py
    ```

2. The script will give you 5 seconds to focus the cursor on the document where you want the text to be typed.
   
3. The script will begin typing the predefined text.

4. After the initial text is typed, you'll be prompted to input new text to simulate typing dynamically. You can keep inputting new text, or type `exit` to quit the simulation.

## Customization

- **Typing Speed**: Adjust the `base_typing_speed` variable to control the average typing speed.
- **Typos**: Adjust `typo_chance` and `leave_misspelled_chance` to control the frequency of typos and how often they are left uncorrected.
- **Capitalization Errors**: Control capitalization mistake frequency by adjusting `cap_error_chance`.
- **Substitution
