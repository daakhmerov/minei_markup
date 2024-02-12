from app import (
    open_xml_file,
    write_xml_file,
    define_genre_in_hymn_tags,
    define_models_in_hymns,
    rename_texthead_to_title,
    UnsortedAttributes,
    move_performance_note_tags,
    define_incipit,
    define_songs,
    markup_p_tags,
    define_irmos,
    set_number_to_p,
    make_tree_for_slava_genre

)

input_path = "input.xml"
output_path = "output.xml"


def main():
    # Input
    xml_file = open_xml_file(input_path)

    # Process
    processed_xml_markup = move_performance_note_tags(xml_file)
    processed_xml_markup = rename_texthead_to_title(xml_file)
    processed_xml_markup = define_models_in_hymns(processed_xml_markup)
    processed_xml_markup = define_genre_in_hymn_tags(processed_xml_markup)
    processed_xml_markup = define_songs(processed_xml_markup)
    processed_xml_markup = markup_p_tags(processed_xml_markup)
    processed_xml_markup = define_irmos(processed_xml_markup)
    processed_xml_markup = set_number_to_p(processed_xml_markup)
    processed_xml_markup = define_incipit(processed_xml_markup)
    processed_xml_markup = make_tree_for_slava_genre(processed_xml_markup)
    
    # Output
    write_xml_file(output_path, processed_xml_markup, UnsortedAttributes())


if __name__ == "__main__":
    main()
