import re
from bs4 import BeautifulSoup
from .... import clean_string

def markup_p_tags(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    hymn_tags = xml_markup.find_all("hymn", attrs={"genre": "песнь"})
    p_tags = [p_tag for tag in hymn_tags for p_tag in tag if p_tag.name == "p"]

    # Process
    for tag in enumerate(p_tags):
        tag_content = clean_string(tag[1].string, ":")
        tag_attrs = tag[1].attrs


        if tag_attrs == {}:
            tag_attrs["class"] = "строфа"
            tag_attrs["name"] = "богородичен" if re.match(r"богородичен\s*:", tag_content) else "тропарь"
            tag_attrs["number"] = ""

    # Output
    return xml_markup

def set_number_to_p(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    song_elements = xml_markup.find_all("hymn", attrs={"genre": "песнь"})

    # Input
    for song in song_elements:
        number = 2
        for p in song:
            if p.name == "p" and p.attrs["number"] != 1:
                p.attrs["number"] = number
                number += 1

    # Output
    return xml_markup