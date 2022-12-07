#TODO env
#TODO coordinates
#TODO validator
#TODO case when user not specify car name

from sys import argv


def get_car_name() -> str:
    if len(argv) > 1:
        car = str(argv[1]).lower()
        return car
    else:
        return "Default"
