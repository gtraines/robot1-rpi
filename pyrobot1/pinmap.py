from collections import namedtuple
from itertools import chain


class RowNames:
    OUTER="outer"
    INNER="inner"

class PinTypes:
    GPIO="gpio"
    POWER_5V="5V+"
    POWER_3V3="3V3+"
    GND="GND"
    I2C="i2c"
    EEPROM="EEPROM"

Pin = namedtuple("Pin", "coords, id, pin_type, special_func")
PinCoords = namedtuple("PinCoords", "row_name, pin_pair_num")
Row = namedtuple("Row", "row_name, pins")
Column = namedtuple("Column", "column_num, outer_pin, inner_pin")

class RPi3Pins:
    
    def __init__(self):
        pass

    @staticmethod
    def get_pins_by_type(pin_type):
        query_results = []

        for entry in chain.from_iterable([
            RPi3Pins.outer_row().pins,
            RPi3Pins.inner_row().pins
            ]):
            if entry.pin_type == pin_type:
                query_results.append(entry)

        return query_results
    
    @staticmethod
    def get_pin_at(inner_or_outer, pair_index):
        if inner_or_outer == RowNames.OUTER:
            return RPi3Pins.outer_row().pins[pair_index]
        
        if inner_or_outer == RowNames.INNER:
            return RPi3Pins.inner_row().pins[pair_index]
            
    
    @staticmethod
    def outer_row(): 
        return Row(row_name=RowNames.OUTER, pins=[
            Pin(
                coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=0),
                id=None,
                pin_type=PinTypes.POWER_5V,
                special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=1),
            id=None,
            pin_type=PinTypes.POWER_5V,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=2),
            id=None,
            pin_type=PinTypes.GND,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=3),
            id=14,
            pin_type=PinTypes.GPIO,
            special_func="TXD0"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=4),
            id=15,
            pin_type=PinTypes.GPIO,
            special_func="RXD0"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=5),
            id=18,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_1"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=6),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=7),
            id=23,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_4"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=8),
            id=24,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_5"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=9),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=10),
            id=25,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_6"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=11),
            id=8,
            pin_type=PinTypes.GPIO,
            special_func="SPI_CE0_N"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=12),
            id=7,
            pin_type=PinTypes.GPIO,
            special_func="SPI_CE1_N"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=13),
            id=0,
            pin_type=PinTypes.EEPROM,
            special_func="I2C EEPROM ID_SC"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=14),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=15),
            id=12,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=16),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=17),
            id=16,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=18),
            id=20,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.OUTER, pin_pair_num=19),
            id=21,
            pin_type=PinTypes.GPIO,
            special_func=None
        )
    ])

    @staticmethod
    def inner_row():
        return Row(row_name=RowNames.INNER, pins=[
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=0),
            id=None,
            pin_type=PinTypes.POWER_3V3,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=1),
            id=2,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=2),
            id=3,
            pin_type=PinTypes.GND,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=3),
            id=4,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GCLK"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=4),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=5),
            id=17,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_0"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=6),
            id=27,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN2"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=7),
            id=22,
            pin_type=PinTypes.GPIO,
            special_func="GPIO_GEN_3"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=8),
            id=None,
            pin_type=PinTypes.POWER_3V3,
            special_func="3V3"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=9),
            id=10,
            pin_type=PinTypes.GPIO,
            special_func="SPI_MOSI"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=10),
            id=9,
            pin_type=PinTypes.GPIO,
            special_func="SPI_MISO"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=11),
            id=11,
            pin_type=PinTypes.GPIO,
            special_func="SPI_CLK"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=12),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=13),
            id=0,
            pin_type=PinTypes.EEPROM,
            special_func="I2C EEPROM ID_SD"
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=14),
            id=5,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=15),
            id=6,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=16),
            id=13,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=17),
            id=19,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=18),
            id=26,
            pin_type=PinTypes.GPIO,
            special_func=None
        ),
        Pin(
            coords=PinCoords(row_name=RowNames.INNER, pin_pair_num=19),
            id=None,
            pin_type=PinTypes.GND,
            special_func="GND"
        )
    ])

def print_pins():
    rpi_pins = RPi3Pins()
    
    longwise_pins = zip(rpi_pins.inner_row().pins, rpi_pins.outer_row().pins)
    
    print(' Power light ^^ ')
    
    def pin_as_string(pin):
        pin_id = str(pin.id)
        special_func = ']\t\t\t'
        if pin.special_func is not None:
            special_func = '(' + pin.special_func + ')]\t\t'
        
        return '[' + pin_id + ': ' + pin.pin_type + special_func
    
    for echelon in longwise_pins:
        print(echelon[0].coords.pin_pair_num, '\t',
              pin_as_string(echelon[0]),
              pin_as_string(echelon[1]))
    print()
    print(' USB Connectors ') 

if __name__ == '__main__':
    print_pins()
    