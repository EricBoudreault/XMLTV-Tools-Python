# Developped by eboudreault@gmail.com
# 2024-08
# coding: utf-8
import io
import sys
import os
import xml.dom.minidom

"""
    Get String between
"""
def between(expression, first_string, last_string, occurrence):
    try:
        final_string = ""

        if occurrence > 0:
            pos1 = 0
            pos2 = 0

            for x in range(occurrence):
                pos1 = expression.find(first_string, pos1) + len(first_string)

                if pos1 < len(first_string):
                    break

            if pos1 < len(first_string):
                final_string = ""
            else:
                pos2 = expression.find(last_string, pos1)
                final_string = expression[pos1:pos2]

                if len(final_string) <= 0:
                    final_string = ""

        return final_string

    except Exception as ex:
        return ""

"""
    Get Channel
"""
def get_channel(line):
    first = f"channel id=\""
    channel = between(line, first, "\"", 1)

    if len(channel) == 0:
        first = f"channel=\""
        channel = between(line, first, "\"", 1)

    return channel

"""
    Filter EPG
"""
def filter_epg(content, filter_string):
    new_content = io.StringIO()
    is_channel_in_line = False
    current_channel = ""
    lines = content.splitlines()

    for line in lines:
        if not is_channel_in_line:
            current_channel = get_channel(line)
            is_channel_in_line = len(current_channel) > 0 and current_channel.lower() in filter_string.lower()

        if is_channel_in_line:
            new_content.write(line + "\n")

            if "</channel>" in line or "</programme>" in line:
                is_channel_in_line = False

    return new_content.getvalue()

"""
    Save XML string to file with pretty formatting
"""
def save_pretty_xml(xml_string, file_name):
    try:
        # Parse the XML string
        xml_dom = xml.dom.minidom.parseString(xml_string)

        # Pretty print the XML with indentation
        pretty_xml_as_string = xml_dom.toprettyxml(indent="  ")

        # Remove unnecessary blank lines
        pretty_xml_as_string = "\n".join([line for line in pretty_xml_as_string.split("\n") if line.strip()])

        # Unescape XML &quot; and &apos;
        unescaped_xml = xml_string.replace('&quot;', '"')
        #unescaped_xml = unescaped_xml.replace('&apos;', "'")

        unescaped_xml = unescaped_xml.replace('/>', " />")

        # Write the pretty XML to the destination file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(unescaped_xml)

    except Exception as ex:
        print(f"save_pretty_xml Error: {ex}\n")

"""
    Main Function
"""
def main():
    try:
        arguments = sys.argv

        if len(arguments) == 4:
            source = arguments[1]
            filter = arguments[2]
            destination = arguments[3]

            print("Getting the content...")

            # Read content from source file
            with open(source, 'r', encoding='utf-8') as source_file:
                content_source = source_file.read()

            print("Filtering...")

            # Filter EPG content
            header_section = between(content_source, "", "<channel", 1)
            main_section = filter_epg(content_source, filter)

            if main_section.endswith("</tv>"):
                content_source = header_section + main_section
            else:
                content_source = header_section + main_section + "\n</tv>"

            # Save formatted XML
            save_pretty_xml(content_source, destination)

            print("EPG Guide filtered successfully!\n")
        else:
            print('Usage: python epg-filter.py "<source_file_path>" "<List of channels separated by |>" "<destination_file_path>"')
            print('       python epg-filter.py "input.xml" "cnn.us|bfmtv.fr|bbcnews.uk" "output.xml"\n')

    except Exception as ex:
        print(f"Main Error: {ex}\n")

"""
    Entry Point
"""
if __name__ == '__main__':
    main()
