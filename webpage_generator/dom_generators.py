# Random HTML page generator
import string
from lorem_text import lorem
import numpy as np
from numpy.random import randint
from random import choice
import css_styles

bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">'
bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>'

# Generate a random HTML page
def RandomHtml():
    yield '<!doctype html>'
    yield '<html lang="en">'
    yield SetupHeader()
    yield '<body>'
    yield RandomH1()
    yield RandomNavBar()
    yield RandomBody()
    yield bootstrap_js
    yield '</body>'
    yield '</html>'

# Set up standard HTML page header
def SetupHeader():
    yield '<head>'
    yield '<!-- Required meta tags -->'
    yield '<meta charset="utf-8">'
    yield '<meta name="viewport" content="width=device-width, initial-scale=1">'
    yield '<!-- Bootstrap CSS -->'
    yield bootstrap_css
    yield css_styles.RandomFont()
    yield '<title>Hello, world!</title>'
    yield '</head>'

# Generate random sections with tables or headers along with paragraphs
def RandomBody():
    yield RandomTableSection()
    for _ in range(randint(3)):
        yield RandomP()
    while randint(2) == 0:
        yield css_styles.RandomFontInline(RandomBody)

# Generate random navigation bar at the top of an HTML page
def RandomNavBar():
    yield '<nav class="navbar navbar-expand-lg navbar-dark bg-dark">'
    yield '<a class="navbar-brand" href="#">' + lorem.words(randint(1, 5)) +'</a>'
    yield '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText">'
    yield '<span class="navbar-toggler-icon"></span>'
    yield '</button>'
    yield '<div class="collapse navbar-collapse">'
    yield '<ul class="navbar-nav mr-auto">'
    for _ in range (randint(2,5)):
        yield '<li className="nav-item">'
        yield '<a className="nav-link" href="#">' + lorem.words(randint(1, 2)) + '</a>'
        yield '</li>'
    yield '</ul>'
    yield '</div>'
    yield '</nav>'

# Generate random header or table contents
def RandomTableSection():
    random_sections = [RandomH1, RandomTable]
    yield choice(random_sections)()

# Generate a randome table
def RandomTable():
    yield '<table class="table table-bordered container">'
    rows = randint(1, 5)
    for _ in range(rows):
        yield RandomRow()
    yield '</table>'

# Generate a random row for table
def RandomRow():
    yield '<tr class="row">'
    cols = randint(3, 9)
    yield RandomCols(cols)
    yield '</tr>'

# Generate a random column for the table
def RandomCols(cols):
    widths = np.random.random_sample(cols)
    # Bootstrap col widths always sum up to 12
    # Subtract cols from it since we're going to +1 after normalization
    factor = (12 - cols) / sum(widths)
    # Normalize numbers and +1 so we don't get widths of 0
    widths = [int(width * factor) + 1 for width in widths]
    # Need a fudge factor to fix rounding problems :)
    fudge = 12 - int(sum(widths))
    for _ in range(fudge):
        widths[randint(0, len(widths))] += 1
    # We have the widths that sum to 12, time to make them
    for width in widths:
        yield '<td class="col-{}">'.format(width)
        yield lorem.words(randint(10))
        yield '</td>'

# Generate a random header with 1-5 words
def RandomH1():
    yield '<h1>'
    yield lorem.words(randint(1,5))
    yield '</h1>'

# Generate a random paragraph
def RandomP():
    yield '<p>'
    yield lorem.paragraph()
    yield '</p>'
