import re


def find_by_pattern(pattern: str, string: str, method: str = "match") -> str | None:
    if method == "search":
        result = re.search(pattern, string)
    else:
        result = re.match(pattern, string)

    return result.group(0) if result is not None else None
