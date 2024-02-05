def clean_string(string:str) -> str:
    string = "".join(
        [char for char in string.strip() if char.isalpha() or char == " "])
    return string