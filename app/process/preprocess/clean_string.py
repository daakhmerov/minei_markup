def clean_string(string: str, *chars, ingore_digits: bool = True) -> str:
    if ingore_digits:
        string = "".join(
            [
                char
                for char in string.lower().strip()
                if char.isalpha() or char in [" ", *chars]
            ]
        )
    else:
        string = "".join(
            [
                char
                for char in string.lower().strip()
                if char.isalpha() or char.isdigit() or char in [" ", *chars]
            ]
        )
    return string
