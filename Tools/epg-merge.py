import sys
import os
import urllib.parse
from pathlib import Path

"""
    Get String between
"""
def between(expression, first_string, last_string):
    try:
        pos1 = expression.index(first_string) + len(first_string)
        pos2 = expression.index(last_string, pos1)
        final_string = expression[pos1:pos2]

        return final_string if final_string else ""

    except Exception:
        return ""

"""
    Main Function
"""
def main():
    try:
        arguments = sys.argv
        
        if len(arguments) == 4:
            source1 = arguments[1]
            source2 = arguments[2]
            destination = arguments[3]

            print("Getting the content...")

            # Get content of source files
            with open(source1, 'r', encoding='utf-8') as file:
                content1 = file.read()

            with open(source2, 'r', encoding='utf-8') as file:
                content2 = file.read()

            print("Getting the CHANNEL section...")

            # Get "Channel" sections of EPG guides
            channel_section1 = "  <channel id=" + between(content1, "<channel id=", "<programme")
            channel_section2 = "<channel id=" + between(content2, "<channel id=", "<programme")

            print("Getting the PROGRAMME section...")

            # Get "Programme" sections of EPG guides
            programme_section1 = "<programme" + between(content1, "<programme", "</tv>")
            programme_section2 = "<programme" + between(content2, "<programme", "</tv>")

            print("Building the new EPG Guide...")

            begin_section = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE tv SYSTEM "xmltv.dtd"><tv generator-info-name="">'
            end_section = "</tv>\r"

            # Join source files
            content = f"{begin_section}\r{channel_section1}{channel_section2}{programme_section1}{programme_section2}{end_section}"
            content = content.replace('\t', '  ')

            print("Saving the EPG Guide...")

            # Generate EPG file
            with open(destination, 'w', encoding='utf-8') as file:
                file.write(content)

            print("EPG Guides merged successfully!\n")

        else:
            print("Error: Missing argument!\n")

    except Exception as ex:
        print(f"Main Error: {ex}\n")

"""
    Entry Point
"""
if __name__ == "__main__":
    main()
