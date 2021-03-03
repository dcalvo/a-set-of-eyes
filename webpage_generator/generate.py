import sys
import os
import dom_generators

# Write generator output to console and file
def Output(generator, out):
    if isinstance(generator, str):
        print(generator)
        out.write(generator)
    else:
        for g in generator: Output(g, out)

def main():
    # To change the output file, put a filename without the HTML extension in the arguments
    # Sample run:
    # py generate.py sample1
    f_name = "index" if len(sys.argv) == 1 else sys.argv[1]
    with open(os.path.join(sys.path[0], f_name + '.html'), 'w') as out:
        Output(dom_generators.RandomHtml(), out)

if __name__ == '__main__':
    main()