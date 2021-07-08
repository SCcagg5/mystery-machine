import sys
import json
import math

class Morning_sunshine:
    def __init__(self, data):
        self.data = json.loads(data)
        self.benefices = 0

    def main(self):
        max = 0
        for batiment in self.data[::-1]:
            for appartement in batiment["floor_layout"]:
                if 'E' in appartement['orientations'] and \
                    batiment['height'] > max:
                    benef =  appartement['monthly_rent']
                    benef =  math.ceil(benef * 0.05)
                    benef *= batiment['height'] - max
                    self.benefices += benef
            max = max if batiment['height'] < max else batiment['height']
        return self.benefices * 12

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Morning_sunshine(sys.argv[1])
    print(project.main())
