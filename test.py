from parser.address_parser import AddressParser


if __name__ == "__main__":
    deconstructed = AddressParser(
        "神奈川県川崎市麻生区上麻生1-3-14 川崎西合同庁舎"
    )
    print(deconstructed.parse())
