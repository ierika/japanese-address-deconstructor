from parser.address_parser import AddressParser


if __name__ == "__main__":
    deconstructed = AddressParser(
        "227-0042 神奈川県川崎市麻生区上麻生１−３４−５ 川崎西合同庁舎 １２３号室"
    )
    print(deconstructed.parse())
    print(deconstructed.get_clean_address())
