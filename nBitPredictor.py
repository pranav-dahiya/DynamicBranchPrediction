class nBitPredictor:
    
    hit = 0
    miss = 0
    n = 0
    BHT = list()
    
    def __init__(self, n, size):
        self.n = n
        self.BHT = [[False for j in range(n)] for i in range(int(size/n))]
        for i in range(len(self.BHT)):
            self.BHT[i][0] = True
    
    def predict(self, PC, branch):
        #print(self.n, PC, end=' ')
        #get BHT address from PC
        PC = PC % len(self.BHT)
        #print(PC, actualBranch, self.BHT[PC][0])
        #check whether the prediction matches the branch and increment hit or miss accordingly
        if self.BHT[PC][0] == branch:
            self.hit += 1
        else:
            self.miss += 1
        #determine whether the value stored in the BHT is not the min in the case of branch missed or max in the case of branch taken
        test = False
        for i in range(self.n):
            if self.BHT[PC][i] != branch:
                test = True
                break
        #if above condition holds true, then increment or decrement BHT value accordingly
        if test:
            for i in range(self.n):
                self.BHT[PC][self.n-i-1] = not(self.BHT[PC][self.n-i-1])
                if self.BHT[PC][self.n-i-1] == branch:
                    break

    
    def printHitMiss(self):
        print(self.hit, self.miss)
    
    def getMissRate(self):
        return self.miss / (self.hit + self.miss)
    
    def getSize(self):
        return self.n * len(self.BHT)
    
    def getN(self):
        return self.n
