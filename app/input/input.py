from bs4 import BeautifulSoup


def open_xml_file(path_to_xml: str) -> BeautifulSoup:
    """Функция 'open_xml_file' открывает файл с размеченным текстом в формате .xml и преобразует его в экземпляр класса BeautifulSoup для дальнейшей работы

    Args:
        path_to_xml (str): Путь к файлу с размеченным текстом в формате .xml

    Returns:
        BeautifulSoup: Экземпляр класса BeautifulSoup, репрезентирующий структуру данных XML-документа
    """
    with open(path_to_xml, "r", encoding="utf-8") as file:
        xml_markup = BeautifulSoup(file.read(), "lxml-xml")
        return xml_markup
