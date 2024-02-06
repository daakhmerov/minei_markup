def clean_string(string: str, *chars) -> str:
    string = "".join(
        [char for char in string.lower().strip() if char.isalpha() or char in [" ", *chars]]
    )
    return string
