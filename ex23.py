# Encoding
# Requires your terminal to output utf-8
import sys
script, input_encoding, error = sys.argv

# Main func to loop through language lines
def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        
# Print the byte string then the decoded character
def print_line(line, encoding, errors):
    next_lang = line.strip()
    # DBES = Decode Bytes Encode Strings
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<==>", cooked_string)
    
# Read the file
languages = open("languages.txt", encoding="utf-8")

# Start reading the lines
main(languages, input_encoding, error)