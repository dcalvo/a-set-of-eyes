import sys
import os
import dom_generators

# Write generator output to console, HTML, and DSL file 
def Output(generator, out, dsl):
    if isinstance(generator, str):
        # Write HTML contect to console and HTML file
        print(generator)
        out.write(generator)
    elif isinstance(generator, list):
        # Generators that yield a list should have one element and that element is written to the DSL file
        dsl.write(generator[0])
    else:
        for g in generator: Output(g, out, dsl)

def main():
    # HTML page and DSL .gui file is generated with the name 'index' by default. To change the name/path add it as a command line argument
    # Sample run:
    # py generate.py sample1
    fname = "index" if len(sys.argv) == 1 else sys.argv[1]
    with open(os.path.join(sys.path[0], f'{fname}.html'), 'w') as html, open(os.path.join(sys.path[0], f'{fname}.gui'), 'w') as dsl:
        Output(dom_generators.RandomHtml(), html, dsl)

if __name__ == '__main__':
    main()