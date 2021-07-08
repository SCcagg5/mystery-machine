import sys
import json

class Money_for_nothing:
    def __init__(self, data):
        self.data = json.loads(data)
        self.achat_vente = []

    def main(self):
        index = 1
        while index < len(self.data):
            while index < len(self.data) \
             and self.data[index] <= self.data[index - 1]:
                index += 1
            if index <= len(self.data):
                self.achat_vente.append(index - 1)
                index += 1
            while index < len(self.data) \
             and self.data[index] >= self.data[index - 1]:
                index += 1
            if index <= len(self.data):
                self.achat_vente.append(index - 1)
                index += 1
        if len(self.achat_vente) % 2 != 0:
            self.achat_vente = self.achat_vente[:-1]
        return self.achat_vente

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    project = Money_for_nothing(sys.argv[1])
    print(project.main())
