# src/prank_device.py

import time
import random
from pathlib import Path
import platform

# Conditionally import GPIO based on platform
if platform.system() == 'Linux' and 'raspberrypi' in platform.uname().version.lower():
    import RPi.GPIO as GPIO
else:
    from .mock_gpio import GPIO

class PrankDevice:
    def __init__(self, ldr_pin=4, sound_dir="sounds"):
        """Initialize the prank device"""
        self.ldr_pin = ldr_pin
        self.sound_dir = Path(sound_dir)
        self.setup_gpio()
        
    def setup_gpio(self):
        """Initialize GPIO settings"""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ldr_pin, GPIO.IN)
        
    def get_rc_time(self):
        """
        Get RC time from LDR
        In development: returns mock values
        On Pi: will return actual RC time
        """
        if platform.system() != 'Linux' or 'raspberrypi' not in platform.uname().version.lower():
            return random.randint(0, 1000)
            
        count = 0
        GPIO.setup(self.ldr_pin, GPIO.OUT)
        GPIO.output(self.ldr_pin, GPIO.LOW)
        time.sleep(0.1)
        
        GPIO.setup(self.ldr_pin, GPIO.IN)
        while GPIO.input(self.ldr_pin) == GPIO.LOW and count < 1000:
            count += 1
        return count
        
    def is_dark(self, threshold=500):
        """Check if environment is dark enough"""
        rc_time = self.get_rc_time()
        return rc_time > threshold
    
    def list_sound_files(self):
        """List all available sound files"""
        return list(self.sound_dir.glob("*.mp3"))
    
    def play_random_sound(self):
        """
        Play a random sound file
        In development: just prints the action
        On Pi: will actually play the sound
        """
        sound_files = self.list_sound_files()
        if sound_files:
            chosen_file = random.choice(sound_files)
            print(f"Playing sound: {chosen_file.name}")
            # Actual sound playing code will be added when hardware is available
            time.sleep(1)  # Simulate sound duration
            
    def cleanup(self):
        """Cleanup GPIO resources"""
        GPIO.cleanup()

def main():
    device = PrankDevice()
    print("Prank device initialized!")
    last_play_time = 0
    min_interval = 30  # Minimum seconds between sounds
    
    try:
        while True:
            current_time = time.time()
            if current_time - last_play_time >= min_interval:
                if device.is_dark():
                    device.play_random_sound()
                    last_play_time = current_time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        device.cleanup()

if __name__ == "__main__":
    main()