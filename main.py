from typing import NoReturn

from google_maps_api import serialize_data_from_gmaps_api
from userdata import get_destination_and_origin, get_car_name


def app() -> NoReturn:
    payload = get_destination_and_origin()
    car = get_car_name()
    data = serialize_data_from_gmaps_api(
        destination_address_from_json=payload.get("destination_adres"),
        origin_address_from_json=payload.get("origin_adres"),
    )

    print(
        f"""
    Statistics:
    Car: {car.title()}
    Start: {data.get('origin_addresses')}
    End: {data.get('destination_addresses')}
    Duration: {data.get('duration')}
    Length: {data.get('distance_in_m')/1000} km.
    """
    )


if __name__ == "__main__":
    app()
