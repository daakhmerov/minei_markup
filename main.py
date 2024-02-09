from app import (
    open_xml_file,
    clean_xml_markup,
    write_xml_file,
    define_genre_in_hymn_tags,
    define_models_in_hymns,
    rename_texthead_to_title
)

input_path = "input.xml"
output_path = "output.xml"


def main():
    # Input
    xml_file = clean_xml_markup(open_xml_file(input_path))

    # Process
    processed_xml_markup = rename_texthead_to_title(xml_file)
    processed_xml_markup = define_models_in_hymns(processed_xml_markup)
    define_genre_in_hymn_tags(processed_xml_markup)
    
    # Output
    write_xml_file(output_path, processed_xml_markup)


if __name__ == "__main__":
    main()
