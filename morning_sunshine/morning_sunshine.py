import sys
import json
import math

class Morning_sunshine:
    def __init__(self, file):
        self.file = file
        self.data = None
        self.benefices = 0

    def read(self):
        f = open(self.file)
        self.data = json.load(f)
        f.close()

    def main(self):
        for batiment in self.data:
            benef = 0
            for appartement in batiment["floor_layout"]:
                if 'E' in appartement['orientations']:
                    benef += math.floor(appartement['monthly_rent'] * 0.05)
                    benef *= batiment['height']
            self.benefices += benef
        return self.benefices

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Morning_sunshine(sys.argv[1])
    project.read()
    print(project.main())
