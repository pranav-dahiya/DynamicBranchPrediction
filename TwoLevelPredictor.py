import math

class TwoLevelPredictor:

    shiftRegister = list()
    PHT = list()
    n = 0
    m = 0
    hit = 0
    miss = 0

    def __init__(self, n, size):
        self.n = n
        self.m = int(math.log2(size)) - n - 1
        self.shiftRegister = [False for i in range(self.m)]
        self.PHT = [[[False for k in range(2)] for j in range(2**self.m)] for i in range(2**self.n)]
        for i in range(len(self.PHT)):
            for j in range(len(self.PHT[i])):
                self.PHT[i][j][0] = True

    def predict(self, PC, branch):
        #print(self.shiftRegister, end=' ')
        #compute PHT number from PC
        PC = PC % (2**self.n)
        #compute index of PHT from shiftRegister
        index = 0
        for i, val in enumerate(self.shiftRegister):
            if val:
                index += 2**(self.m - i - 1)
        #check if prediction matches branch
        #print(index, self.PHT[index][0], branch)
        if self.PHT[PC][index][0] == branch:
            self.hit += 1
        else:
            self.miss += 1
        #left shit shitRegister
        del self.shiftRegister[0]
        self.shiftRegister.append(branch)
        #determine whether the value stored in the PHT is not the min in the case of branch missed or max in the case of branch taken
        test = False
        for i in range(2):
            if self.PHT[PC][index][i] != branch:
                test = True
                break
        #if above condition holds true, then increment or decrement BHT value accordingly
        if test:
            for i in range(2):
                self.PHT[PC][index][1-i] = not(self.PHT[PC][index][1-i])
                if self.PHT[PC][index][1-i] == branch:
                    break

    def getMissRate(self):
        return self.miss / (self.hit + self.miss)

    def getSize(self):
        return len(self.PHT) * len(self.PHT[0])

    def getN(self):
        return self.n
