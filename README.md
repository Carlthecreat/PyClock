# Alarm Clock Application
A basic alarm clock created as a personal small project.

**Version 1.0.0**

**Date Completed: September 13, 2024**

## Overview
This application provides three main features:

1. **Clock:** Displays the current date and time.

2. **Stopwatch:** Counts upwards, displaying hours, minutes, seconds, and centiseconds. The stopwatch resets after reaching 24 hours.

3. **Timer:** Allows users to set a timer for a specific number of hours and minutes, triggering an alarm sound when the time is up.

## Features
**User-Friendly Interface:** Simple navigation with buttons to switch between the clock, stopwatch, and timer.

**Configurable Timer:** Easily set hours and minutes with combo boxes to schedule an alarm.

**Alarm Sound:** Plays a sound file when the timer expires (audio file can be customized).

**Persistent Time Display:** The clock updates every second to show the current time and date.

**Responsive Design:** Designed with PyQt6's layout managers for a clean, adaptive interface.

## Installation
### Prerequisites
1. Python 3.x
2. PyQt6
### Setup
Clone the repository:

```bash
git clone https://github.com/carlthecreat/PyClock.git
```
Navigate to the project directory:

```bash
cd PyClock
```
Install the required dependencies:

```bash
pip install PyQt6
```
Run the application:

```bash
python main.py
```
## How to Use
### Clock
Simply open the application to view the current date and time.
### Stopwatch
1. Navigate to the Stopwatch tab using the "Stopwatch" button.
2. Click "Start" to begin counting time.
3. Click "Stop" to pause the stopwatch.
4. Click "Reset" to reset the stopwatch to zero.

### Timer
1. Navigate to the Timer tab using the "Timer" button.
2. Use the combo boxes to set the desired hours and minutes.
3. Click "Enter" to start the timer.
4. An alarm sound will play when the timer reaches zero.
5. Click "Reset" to stop the alarm and reset the timer.

## Customization
Alarm Sound: Replace the audio/clock sound.wav file with your preferred sound file. Ensure it is in .wav format for compatibility.

## Troubleshooting
If the alarm sound does not play, ensure the sound file path is correct and the file format is supported. The default path is set to audio/clock sound.wav.

## License
This project is licensed under the MIT License.

## Acknowledgments
Created using PyQt6.
