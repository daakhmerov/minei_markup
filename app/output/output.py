from bs4 import BeautifulSoup


def write_xml_file(path_to_processed_xml: str, xml_markup: BeautifulSoup) -> None:
    """Функция write_xml_file создает файл по указанному пути и записывает в него xml-разметку

    Args:
        path_to_processed_xml (str): Путь файла, в который будет записана .xml-разметка
        xml_markup (BeautifulSoup): Экземпляр класса BeautifulSoup, который представляет XML-разметку документа
    """
    with open(path_to_processed_xml, "w", encoding="utf-8") as file:
        file.write(xml_markup.prettify())
