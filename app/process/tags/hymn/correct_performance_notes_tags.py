from bs4 import BeautifulSoup, Tag

def _merge_performance_note_head(tag:Tag) -> None:
        # "hymn_tag" — следующий за элементом "tag" тег "hymn".
        # "head" — дочерний тег "head" элемента "hymn".
        tag_content = tag.string
        hymn_tag = tag.find_next("hymn")
        head = hymn_tag.head

        # Вставка строки "tag_content" в элемент "head"
        head.insert(0, tag_content)

        # Удаление тега "performance_note", на который указывает переменная
        # "tag".
        tag.decompose()

        # Очистка строки, которая обернута в тег "head", от пробелов и 
        # переноса строк.
        cleaned_head_content = " ".join(
            [
                string.replace("\n", "")
                for string in head.text.split(" ")
                if string not in ["\n", ""]
            ]
        )

        # Замена содержимого тега "head" на очищенную строку
        head.string = cleaned_head_content

def correct_performance_notes_tags(xml_markup: BeautifulSoup) -> BeautifulSoup:
    """Функция "correct_performance_notes_tags" объединяет содержимое тегов "performance_note" и дочернего тега "head" элемента "hymn", следующего по порядку за элементом "performance_note" в XML-дереве.

    Args:
        xml_markup (BeautifulSoup): Экземпляр класса BeautifulSoup, в котором представлены данные об XML-разметке данного текста

    Returns:
        BeautifulSoup: Экземпляр класса BeautifulSoup, который представляет XML-разметку документа
    """    

    # Переменная "performance_note_tags", указывающая на список со всеми тегами
    # "performance_note".
    # Переменная "performance_note_tags_and_hymn" указывающая на список тегов
    # "performance_note", за которыми в дереве XML-элементов следуют теги
    # "hymn".

    performance_note_tags = xml_markup.find_all("performance_note")
    performance_note_tags_and_hymn = [
        tag for tag in performance_note_tags if tag.find_next().name == "hymn"
    ]

    for tag in performance_note_tags_and_hymn:
        # Итерация по списку "performance_note_tags_and_hymn". "tag_content" —
        # строка, обернутая в тег "performance_note".
        _merge_performance_note_head(tag)

    return xml_markup
