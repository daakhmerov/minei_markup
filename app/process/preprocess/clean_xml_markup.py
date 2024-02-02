from bs4 import BeautifulSoup
from bs4.dammit import EntitySubstitution


def _xml_formatter(str: str) -> EntitySubstitution:
    """Функция _xml_formatter служит для создания собственного форматтера, который форматирует содержимое тегов: убирает пробелы и табуляцию в начале и в конце строки, а также заменяет переносы строки на пробелы.
    """    
    return EntitySubstitution.substitute_xml(str.strip().replace("\n", " "))

def clean_xml_markup(xml_markup: BeautifulSoup) -> BeautifulSoup:
    """Функция clean_xml_markup убирает пробелы и табуляцию в начале и в конце строк, обернутых в XML-теги, а также заменяет переносы строки на пробелы. 

    Args:
        xml_markup (BeautifulSoup): Экземпляр класса BeautifulSoup, в котором представлены данные об XML-разметке данного текста

    Returns:
        BeautifulSoup: Экземпляр класса BeautifulSoup, репрезентирующий структуру данных XML-документа
    """    
    processed_xml_markup = xml_markup.prettify(formatter=_xml_formatter)
    return BeautifulSoup(processed_xml_markup, 'lxml-xml')