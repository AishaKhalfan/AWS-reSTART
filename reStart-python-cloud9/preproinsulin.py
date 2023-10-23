import re
'''
script = """
ORIGIN      
1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
"""
pattern = r'ORIGIN\s*\d+\s*|//|\s+|\n|\r'
cleaned_script = re.sub(pattern, '', script)
print(cleaned_script)

cut -c 1-24 preproinsulin-seq-clean.txt > lsininsulin-seq-clean.txt
'''
# Read the contents of the input file
with open('preproinsulin-seq.txt', 'r') as file:
    data = file.read()

# Define a regular expression pattern to match and replace the undesired content
pattern = r'ORIGIN|\d+|//|\s+'
cleaned_data = re.sub(pattern, '', data)

# Save the cleaned data to a new file or overwrite the original file
with open('cleaned_preproinsulin-seq.txt', 'w') as output_file:
    output_file.write(cleaned_data)

print("Data has been cleaned and saved to cleaned_preproinsulin-seq.txt.")
