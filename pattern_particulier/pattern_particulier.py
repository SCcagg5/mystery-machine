import sys
import json
import argparse
import re

class Pattern_particulier:
    def __init__(self):
        self.data = None
        self.matchs = []

    def read(self):
        f = open(self.file)
        self.data = f.read()
        f.close()

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('files', metavar='N', type=str, nargs='+')
        parser.add_argument("-e", action='append')
        args = vars(parser.parse_intermixed_args())
        for file in args['files']:
            f = open(file)
            text = f.read()
            f.close()
            for a in args['e']:
                match = 0
                while True:
                    m = re.search(a, text[match:])
                    if m is None or match > len(text):
                        break
                    span = m.span()
                    self.matchs.append({"pattern": a, "offset": match + span[0] })
                    match += span[1] if span[1] > 0 else 1
        return json.dumps(self.matchs)

if __name__ == "__main__":
    project = Pattern_particulier()
    print(project.main())
