# Helper functions for styling
from numpy.random import randint

def RandomAlign(element):
    alignments = ['center', 'justify', 'right', 'left']
    yield f'<div style="text-align: {alignments[randint(len(alignments))]};">'
    yield element()
    yield '</div>'

# Font list from fonts.google.com
# Add font names to list below to include them in generated DOM
FONT_LIST = [
    "Akaya Telivigala",
    "DotGothic16",
    "Lato",
    "Roboto Mono",
    "Stick",
    "Pacifico",
    "Indie Flower",
    "Amatic SC"
]
COLORS = [
    'AliceBlue',
    'Aqua',
    'Charteuse',
    'White',
    'Coral',
    'DarkCyan',
    'DarkSeaGreen']

# Pick a random font for page
def RandomPageStyle():
    font = FONT_LIST[randint(len(FONT_LIST))]
    color = COLORS[randint(len(COLORS))]
    yield f'<link rel="stylesheet" href="https://fonts.googleapis.com/css?family={font.replace(" ", "+")}">'
    yield '<style>body{font-family: "' + font + '", serif;' + 'background-color: ' + color + ';}</style>'
