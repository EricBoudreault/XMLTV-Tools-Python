# Developped by eboudreault@gmail.com
# 2024-08
import argparse
import os
import re

# Validate the M3U8 file format according to specified rules
def validate_m3u8_file(filename):
    
    # Initialize the list of warnings
    warnings = []
    
    # Read the lines from the file
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize a counter for #EXTINF lines
    extinf_count = 0

    # Process each line in the file
    for i, line in enumerate(lines, 1):
        
        # Skip lines starting with #EXTREM:
        if line.startswith('#EXTREM:'):
            continue

        # Process lines starting with #EXTINF:
        if line.startswith('#EXTINF:'):
            extinf_count += 1
            
            # Check that there are no consecutive lines starting with the '#EXTINF' tag
            if extinf_count > 1:
                warnings.append(f"From line {i}, there is more than one line starting with the '#EXTINF' tag.")
            
            # Check for the presence of mandatory attributes
            if not all(keyword in line for keyword in 'tvg-id="'):
                warnings.append(f"Line {i}: 'tvg-id' attribute is missing.")
            if not all(keyword in line for keyword in 'tvg-logo="http'):
                warnings.append(f"Line {i}: 'tvg-logo' attribute is missing.")
            if not all(keyword in line for keyword in 'group-name="'):
                warnings.append(f"Line {i}: 'group-name' attribute is missing.")
            
            # Check for the presence of 'group-title'
            if 'group-title=' in line:
                warnings.append(f"Line {i}: Unauthorized presence of the 'group-title' attribute.")
            
            # Check that there is a value between quotes for attributes 'tvg-id', 'tvg-logo' and 'group-name'
            if not re.search(r'tvg-id="[^"]+"', line):
                warnings.append(f"Line {i}: No channel identifier for the 'tvg-id' attribute.")
            if not re.search(r'tvg-logo="http[^"]+"', line):
                warnings.append(f"Line {i}: No logo address for the 'tvg-logo' attribute.")
            if not re.search(r'group-name="[^"]+"', line):
                warnings.append(f"Line {i}: No group name for the 'group-name' attribute.")
            
            # Check that there is a TV channel title
            if ',' not in line or line.strip().endswith(','):
                warnings.append(f"Line {i}: No TV channel title.")
            else:
                # Check that there is no space between the last comma and the following text
                text_after_comma = line.split(',', 1)[1]
                if text_after_comma.startswith(' '):
                    warnings.append(f"Line {i}: A space preceding the TV channel title.")
        else:
            # Reset the #EXTINF line counter if another line is encountered
            extinf_count = 0
    
    # Write the warnings
    script_name = os.path.basename(__file__)

    with open(f'{script_name}-err.txt', 'w', encoding='utf-8') as warning_file:
        for error in warnings:
            warning_file.write(error + '\n')

# Entry Point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate M3U8 file format.")
    parser.add_argument('filename', type=str, help="The M3U8 file to validate")
    args = parser.parse_args()
    
    # Validate the file
    validate_m3u8_file(args.filename)
