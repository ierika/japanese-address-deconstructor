from parser.utils import deconstruct_jp_address


if __name__ == "__main__":
    deconstructed = deconstruct_jp_address(
        "121-0064東京都足立区保木間4-46-2ぶらぶらビル3階"
    )
    print(deconstructed)
