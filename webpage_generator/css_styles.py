from numpy.random import randint

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

# Pick a random font for page
def RandomFont():
    font = FONT_LIST[randint(len(FONT_LIST))]
    yield f'<link rel="stylesheet" href="https://fonts.googleapis.com/css?family={font.replace(" ", "+")}">'
    yield '<style>body{font-family: "' + font + '", serif;}</style>'

# Pick a random font for an element
def RandomFontInline(element):
    font = FONT_LIST[randint(len(FONT_LIST))]
    yield f'<div style="font-family: \'{font}\', serif;">'
    yield element()
    yield '</div>'
