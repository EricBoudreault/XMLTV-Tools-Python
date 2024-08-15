import sys
import os
import xml.dom.minidom

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

        folder = os.path.dirname(os.path.abspath(__file__))
        source = arguments[1]
        destination = arguments[2]

        with open(source, 'r', encoding="utf-8") as file:
            content_source = file.read()

        save_pretty_xml(content_source, destination)

        print("File formatted successfully!\n")

    except Exception as ex:
        print(f"Main Error: {ex}\n")

"""
    Entry Point
"""
if __name__ == "__main__":
    main()
