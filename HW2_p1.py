import numpy as np
import matplotlib.pyplot as plt

def TrueCoverageProb(N):
    p=np.arange(0.01,1.00,0.01)
    #X = map(lambda x: np.random.binomial(N, x),p)
    count=list(np.zeros(len(p)))
    iteration=10000
    for i in range(iteration):
        X = map(lambda x: np.random.binomial(N, x),p)
        Sample=map(lambda xx: np.random.beta(xx+0.5,N-xx+0.5,10000),X)
        Sample=[np.sort(x) for x in Sample]
        CI=[(x[250-1],x[9750-1]) for x in Sample]
        check=map(lambda x,y: (x <= y[1] and x>=y[0])*1,p,CI)
        count=map(lambda x,y: x+y,count,check)
    return [x/iteration*1.0 for x in count]
resultN30=TrueCoverageProb(30)
resultN50=TrueCoverageProb(50)
resultN100=TrueCoverageProb(100)

print resultN30 
print resultN50 
print resultN100 
plt.plot(resultN30)
plt.plot(resultN50)
plt.plot(resultN100)

