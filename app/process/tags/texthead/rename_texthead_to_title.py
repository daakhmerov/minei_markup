from bs4 import BeautifulSoup

def rename_texthead_to_title(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    texthead_tag = xml_markup.texthead

    # Process
    texthead_tag.name = 'title'

    # Output
    return xml_markup