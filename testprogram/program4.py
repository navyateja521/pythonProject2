class find_fact:
    def __init__(self,n):
        self.n=n

    def number(self,givennumber,fact):
        self.fact=1
        # if givennumber <0:
        #     return "enter positive number!"
        # elif givennumber ==0:
        #     return "enter the number other than 0"
        # else givennumber >0:
            for i in range(self.givennumber+1):
                self.fact=self.fact*i
            return self.fact


