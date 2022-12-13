#TODO AddressValidationGMaps.validate_address

from os import environ

from requests import get, post
from dotenv import load_dotenv


def get_data_json_from_gmaps_api(origin_address: str, destination_address: str) -> dict:
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    load_dotenv()
    API_KEY = environ.get("API_KEY")
    payload = {
        "destinations": destination_address,
        "origins": origin_address,
        "key": API_KEY,
    }
    response = get(url, payload)
    if response.ok:
        data = response.json()
        return data
    else:
        raise NotImplemented


def serialize_data_from_gmaps_api(
    origin_address_from_json: str, destination_address_from_json: str
):
    data = get_data_json_from_gmaps_api(
        origin_address=origin_address_from_json,
        destination_address=destination_address_from_json,
    )
    destination_addresses = data.get("destination_addresses")[0]
    origin_addresses = data.get("origin_addresses")[0]
    distance_in_m = data.get("rows")[0]["elements"][0]["distance"]["value"]
    duration = data.get("rows")[0]["elements"][0]["duration"]["text"]
    return {
        "destination_addresses": destination_addresses,
        "origin_addresses": origin_addresses,
        "distance_in_m": distance_in_m,
        "duration": duration,
    }


class AddressValidationGMaps:

    @staticmethod
    # def validate_address(origin_address, destination_address):
    def validate_address():
        url = "https://addressvalidation.googleapis.com/v1:validateAddress"
        load_dotenv()
        api_key = environ.get('ADDRESS_VALID_API_KEY')
        payload = {
            'address': {
                'revision': 0,
                'regionCode': 'PL',
                'locality': 'Mountain View',
                'addressLines': ['1600 Amphitheatre Pkwy']
                # 'addressLines': [origin_address, destination_address]
            },
            'previousResponseId':'',
            'enableUspsCass': True,
        }

        example_payload = {
          "address": {
            "regionCode": "US",
            "locality": "Mountain View",
            "administrativeArea": "CA",
            "postalCode": "94043",
            "addressLines": ["1600 Amphitheatre Pkwy"],
          },
          "enableUspsCass": False
        }

        parameters = {
            'key': api_key,

        }
        response = post(url, json=example_payload, data=parameters)
        print(response)
        if response.ok:
            data = response.json()
            print(data)
        else:
            print(response.json())


AddressValidationGMaps.validate_address()

