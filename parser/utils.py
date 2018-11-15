import re


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
