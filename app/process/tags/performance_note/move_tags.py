from bs4 import BeautifulSoup
from .... import clean_string, _move_tag_content, _remove_tag, find_by_pattern


def move_performance_note_tags(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    performance_note_tags = xml_markup.find_all("performance_note")

    # Process
    for tag in performance_note_tags:
        tag_content = tag.string
        processed_tag_content = clean_string(str(tag_content), ":", ingore_digits=False)

        if find_by_pattern(r"песнь\s+\d", processed_tag_content):
            _move_tag_content(xml_markup, tag, "down")
            _remove_tag(tag)
        elif find_by_pattern(r"богородичен:", processed_tag_content):
            _move_tag_content(xml_markup, tag, "up", "hymn", -1)
            _remove_tag(tag)
        elif find_by_pattern(r"стих\w+", processed_tag_content, method="search"):
            _move_tag_content(xml_markup, tag, "down")
            _remove_tag(tag)

    # Outputs
    return xml_markup
