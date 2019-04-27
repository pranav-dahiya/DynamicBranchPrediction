from nBitPredictor import nBitPredictor
from CorrelatingPredictor import CorrelatingPredictor
from TwoLevelPredictor import TwoLevelPredictor
from BranchTableBuffer import BranchTableBuffer
import multiprocessing

def simulatePredictors(filename):
    output = ""
    predictors = []
    for size in [2**i for i in [10,11,12,13,14,15,16]]:
    #    for m in [8]:
            for n in [3,5,6,7]:
                #predictors.append(nBitPredictor(n, size))
                #predictors.append(CorrelatingPredictor(m, n, size))
                predictors.append(TwoLevelPredictor(n, size))
                #predictors.append(BranchTableBuffer(size))
                #print(size)
    for size in [2**i for i in [15,16]]:
        for n in [1,2,3,4,5,6,7]:
            predictors.append(TwoLevelPredictor(n, size))
    with open(filename) as f:
        for line in f:
            if line[20] != '-':
                PC = int(line[2:8], 16)
                branch = (line[20] == 'T')
                #target = int(line[66:72], 16)
                for predictor in predictors:
                    predictor.predict(PC, branch)
                    #predictor.predict(PC, target)
    output += filename + "\n"
    for predictor in predictors:
        #output += str(predictor.getSize()) +  ", " + str(predictor.getM()) + ", " + str(predictor.getN()) + ": " + str(predictor.getMissRate()) + "\n"
        output += str(predictor.getSize()) + ", " + str(predictor.getN()) + ": " + str(predictor.getMissRate()) + "\n"
        #output += str(predictor.getSize()) + ", " + str(predictor.getM()) + ": " + str(predictor.getMissRate()) + "\n"
        #output += str(predictor.getSize()) + ": " + str(predictor.getMissRate()) + "\n"
    return output

filenames = ["art.trace", "gcc.trace", "go.trace", "hmmer.trace", "libquantum.trace", "mcf.trace", "sjeng.trace", "sphinx3.trace"]
#filenames = ["gcc-1K.trace"]

pool = multiprocessing.Pool(multiprocessing.cpu_count())

processes = []
for filename in filenames:
    processes.append(pool.apply_async(simulatePredictors, (filename,)))

with open("output.txt", "w") as f:
    for process in processes:
        output = process.get()
        print(output)
        f.write(output)

