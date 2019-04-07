from RPi import GPIO as gpio
import time
from pinmap import RPi3Pins, PinTypes, RowNames


class Indicator:
    
    def __init__(self, pin_tuple, high_is_on=True):
        self._pin_tuple = pin_tuple
        self._pin_num = pin_tuple.id
        self._high_is_on = high_is_on
        self._set_pin_mode()
        
    def _set_pin_mode(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self._pin_num, gpio.OUT)
        
    def turn_on(self):
        if self._high_is_on:
            gpio.output(self._pin_num, gpio.HIGH)
        else:
            gpio.output(self._pin_num, gpio.LOW)

    def turn_off(self):
        if self._high_is_on:
            gpio.output(self._pin_num, gpio.LOW)
        else:
            gpio.output(self._pin_num, gpio.HIGH)

    def blink_times(self, num_times):
        for _ in range(num_times):
            self.turn_on()
            time.sleep(0.25)
            self.turn_off()
            time.sleep(0.25)
        self.turn_off()
    

def get_available_gpio_pins():
    gpio_pins = RPi3Pins.get_pins_by_type(PinTypes.GPIO)
    return gpio_pins

class StatusIndicators:

    def __init__(self):
        gpio_pins = get_available_gpio_pins()
        
        self._right_side_pins = [pin for pin in gpio_pins \
                                 if pin.coords.row_name == RowNames.OUTER and pin.coords.pin_pair_num >= 17]

        self._left_side_pins = [pin for pin in gpio_pins \
                                 if pin.coords.row_name == RowNames.INNER and pin.coords.pin_pair_num >= 16]

        
def main():
    indicators = StatusIndicators()
    for pin in indicators._right_side_pins:
        print(pin.id, pin.coords)
    for pin in indicators._left_side_pins:
        print(pin.id, pin.coords)


def blink_some_indicators():
    for pin in get_available_gpio_pins():
        if pin.coords.pin_pair_num > 15:
            print(pin.id, pin.coords)
            led = Indicator(pin, False)
            led.blink_times(5)

if __name__ == '__main__':
    main()

