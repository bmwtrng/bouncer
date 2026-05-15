# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(
    name,
    date_of_birth,
    place_of_birth,
    height,
    nationality
):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }

    return passport


# Example
print(create_passport(
    "John Doe",
    "2002-12-31",
    "Amsterdam",
    1.82,
    "Dutch"
))
def create_passport(
    name,
    date_of_birth,
    place_of_birth,
    height,
    nationality
):
    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }


def add_stamp(passport, country):

    # Create stamps list if it does not exist yet
    if "stamps" not in passport:
        passport["stamps"] = []

    # Add country only if:
    # - it is not already in stamps
    # - it is not the home country
    if (
        country not in passport["stamps"]
        and country != passport["nationality"]
    ):
        passport["stamps"].append(country)

    return passport


# Example
passport = create_passport(
    "John Doe",
    "2002-12-31",
    "Amsterdam",
    1.82,
    "Netherlands"
)

print(add_stamp(passport, "Spain"))
print(add_stamp(passport, "France"))
print(add_stamp(passport, "Spain"))       # duplicate, won't be added
print(add_stamp(passport, "Netherlands")) # home country, won't be added
def add_biometric_data(passport, name, value, date):

    # Create biometric dictionary if it does not exist yet
    if "biometric" not in passport:
        passport["biometric"] = {}

    # Create biometric data dictionary
    biometric_data = {
        "date": date,
        "value": value
    }

    # Add or update biometric data
    passport["biometric"][name] = biometric_data

    return passport


# Example
passport = {
    "name": "John Doe",
    "nationality": "Dutch"
}

print(add_biometric_data(
    passport,
    "fingerprint",
    "ABC123XYZ",
    "2026-05-15"
))

print(add_biometric_data(
    passport,
    "eye_color",
    "blue",
    "2026-05-16"
))
