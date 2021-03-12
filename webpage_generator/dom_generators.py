# Random HTML page generator
# Note: yield statements that yield an array are written to DSL file, 
# DSL equivalent of HTML elements will come after the element is generated in the code below.
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
    # (Multi-line strings are left aligned although they look weird in python 
    # because the output would include the tabbed space. sorry :( )
    yield f'''
<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        {bootstrap_css}
        <!-- Random Font -->'''
    # Generator calls can't be used inline with strings
    yield css_styles.RandomPageStyle()
    yield '''
        <title>RandomPage</title>
    </head>
    <body>
    '''
    # TODO: Change DSL defition for this?
    yield ['body{\n']
    # TODO: See if generated elements can be more reader friendly? 
    yield GenerateRandomSection()
    yield ['}']
    yield f'''
    {bootstrap_js}
    </body>
</html>
'''

# Helper function since using lorem.words(randint(...)) can get a bit messy
def Lorem(num_of_words):
    return lorem.words(randint(1, num_of_words))

# Generate a Random Form 
def RandomForm():
    form_types = ["text", "radio", "checkbox", "date", "email", "file"]
    yield '<form>'
    yield ['form {\n']
    # Forms can have 0 - 15 elements
    for _ in range(randint(15)):
        yield f'<label>{Lorem(5)}</label><br>'
        field_type = form_types[randint(len(form_types))]
        if field_type == "date":
            yield f'<input type="{field_type}" value=""/><br>'
        else:
            yield f'<input type="{field_type}" value="{Lorem(5)}"/><br>'
        yield [f'{field_type},\n']
    yield '<input type="submit" value="Submit">'
    yield ['submit-btn,\n']
    yield '</form>'
    yield ['}\n']

# Generate a random table
def RandomTable():
    yield '<table class="table table-bordered container">'
    yield ['table{\n']
    rows = randint(1, 5)
    for _ in range(rows):
        yield RandomRow()
    yield '</table>'
    yield ['}\n']

# Generate a random row for table
def RandomRow():
    yield '<tr class="row">'
    cols = randint(3, 9)
    yield RandomCols(cols)
    yield '</tr>'

# Generate a random column for table
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
        yield lorem.words(randint(1, 10))
        yield '</td>'

# Generate a random header with 1-5 words
def RandomHeader():
    sizes = ['1', '2', '3', '4', '5']
    size = sizes[randint(len(sizes))]
    yield [f'heading-{size},\n']
    yield f'<h{size}>'
    yield Lorem(5)
    yield f'</h{size}>'

# Generate a random paragraph
def RandomParagraph():
    yield ['text,\n']
    yield '<p>'
    p = lorem.paragraph().split(" ")
    # =< 10% of the paragraph will have links
    num_of_links = (int) (0.10 * len(p))
    for _ in range(num_of_links):
        p[randint(len(p))] = f'<a href="#">{Lorem(5)}</a>'
    yield ' '.join(p)
    yield '</p>'

# TODO: clean up please.
def RandomNavBar():
    styles = [('navbar-light', 'bg-light'), ('navbar-dark', 'bg-dark')]
    style = styles[randint(len(styles))]
    yield f'<nav class="navbar navbar-expand-lg {styles[0]} {styles[1]}">'
    yield ['navbar {\n']
    yield f'<a class="navbar-brand" href="#">{Lorem(3)}</a>'
    yield ['logo,\n']
    yield '<div class="collapse navbar-collapse" id="navbarSupportedContent">'
    yield '<ul class="navbar-nav mr-auto">'
    # TODO: Include style for active link, currently not all fonts show the link as active
    yield '<li class="nav-item">'
    yield f'<a class="nav-link" href="#">{Lorem(3)}</a>'
    yield ['link,\n']
    yield '</li>'
    for _ in range(randint(1,5)):
        yield '<li class="nav-item">'
        yield ['link,\n']
        yield f'<a class="nav-link" href="#">{lorem.words(randint(1,3))}</a>'
        yield '</li>'
    # 50% chance a drop down menu will occur
    if randint(0,1) == 0:
        yield '<li class="nav-item dropdown">'
        yield f'<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown">{Lorem(3)}</a>'
        yield ['dropdown {\n']
        yield '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
        # TODO: These items aren't visible until interacted with, need some way for model to know this
        for _ in range(randint(1,5)):
            yield f'<a class="dropdown-item" href="#">{Lorem(2)}</a>'
        yield '</li>'
        yield ['}\n']
    yield '</ul>'
    yield '<form class="form-inline my-2 my-lg-0">'
    yield '<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">'
    yield ['search,\n']
    yield f'<button class="btn btn-outline-success my-2 my-sm-0" type="submit">{Lorem(2)}</button>'
    yield ['btn\n']
    yield '</form>'
    yield '</div>'
    yield '</nav>'
    yield ['}\n']

# Define generator functions above this list of functions
RANDOM_SECTIONS = [
    RandomForm,
    RandomTable,
    RandomHeader,
    RandomParagraph,
    RandomNavBar
]
NUM_OF_SECTIONS = len(RANDOM_SECTIONS)

def GenerateRandomSection():
    # Random alignment
    # TODO: See if possible to nest generator calls
    yield css_styles.RandomAlign(RANDOM_SECTIONS[randint(NUM_OF_SECTIONS)])
    if randint(10) <= 8:
        # 80% chance a new section will be added
        yield GenerateRandomSection()