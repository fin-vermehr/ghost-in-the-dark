# Ghost in the Dark

A fun project that plays random sounds in dark environments using a Raspberry Pi Zero 2 W. The device detects ambient light levels and plays random audio clips when it's dark, stopping when lights are turned on.

## Hardware Requirements

<img width="655" alt="Screenshot 2025-01-12 at 10 52 37 PM" src="https://github.com/user-attachments/assets/8cbf1ed7-9f7b-4b4c-843d-08e8fed7685c" />

### Core Electronics
- Raspberry Pi Zero 2 W (main computer)
- GL5516 Photoresistor/LDR (light detection)
- PAM8403 amplifier module (audio amplification)
- 4Ω 3W mini speakers
- 10kΩ resistor

  

### Power & Storage
- Anker PowerCore 10000 battery pack
- 16GB SanDisk microSD card

### Connection & Mounting
- Mini breadboard
- Dupont wires
- Double-sided tape
- 5x7 mat board

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/fin-vermehr/ghost-in-the-dark
cd prank_machine
```

2. Create and activate a Python virtual environment:
```bash
pyenv virtualenv 3.11.7 arduino_prank
pyenv activate arduino_prank
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. Run the tests:
```bash
pytest tests/
```

## Project Structure
```
prank_machine/
├── pyproject.toml          # Project configuration
├── src/
│   ├── __init__.py
│   ├── mock_gpio.py       # GPIO simulator for development
│   └── prank_device.py    # Main device code
├── tests/
│   ├── __init__.py
│   └── test_prank_device.py
└── sounds/                 # Directory for sound files
```

## Hardware Setup

1. Flash Raspberry Pi OS to the SD card
2. Configure WiFi/SSH for headless setup
3. Mount components on mat board following the wiring diagram:
   - LDR + 10kΩ resistor to GPIO4
   - PAM8403 amp to Pi's audio out
   - Speakers to amp
   - Power via USB-C

## Usage

1. Add MP3 sound files to the `sounds` directory
2. Run the program:
```bash
python -m src.prank_device
```

The device will:
- Monitor ambient light levels
- Play random sounds when it's dark
- Stop playing when lights are turned on
- Wait at least 30 seconds between sounds

## Development Mode

The project includes a mock GPIO module for development without hardware. This allows you to:
- Test the logic without a Raspberry Pi
- Simulate light level changes
- Debug sound file handling

## Testing

Run the test suite:
```bash
pytest tests/
```
