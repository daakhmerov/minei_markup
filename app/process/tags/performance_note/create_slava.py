from .... import find_by_pattern, clean_string
from bs4 import BeautifulSoup

def make_tree_for_slava_genre(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    performance_note_tags = xml_markup.find_all("performance_note")

    # Process
    for tag in performance_note_tags:
        tag_content = clean_string(tag.string, ingore_digits=False)

        if find_by_pattern(r"богородичен", tag_content, method="search"):
            tag.wrap(xml_markup.new_tag("head"))
            head_parent_tag = tag.find_parent("head")
            head_parent_tag.wrap(xml_markup.new_tag("hymn", attrs={"type": "hymnography", "genre": "славословие малое"}))

    # Output
    return xml_markup