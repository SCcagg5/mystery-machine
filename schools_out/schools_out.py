import sys
import json
import datetime


class Schools_out:
    def __init__(self, file):
        self.file = file
        self.data = None
        self.salles = 0

    def read(self):
        f = open(self.file)
        self.data = json.load(f)
        f.close()

    def main(self):
        intervals = []
        self.salles = 0
        min = datetime.datetime.strptime('23:59', "%H:%M")
        max = datetime.datetime.strptime('0:00', "%H:%M")
        for course in self.data:
            start = datetime.datetime.strptime(course['start'], "%H:%M")
            end = datetime.datetime.strptime(course['end'], "%H:%M")
            intervals.append({'start': start, 'end': end, 'id': id})
        for heures in range(0, 24):
            for minutes in range(0, 60):
                salles = 0
                to_test =  datetime.datetime.strptime(f'{heures}:{minutes}', "%H:%M")
                for course in intervals:
                    if (course['start'] <= to_test and course['end'] >  to_test) \
                    or (course['start'] <  to_test and course['end'] >= to_test):
                        salles += 1
                if salles > self.salles:
                    self.salles = salles
        return self.salles

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Schools_out(sys.argv[1])
    project.read()
    print(project.main())
