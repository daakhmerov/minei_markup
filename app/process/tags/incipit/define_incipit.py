from bs4 import BeautifulSoup

def define_incipit(xml_markup: BeautifulSoup) -> BeautifulSoup:
    # Variables
    model_tags = xml_markup.find_all("model")
    # Process
    for tag in model_tags:
        # Variables
        tag_content_parsed = tag.string.split(":")
        tag_similar = tag_content_parsed[0]
        tag_incipit = tag_content_parsed[1]

        # Process
        tag.string = ""
        tag.insert(0, tag_similar + ":")
        tag.insert(-1, xml_markup.new_tag("incipit"))
        tag.incipit.string = tag_incipit + ":"

        tag.find_parent("hymn").attrs["model"] = tag_incipit

    # Output
    return xml_markup