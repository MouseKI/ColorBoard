#------------------------------------------------------------------------------------------------------------
# This python script is for creating Jupyter Notebook that display color board table markdown.
# Author: Runquanye
# Date: 2024 / 07
#------------------------------------------------------------------------------------------------------------

import nbformat as nbf

# Create a new notebook object
nb = nbf.v4.new_notebook()

# Define your variables
text = """\
# <center><span style="color:#0392cf">Color Set Collections</span></center>
Here are some of my favourite colour set collections. Hope you like it.
"""

# Add cells to the notebook
nb['cells'] = [
    nbf.v4.new_markdown_cell('# <center></span><span style="color:#0392cf">Color Set Collections</span></center>'),
    nbf.v4.new_markdown_cell('#### <b>Description:</b> Here are some of my favourite colour set collections. Hope you like it.\n\n---'),
]

color_set = {
    "four_color_collection" : {
        1 : ["#ff6453", "#ff8253", "#ffac53", "#ffe353"]
    },
    "five_color_collection" : {
        1 : ["#ee4035", "#f37736", "#fdf498", "#7bc043", "#0392cf"],
        2 : ["#7dde92", "#8bb879", "#e1de69", "#b6be6f", "#9aea6b"],
        3 : ["#47c68b", "#d39f74", "#abd14c", "#f1afaf", "#e7ef92"],
        4 : ["#d9ed92", "#b5e48c", "#99d98c", "#76c893", "#52b69a"],
        5 : ["#fffa85", "#fcd238", "#ff7f50", "#eb655b", "#58b849"],
        6 : ["#e7e47d", "#b69649", "#8edc62", "#5aaa31", "#479396"],
        7 : ["#ff4e50", "#f57758", "#eca061", "#e2c969", "#d8f271"],
        8 : ["#423f3f", "#336b8b", "#83984d", "#f0b51f", "#ea700b"],
        9 : ["#22d3ee", "#f87171", "#facc15", "#e879f9", "#4ade80"]
    },
    "six_color_collection" : {
        1 : ["#f9acdf", "#f7c98b", "#dbfb78", "#abf28c", "#90dcf2", "#e181ea"],
        2 : ["#f83361", "#fb4e01", "#e9f109", "#06ad40", "#0271bc", "#350450"],
        3 : ["#dfe801", "#f73560", "#008d26", "#0065bf", "#280439", "#fe4807"],
    },
    "other_color_collection" : {
        1 : ["#fe5e9d", "#f9662d", "#5e22a0", "#38a879", "#51cbf4", "#314cd2", "#f63933", "#1f2227"],
        2 : ["#bc908f", "#bc9690", "#e9ccd0", "#a89ea6", "#8c94c0", "#89a6a4", "#7767a7", "#829fcc", "#88a498", "#a99787", "#e88b93", "#99888e"]
    }
}

def createSpanTag(text, colorHEX, background):
    return f'<span style="color:{colorHEX}; background:{background};">{text}</span>'

# Load the Jupyter Notebook
with open('ColorBoard.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Function to replace variables in Markdown cells
def replace_variables_in_markdown(cell):
    if cell.cell_type == 'markdown':
        for key, value in variables.items():
            cell.source = cell.source.replace(key, value)
    return cell

# Apply the function to all cells
nb.cells = [replace_variables_in_markdown(cell) for cell in nb.cells]

# Save the modified notebook
with open('ColorBoard.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook has been modified and saved as 'ColorBoard.ipynb'")
