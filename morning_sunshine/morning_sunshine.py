import sys
import json
import math

class Morning_sunshine:
    def __init__(self, data):
        self.file = file
        self.data = json.loads(data)
        self.benefices = 0

    def main(self):
        max = 0
        for batiment in self.data[::-1]:
            benef = 0
            for appartement in batiment["floor_layout"]:
                if 'E' in appartement['orientations']:
                    if batiment['height'] > max:
                        benef += math.floor(appartement['monthly_rent'] * 0.05)
                        benef *= batiment['height'] - max
                        max = batiment['height']
            self.benefices += benef
        return self.benefices

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Morning_sunshine(sys.argv[1])
    project.read()
    print(project.main())
