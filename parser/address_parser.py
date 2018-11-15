import re

from parser.japanese_parser import zen2han
from parser.prefectures import PREFECTURES


class AddressParser:
    """Parse address into components"""
    postal_code = None
    prefecture = None
    city = None
    street_address = None
    house_number = None
    floor_number = None
    unit_number = None

    def __init__(self, input_address):
        """Take input address"""
        self.input_address = input_address
        self.parse()

    def parse(self):
        """Deconstruct Japanese address"""
        value = self.input_address

        # Strip all whitespaces
        value = re.sub(r"\s", "", value)

        # Converts all full-width digits to half-width
        full_width_match = re.findall(r"[０-９−ー]", value)
        for match in full_width_match:
            value = value.replace(match, zen2han(match))
        value = value.replace("−", "-")

        # Get postal code and strip
        post_code_match = re.search(r"\d{3}-?\d{4}", value)
        if post_code_match:
            self.postal_code = post_code_match.group(0)
            value = value.replace(self.postal_code, "")

        # Get prefecture and strip
        def get_prefecture(x):
            for pref in PREFECTURES:
                re_match = re.search(r"{}".format(pref), x)
                if re_match:
                    return pref
            return None

        prefecture = get_prefecture(value)
        if prefecture:
            value = value.replace(prefecture, "")
            self.prefecture = prefecture

        # Get floor and strip
        floor_match = re.search(r"(\d+)\s?[階Ff]", value)
        if floor_match:
            self.floor_number = floor_match.group(1) + 'F'
            value = value.replace(floor_match.group(0), "").strip()

        # Get room number and strip
        unit_number_match = re.search(r"(\d+)(号室|号)?$", value)
        if unit_number_match:
            self.unit_number = unit_number_match.group(1) + "号"
            value = value.replace(unit_number_match.group(0), "").strip()

        # Get the city and strip
        city_match = re.search(r"(.+?[区市郡])(.+)", value)
        if city_match:
            city, remainder = city_match.groups()
            self.city = city
            value = remainder

        # Get house number
        house_number_match = re.search(r"[\d−-]+", value)
        if house_number_match:
            self.house_number = house_number_match.group(0)
            value = value.replace(self.house_number, "").strip()

        # Lastly, the remainder should be the district/street address
        self.street_address = value

        return self.get_output_components()

    def get_output_components(self):
        """Outputs cleaned address components into a dictionary"""
        return {
            "postal_code": self.postal_code,
            "prefecture": self.prefecture,
            "city": self.city,
            "street_address": self.street_address,
            "house_number": self.house_number,
            "floor_number": self.floor_number,
            "unit_number": self.unit_number,
        }

    def get_clean_address(self):
        """Concatenate ouput components into one string"""
        return " ".join(
            [x for x in self.get_output_components().values() if x is not None]
        )
