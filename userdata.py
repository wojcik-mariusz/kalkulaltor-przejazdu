# TODO env
# TODO coordinates
# TODO validator
# TODO case when user not specify car name

from sys import argv


def get_car_name() -> str:
    if len(argv) > 1:
        car = str(argv[1]).lower().strip()
        return car
    else:
        return "Default"


def get_destination_and_origin() -> dict:
    coordinates = {}
    if len(argv) > 3:
        coordinates["origin_adres"] = argv[2]
        coordinates["destination_adres"] = argv[3]
        return coordinates

    else:
        raise ValueError("Missed origin or destination coordinates")
