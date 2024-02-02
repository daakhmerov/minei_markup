from app import open_xml_file, clean_xml_markup, write_xml_file, correct_performance_notes_tags

input_path = 'input.xml'
output_path = 'output.xml'

def main():
    xml_file = open_xml_file(input_path)
    processed_xml_markup = correct_performance_notes_tags(clean_xml_markup(xml_file))
    write_xml_file(output_path, processed_xml_markup)

if __name__ == '__main__':
    main()