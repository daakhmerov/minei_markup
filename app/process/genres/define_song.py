from bs4 import BeautifulSoup
from ... import clean_string, find_by_pattern, _remove_tag

def define_songs(xml_markup: BeautifulSoup) -> BeautifulSoup:
    """Функция определяет жанр и номер песни. Также меняет теги на нормальные

    Args:
        xml_markup (BeautifulSoup): _description_

    Returns:
        BeautifulSoup: _description_
    """
    # Variables
    edited_tags = xml_markup.find_all("edited")

    # Process
    for tag in edited_tags:
        tag_content = clean_string(tag.string, ingore_digits=False)
        if find_by_pattern(r"песнь\s+\d", tag_content):
            # Variables
            tag_content_parsed = tag_content.split(" ")
            genre = tag_content_parsed[0]
            number = tag_content_parsed[-1]

            # Process
            parent_hymn_tag = tag.find_parent("hymn")
            parent_hymn_tag["genre"] = genre
            parent_hymn_tag["number"] = number
            _remove_tag(tag)
        elif find_by_pattern(r"стих\w+", tag_content, method="search"):
            sibling_head_tag = tag.find_next_sibling("head")
            sibling_head_tag.insert(0, tag.string)

            parent_hymn_tag = tag.find_parent("hymn")
            parent_hymn_tag["genre"] = "стихира"
            _remove_tag(tag)

        else:
            tag.name = "p"

    return xml_markup

def define_irmos(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    hymn_tags = xml_markup.find_all("hymn", attrs={"genre": "песнь"})

    # process head-tags
    for tag in hymn_tags:
        # Head
        if tag.head:
            head_tag = tag.head
            head_tag_content = clean_string(head_tag.string, ":")
            if find_by_pattern(r"ирмос\s*:", head_tag_content):
                head_tag.name = "p"
                head_tag.attrs["class"] = "строфа"
                head_tag.attrs["name"] = "ирмос"
                head_tag.attrs["number"] = 1

    # Output
    return xml_markup