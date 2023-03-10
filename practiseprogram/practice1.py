import os
class Searchfiles():
    def __init__(self):
        pass
    def searchfile(self,dir,filename):
        self.filename = filename
        self.dir = dir
        self.f=[]
        for root,dir,file in os.walk(self.dir):
            if self.filename in file:
                self.f.append(os.path.join(root,self.filename))
        return self.f
# od = Searchfiles()
# print(od.searchfile())