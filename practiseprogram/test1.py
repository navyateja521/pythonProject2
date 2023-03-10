import os
class Filecount():
    def __init__(self):
        self.count=0
    def count_file(self,dir):
        self.dir=dir
        for file in os.listdir(self.dir):
            if file.endswith(".py"):
                self.count += 1
        return self.count

        # print(count)
# dir = '..//normal//testprogram'
# obj=Filecount()
# print(obj.count_file(dir))
