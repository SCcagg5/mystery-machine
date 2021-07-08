import sys
import json
import math
import hashlib

class Flowrent_pagny:
    def __init__(self, data, data2):
        self.map = json.loads(data)
        self.task = json.loads(data2)
        self.res = []

    def main(self):
        for task in self.task:
            for  map in self.map:
                _, ret = self.run(map, task["input"])
                self.res.append(ret)
        return json.dumps(self.res)

    def run(self, task, input):
        res = b''
        if isinstance(input, str):
            input = input.encode('utf-8')
        if task["task_type"] == "primitive":
            res = input
        elif task["task_type"] == "workflow":
            for task_id in task["tasks"]:
                i = 0
                while i < len(self.map):
                    if self.map[i]["id"] == task_id:
                        r, _ = self.run(self.map[i], input)
                        res += r
                        break
                    i += 1
        return hashlib.md5(res).digest(), hashlib.md5(res).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit()
    project = Flowrent_pagny(sys.argv[1], sys.argv[2])
    print(project.main())
