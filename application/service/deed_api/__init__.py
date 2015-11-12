from . import implementation, interface


def make_deed_api_client():
    return interface.DeedApiInterface(implementation)
