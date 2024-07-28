import os

variables = {
  "{{title}}": "Color Set Collections",
  "{{description}}": "Here are some of my favourite colour set collections. Hope you like it.",
  "{{color1}}": "#0392cf"
}

with open("README.md", "r") as file:
    content = file.read()

for key, value in variables.items():
    content = content.replace(key, value)

with open("README.md", "w") as file:
    file.write(content)
