from app.input.input import open_xml_file
from app.output.output import write_xml_file
from app.process.preprocess.clean_string import clean_string
from app.process.genres.define_genre import define_genre_in_hymn_tags
from app.process.genres.define_model import define_models_in_hymns
from app.utils.read_json import genres
from app.process.tags.texthead.rename_texthead_to_title import rename_texthead_to_title
from app.process.tags.attrs_order.attrs_order import UnsortedAttributes
from app.utils.move_tag import _remove_tag, _move_tag_content
from app.utils.find_by_pattern import find_by_pattern
from app.process.tags.performance_note.move_tags import move_performance_note_tags
from app.process.tags.p.markup_p_tags import markup_p_tags
from app.process.tags.incipit.define_incipit import define_incipit
from app.process.tags.p.markup_p_tags import markup_p_tags, set_number_to_p
from app.process.genres.define_song import define_irmos, define_songs
from app.process.tags.performance_note.create_slava import make_tree_for_slava_genre

name = "mineiMarkup"
__version__ = "0.1.0"
