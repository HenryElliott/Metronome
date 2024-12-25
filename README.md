# AIO-Metronome

This metronome tool is designed to help improve your prayer flicking timing in Old School RuneScape. It features both a visual and auditory cue to help synchronize your flicking with the game's mechanics. You can customize the beats per minute (BPM) and control the metronome with a keybinding.

## Features
- **Visual Metronome**: A flashing window that provides a visual cue for each beat.
- **Auditory Metronome**: A customizable beep sound played at the set BPM.
- **Customizable BPM**: Adjust the metronome's BPM (beats per minute) to match your flicking speed.
- **Keybinding Control**: Start and stop the metronome with `Ctrl + Shift + C`.
- **Movable Window**: The metronome window can be moved anywhere on your screen.

## Requirements
- Python 3.x
- `pygame` library (for sound playback)
- `keyboard` library (for detecting key presses)
- A `.wav` file for the beep sound (you can use any `.wav` file you prefer)

## Installation
- Install required dependencies.
  `pip install pygame keyboard`
- Place beep.wav file in the same directory as the script. (ONLY IF USING YOUR OWN SOUND!)

## Usage
- Run the script using python
  `python metronome.py`
- The metronome window will appear. To Start and stop the metronome press `Ctrl + Shift + C`
- The visual cue will flash, and the sound will play at the set BPM (default is 25 BPM for OSRS, but you can adjust it in the code.)

## Keybindings
- `Ctrl + Shift + C` Toggles the metronome on and off.

## Customization
- To adjust the beats per minute (BPM) of the metronome, change the BPM variable in the script. For example:
  `BPM = 100` = Set the BPM to 100 beats per minute

