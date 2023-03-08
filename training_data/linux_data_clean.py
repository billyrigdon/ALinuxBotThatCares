import re

input_file = "training_data.txt"
output_file = "training_data_cleaned.txt"

with open(input_file, "r") as file:
    text = file.read()

# Remove blank lines
text = re.sub(r'\n\s*\n', '\n', text)

# Remove trailing spaces at the beginning and end of lines
text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)

# Remove multiple spaces between words
text = re.sub(r' +', ' ', text)

# Write cleaned text to output file
with open(output_file, "w") as file:
    file.write(text)