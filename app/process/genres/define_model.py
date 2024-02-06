import re
from bs4 import BeautifulSoup, Tag
from app.process.preprocess.clean_string import clean_string

def _tag_model_inside_head_tag(hymn_tag: Tag, model_string: str) -> None:
    # Variables
    head_tag = hymn_tag.head
    model_tag_markup = f'<model>{model_string}</model>'

    # Process
    head_tag_markup = str(head_tag).replace(model_string, model_tag_markup)

    # Create new tag and delete outdated
    updated_head_tag = BeautifulSoup(head_tag_markup, 'lxml-xml').head
    
    # Add new tag and delete old
    head_tag.decompose()
    hymn_tag.insert(1, updated_head_tag)
    

def _define_model(hymn_tag: Tag) -> None:
    # Variables
    head_tag = hymn_tag.head
    head_tag_content = head_tag.string.split(".")
    pattern = r"подобен:\s{1,3}.*:"

    # Process
    result = [
        substring
        for substring in head_tag_content
        if re.search(pattern, clean_string(substring, ":"))
    ]
    string = result[0] if result else None

    # Output
    return string


def define_models_in_hymns(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    hymns_tag = xml_markup.find_all("hymn")

    # Process
    for tag in hymns_tag:
        model = _define_model(tag)
        if model:
            _tag_model_inside_head_tag(tag, model)

    # Output
    return xml_markup
