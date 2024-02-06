import re
from bs4 import BeautifulSoup, Tag
from app.process.preprocess.clean_string import clean_string

def _define_model(hymn_tag: Tag) -> None:
    # Variables
    head_tag = hymn_tag.head
    head_tag_content = clean_string(str(head_tag.string), ':')
    pattern = r"подобен:\s{1,3}.*:"

    # Process
    result = re.search(pattern, head_tag_content)
    string = result.group(0) if result else None

    # Output
    return string, head_tag.string

def define_models_in_hymns(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    hymns_tag = xml_markup.find_all("hymn")

    # Process
    for tag in hymns_tag:
        model = _define_model(tag)
        if model:
            print(model[0], model[1], '\n')

    # Output
    return xml_markup