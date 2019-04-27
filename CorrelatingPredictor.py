class CorrelatingPredictor:
    
    globalHistory = list()
    localBHT = list()
    m = 0
    n = 0
    hit = 0
    miss = 0
    
    def __init__(self, m, n, size):
        tableSize = int(size / ((2**m)*n))
        self.globalHistory = [False for j in range(m)]
        self.localBHT = [[[False for k in range(n)] for j in range(tableSize)] for i in range(2**m)]
        self.n = n
        self.m = m
        self.globalHistory[0] = True
        for i in range(len(self.localBHT)):
            for j in range(len(self.localBHT[i])):
                self.localBHT[i][j][0] = True
    
    def predict(self, PC, branch):
        #calculate BHT address from 
        #print(PC, end=' ')
        PC = PC % len(self.localBHT[0])
        #print(PC, end=' ')
        #calculate which local BHT needs to accessed
        BHT = 0
        for i, val in enumerate(self.globalHistory):
            if val:
                BHT += 2**(self.m-i-1)
        #check whether the local BHT prediction matches the actual branch
        #print(self.localBHT[BHT][PC][0], branch, end=' ')
        if self.localBHT[BHT][PC][0] == branch:
            self.hit += 1
        else:
            self.miss += 1
        #shift the global history register left
        del self.globalHistory[0]
        self.globalHistory.append(branch)
        #print(self.globalHistory)
        #determine whether the value stored in the local BHT is not the min in the case of branch missed or max in the case of branch taken
        test = False
        for i in range(self.n):
            if self.localBHT[BHT][PC][i] != branch:
                test = True
                break
        #if above condition holds true, then increment or decrement local BHT value accordingly
        if test:
            for i in range(self.n):
                self.localBHT[BHT][PC][self.n-i-1] = not(self.localBHT[BHT][PC][self.n-i-1])
                if self.localBHT[BHT][PC][self.n-i-1] == branch:
                    break
    
    def getMissRate(self):
        return self.miss / (self.hit + self.miss)
    
    def getSize(self):
        return self.n * (2**self.m) * len(self.localBHT[0])
    
    def getN(self):
        return self.n
    
    def getM(self):
        return self.m
