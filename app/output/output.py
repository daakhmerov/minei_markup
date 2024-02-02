from bs4 import BeautifulSoup


def write_xml_file(
    path_to_processed_xml: str, xml_markup: BeautifulSoup, formatter: None | str = None
) -> str:
    with open(path_to_processed_xml, "w", encoding='utf-8') as file:
        if formatter is not None:
            file.write(xml_markup.prettify(formatter=formatter))
        else:
            file.write(xml_markup.prettify())
