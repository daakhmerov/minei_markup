# Задачи:
# Определить жанры
# - Выделить model и incipit
# - В тегах p

from bs4 import BeautifulSoup, Tag
from Levenshtein import distance

from app.utils.read_json import genres
from app.process.preprocess.clean_string import clean_string


def _set_genre_to_hymn_tag(
    tokens: list, hymn_tag: Tag, genre: str, lev_distance: int = 2
) -> None:
    """Функция "_set_genre_to_hymn_tag" на основе расстояния Левенштейна между строкой, взятой из файла "genres.json", и токеном из списка "tokens" устанавливает значение атрибута "genre" тега "hymn".

    Args:
        tokens (list): Список токенов
        hymn_tag (Tag): Экземпляр класса "Tag", представляющий тег "hymn"
        genre (str): Название искомого жанра
        lev_distance (int, optional): значение расстояния Левенштейна. Всё, что больше значения метрики, игнорируется. По умолчанию — 2.
    """
    if genres.get(genre):
        keywords = genres.get(genre)

        for word, token in zip(keywords, tokens):
            if distance(word, token) <= lev_distance:
                hymn_tag["genre"] = genre

    else:
        for token in tokens:
            if distance(genre, token) <= lev_distance:
                hymn_tag["genre"] = genre


def _define_genre_in_hymn_tag(hymn_tag: Tag, genre: str) -> str | None:
    # "head_tag_content" — переменная, которая указывает на строку, заключенную в тег "head" элемента "hymn".
    head_tag_content = hymn_tag.head.string

    # Предобработка строки. На этом этапе удаляются служебные символы (диакритические знаки и проч. символы, которые не представляют буквы. Исключение — символы пробела.
    head_tag_content = clean_string(head_tag_content)

    # Разбиение строки на токены с помощью метода "split".
    tokens = [token for token in head_tag_content.split() if token != ""]

    # Вызов функции "_set_genre_to_hymn_tag", которая на основе расстояния Левенштейна между строкой, взятой из файла "genres.json", и токеном из списка "tokens" устанавливает значение аттрибута "genre" тега "head" элемента "hymn".
    _set_genre_to_hymn_tag(tokens, hymn_tag, genre)


def define_genre_in_hymn_tags(xml_markup: BeautifulSoup) -> BeautifulSoup:
    """Функция "define_genre_in_hymn_tags" делает парсинг строк элементов "head", вложенных в теги "hymn". Функция определяет упомянутого в строке жанра и устанавливает эту строку в качестве значения атрибута "genre" тега "hymn".

    Args:
        xml_markup (BeautifulSoup): Экземпляр класса BeautifulSoup, в котором представлены данные об XML-разметке данного текста.

    Returns:
        BeautifulSoup: Экземпляр класса BeautifulSoup, который представляет XML-разметку документа
    """
    # "hymns_tag" — переменная, указывающая на список, который состоит из всех элементов, закодированных тегом "hymn" в XML-разметке документа.
    hymns_tag = xml_markup.find_all("hymn")

    # Итерация по списку "hymns_tag", который состоит из элементов, обернутых в тег "hymn".
    for hymn_tag in hymns_tag:
        # Итерация по списку "genres". Файл "genres.json", который содержит названия жанров, декодируется в словарь "genres".
        for genre in genres.keys():
            _define_genre_in_hymn_tag(hymn_tag, genre)

    return xml_markup
