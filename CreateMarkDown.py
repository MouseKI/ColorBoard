import re

# Define your variables
variables = {
    "{{title}}": "Color Set Collections",
    "{{description}}": "Here are some of my favourite colour set collections. Hope you like it.",
    "{{color1}}": "#0392cf"
}

# Read the Markdown file
with open('README.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# Replace variables in the Markdown content
for key, value in variables.items():
    markdown_content = re.sub(re.escape(key), value, markdown_content)

# Write the processed Markdown to an output file
with open('PROCESSED_README.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print("Processed Markdown written to PROCESSED_README.md")
