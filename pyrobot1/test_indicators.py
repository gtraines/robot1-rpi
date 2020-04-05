import time
from indicators import Indicator, blink_some_indicators
from pinmap import RowNames, RPi3Pins


class GreenRedIndicator:
    def __init__(self, green_pin_tuple, red_pin_tuple, high_is_on=True):
        self._green_indicator = Indicator(green_pin_tuple, high_is_on)
        self._red_indicator = Indicator(red_pin_tuple, high_is_on)
    
    def blink_amber(self, times):
        for _ in range(times):
            self.turn_on_amber()
            time.sleep(0.25)
            self.turn_off_amber()
            time.sleep(0.25)
        self.turn_off_amber()
        
    def blink_green(self, times):
        self._green_indicator.blink_times(times)
        
    def blink_red(self, times):
        self._red_indicator.blink_times(times)
        
    def turn_off(self):
        self.turn_off_amber()
    
    def turn_off_amber(self):
        self._green_indicator.turn_off()
        self._red_indicator.turn_off()
        
    def turn_off_green(self):
        self._green_indicator.turn_off()

    def turn_off_red(self):
        self._red_indicator.turn_off()

    def turn_on(self):
        self._turn_on_amber()
    
    def turn_on_amber(self):
        self._green_indicator.turn_on()
        self._red_indicator.turn_on()

    def turn_on_green(self):
        self._green_indicator.turn_on()
            
    def turn_on_red(self):
        self._red_indicator.turn_on()


if __name__ == '__main__':
    #blink_some_indicators()
    
    green_indicator_tuple = RPi3Pins.get_pin_at(RowNames.OUTER, 18)
    red_indicator_tuple = RPi3Pins.get_pin_at(RowNames.OUTER, 17)
    
    gra_indicator = GreenRedIndicator(green_indicator_tuple, red_indicator_tuple)
    
    gra_indicator.blink_green(3)
    gra_indicator.blink_red(3)
    gra_indicator.blink_amber(3)
    