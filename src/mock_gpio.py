# src/mock_gpio.py

class MockGPIO:
    BCM = "BCM"
    BOARD = "BOARD"
    IN = "IN"
    OUT = "OUT"
    HIGH = 1
    LOW = 0
    
    def __init__(self):
        self.mode = None
        self.pin_states = {}
        self.warnings = True
        
    def setmode(self, mode):
        """Set the pin numbering mode"""
        self.mode = mode
        
    def setup(self, pin, mode, initial=None, pull_up_down=None):
        """Setup a GPIO pin"""
        self.pin_states[pin] = {
            'mode': mode,
            'value': initial if initial is not None else self.LOW
        }
        
    def input(self, pin):
        """Read value from a GPIO pin"""
        if pin not in self.pin_states:
            raise RuntimeError(f"Pin {pin} not setup")
        return self.pin_states[pin]['value']
        
    def output(self, pin, value):
        """Set output value for a GPIO pin"""
        if pin not in self.pin_states:
            raise RuntimeError(f"Pin {pin} not setup")
        if self.pin_states[pin]['mode'] != self.OUT:
            raise RuntimeError(f"Pin {pin} not set as output")
        self.pin_states[pin]['value'] = value
        
    def cleanup(self, pin=None):
        """Clean up GPIO pins"""
        if pin is None:
            self.pin_states.clear()
        else:
            if pin in self.pin_states:
                del self.pin_states[pin]
                
    def setwarnings(self, state):
        """Enable or disable warnings"""
        self.warnings = state

# Create a singleton instance
GPIO = MockGPIO()