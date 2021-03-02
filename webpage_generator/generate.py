import sys
import os
import string
import numpy as np
from numpy.random import randint
from random import choice

bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">'
bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>'

def SetupHeader():
    yield '<head>'
    yield '<!-- Required meta tags -->'
    yield '<meta charset="utf-8">'
    yield '<meta name="viewport" content="width=device-width, initial-scale=1">'
    
    yield '<!-- Bootstrap CSS -->'
    yield bootstrap_css

    yield '<title>Hello, world!</title>'
    yield '</head>'

def RandomHtml():
    yield '<!doctype html>'
    yield '<html lang="en">'
    yield SetupHeader()
    yield '<body>'
    yield RandomBody()
    yield bootstrap_js
    yield '</body>'
    yield '</html>'

def RandomBody():
    yield RandomSection()
    if randint(2) == 0:
        yield RandomBody()

def RandomSection():
    random_sections = [RandomH1, RandomTable]
    yield choice(random_sections)()

def RandomTable():
    yield '<table class="table table-bordered container">'
    rows = randint(1, 5)
    for _ in range(rows):
        yield RandomRow()
    yield '</table>'

def RandomRow():
    yield '<tr class="row">'
    cols = randint(3, 9)
    yield RandomCols(cols)
    yield '</tr>'

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
        yield RandomWord()
        yield '</td>'


def RandomH1():
    yield '<h1>'
    yield RandomSentence()
    yield '</h1>'
    sentences = randint(5, 10)
    for _ in range(sentences):
         yield RandomSentence()

def RandomSentence():
    words = randint(5, 15)
    yield (' '.join(RandomWord() for _ in range(words)) + '.').capitalize()

def RandomWord():
    chars = randint(2, 10)
    return ''.join(choice(string.ascii_lowercase) for _ in range(chars))

def Output(generator):
    if isinstance(generator, str):
        print(generator)
        out.write(generator)

    else:
        for g in generator: Output(g)

with open(os.path.join(sys.path[0], 'index.html'), 'w') as out:
    Output(RandomHtml())