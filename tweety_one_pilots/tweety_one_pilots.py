import sys
import json


class Tweety_one_pilots:
    def __init__(self, file):
        self.file = file
        self.data = None
        self.hashtags = []

    def read(self):
        f = open(self.file)
        self.data = json.load(f)
        f.close()

    def main(self):
        percentage = self.data['percentage_threshold']
        length = 0
        hashtags = {}
        for tweet in self.data['tweets']:
            for hashtag in tweet['hashtags']:
                if hashtag not in hashtags:
                    hashtags[hashtag] = 0
                hashtags[hashtag] += 1
                length += 1
        min = length * percentage / 100
        for hashtag in hashtags:
            if hashtags[hashtag] >= min:
                self.hashtags.append(hashtag)
        return json.dumps(self.hashtags)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Tweety_one_pilots(sys.argv[1])
    project.read()
    print(project.main())
