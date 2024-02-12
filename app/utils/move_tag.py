from bs4 import Tag, BeautifulSoup


# Удалить тег
def _remove_tag(tag: Tag):
    tag.decompose()


# Переместить содержимое тега в тег, который находится в дереве выше
def _move_tag_content(
    xml_markup: BeautifulSoup,
    tag: Tag,
    direction: str,
    find_tag: str | None = None,
    index: int = 0,
):
    # Variables
    tag_content = tag.string
    edited_tag = xml_markup.new_tag("edited")
    edited_tag.string = tag_content

    match (direction, find_tag):
        case ("down", None):
            sibling_tag = tag.find_next_sibling()
        case ("down", find_tag) if find_tag is not None:
            sibling_tag = tag.find_next_sibling(find_tag)
        case ("up", None):
            sibling_tag = tag.find_previous_sibling()
        case ("up", find_tag) if find_tag is not None:
            sibling_tag = tag.find_previous_sibling(find_tag)

    # Process
    sibling_tag.insert(index, edited_tag)
