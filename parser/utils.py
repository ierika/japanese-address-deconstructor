import re

from parser.prefectures import PREFECTURES


def deconstruct_jp_address(value: str) -> dict:
    """Deconstruct Japanese address"""
    result = {"input_address": value}

    # Get postal code and strip
    post_code_match = re.match(r"\d{3}-?\d{4}", value)
    if post_code_match:
        result["postal_code"] = post_code_match.group(0)
        value = value.replace(result["postal_code"], "")
    else:
        result["postal_code"] = None

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
        result["prefecture"] = prefecture
    else:
        result["prefecture"] = None

    # Get floor and strip
    floor_match = re.match(r".*((\d+)\s?[階Ff]).*", value)
    if floor_match:
        result["floor_number"] = floor_match.group(2) + 'F'
        value = value.replace(floor_match.group(1), "").strip()
    else:
        result["floor_number"] = None

    # Get the city and strip
    match = re.match(r'(.+?[区市郡])(.+)', value)
    if match:
        city, address = match.groups()
        result["city"] = city
        result["street_address"] = address
    else:
        result["city"] = None
        result["street_address"] = None

    return result


def hyphenate_jp_postal_code(value: str) -> str:
    """Hyphenates Japanese postal code"""
    # Check if it is a 6 or 7 digit postal code first
    re_match = re.match(r"(\d{2,3})(\d{4})", value)
    if re_match:
        return "-".join(re_match.groups())
    else:
        return value


def has_japanese_letter(value):
    """Detects if string has a Japanese character"""
    pattern = re.compile(r'.*[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-'
                         r'\ufaff\uff66-\uff9f].*')
    return True if pattern.match(value) else False
