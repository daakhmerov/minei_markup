from app.input.input import open_xml_file
from app.output.output import write_xml_file
from app.process.preprocess.clean_xml_markup import clean_xml_markup
from app.process.preprocess.clean_string import clean_string
from app.process.tags.hymn.correct_performance_notes_tags import (
    correct_performance_notes_tags,
)
from app.process.genres.define_genre import define_genre_in_hymn_tags
from app.process.genres.define_model import define_models_in_hymns
from app.utils.read_json import genres


name = "mineiMarkup"
__version__ = "0.1.0"
