from app import (
    open_xml_file,
    clean_xml_markup,
    write_xml_file,
    correct_performance_notes_tags,
    define_genre_in_hymn_tags,
    define_models_in_hymns,
)

input_path = "input.xml"
output_path = "output.xml"


def main():
    # Input
    xml_file = clean_xml_markup(open_xml_file(input_path))

    # Process
    correct_performance_notes_tags(xml_file)
    processed_xml_markup = define_models_in_hymns(xml_file)
    define_genre_in_hymn_tags(xml_file)
    
    # Output
    write_xml_file(output_path, processed_xml_markup)


if __name__ == "__main__":
    main()
