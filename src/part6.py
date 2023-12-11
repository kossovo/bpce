import requests

API_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
API_URL = "https://demo.nautobot.com/api"


def get_address_lit() -> list:
    """Return the Nautobot API address lit"""

    return requests.get(
        f"{API_URL}/dcim/sites/",
        headers={"Authorization": f"Token {API_TOKEN}"},
        timeout=5,
    ).json()["results"]


def get_sites() -> list:
    """Return the Nautobot API sites"""

    return requests.get(
        f"{API_URL}/dcim/locations/",
        headers={"Authorization": f"Token {API_TOKEN}"},
        timeout=5,
    ).json()["results"]


def get_interfaces(device: str = None) -> list:
    """get the interfaces"""

    interfaces = requests.get(
        f"{API_URL}/dcim/interfaces/",
        headers={"Authorization": f"Token {API_TOKEN}"},
        timeout=5,
    ).json()["results"]

    result = []
    for interface in interfaces:
        if interface["device"]["name"] == device:
            result.append(interface)

    return result
