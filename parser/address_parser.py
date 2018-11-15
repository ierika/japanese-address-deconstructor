import re

from parser.japanese_parser import zen2han
from parser.prefectures import PREFECTURES


class AddressParser:
    """Parse address into components"""
    postal_code = None
    prefecture = None
    city = None
    street_address = None
    floor_number = None

    def __init__(self, input_address):
        """Take input address"""
        self.input_address = input_address
        self.parse()

    def parse(self):
        """Deconstruct Japanese address"""
        value = self.input_address

        # Converts all full-width digits to half-width
        full_width_match = re.findall(r"[０-９−ー]", value)
        for match in full_width_match:
            value = value.replace(match, zen2han(match))

        # Get postal code and strip
        post_code_match = re.match(r"\d{3}-?\d{4}", value)
        if post_code_match:
            self.postal_code = post_code_match.group(0)
            value = value.replace(self.postal_code, "")

        # Get prefecture and strip
        def get_prefecture(x):
            for pref in PREFECTURES:
                re_match = re.match(r".*{}.*".format(pref), x)
                if re_match:
                    return pref
            return None

        prefecture = get_prefecture(value)
        if prefecture:
            value = value.replace(prefecture, "")
            self.prefecture = prefecture

        # Get floor and strip
        floor_match = re.match(r".*((\d+)\s?[階Ff]).*", value)
        if floor_match:
            self.floor_number = floor_match.group(2) + 'F'
            value = value.replace(floor_match.group(1), "").strip()

        # Get the city and strip
        match = re.match(r"(.+?[区市郡])(.+)", value)
        if match:
            city, address = match.groups()
            self.city = city
            self.street_address = address

        return self.get_output_components()

    def get_output_components(self):
        """Outputs cleaned address components into a dictionary"""
        return {
            "postal_code": self.postal_code,
            "prefecture": self.prefecture,
            "city": self.city,
            "street_address": self.street_address,
            "floor_number": self.floor_number,
        }
