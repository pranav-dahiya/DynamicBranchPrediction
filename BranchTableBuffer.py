import math

class BranchTableBuffer:
    
    BTB = list()
    hit = 0
    miss = 0
    
    def __init__(self, size):
        self.BTB = [0 for i in range(int(size/24))]
    
    def predict(self, PC, target):
        #print(PC, end=' ')
        #compute BTB address from PC
        PC = PC % len(self.BTB)
        #print(PC, self.BTB[PC], target)
        #determine whether prediction is correct
        if self.BTB[PC] == target:
            self.hit += 1
        else:
            self.miss += 1
        #update BTB
        self.BTB[PC] = target
    
    def getMissRate(self):
        return self.miss / (self.hit + self.miss)
    
    def getSize(self):
        return len(self.BTB) * 24
