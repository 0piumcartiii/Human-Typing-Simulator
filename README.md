
# Human Typing with GUI Simulation

This project simulates human typing with fatigue, introduces random typos, and slows typing speed over time. 
It includes a graphical user interface (GUI) built using `tkinter` and uses `pyautogui` to interact with the system.

## Features
- Simulates typing speed changes due to fatigue.
- Introduces random typos.
- Allows setting of typing speed, chance of typos, and other custom parameters.

## Prerequisites

Make sure you have Python installed (version 3.6 or later).

You also need to install the following Python libraries:

```bash
pip install pyautogui
pip install tkinter
```

## Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

> Note: Make sure to add `pyautogui` and `tkinter` to your `requirements.txt`.

## Usage

1. Run the Python script:

```bash
python human_typing_with_gui.py
```

2. The GUI will open, allowing you to adjust parameters like:
   - Typing speed
   - Typo frequency
   - Pause duration

3. Watch as the simulated typing takes place with the settings you have chosen.

## Customization

You can modify the script to adjust:
- Base typing speed
- Typo chance
- Fatigue factor
- Thinking pause

These parameters are available in the `simulate_typing` function inside the script.

## License

This project is licensed under the MIT License.
