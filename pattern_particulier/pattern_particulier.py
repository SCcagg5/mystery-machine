import sys
import json
import argparse

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
        self.args = args
        return args

if __name__ == "__main__":
    project = Pattern_particulier()
    print(project.main())
