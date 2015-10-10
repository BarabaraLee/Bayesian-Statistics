import numpy as np
import matplotlib as mpl
import pandas as pd

def LE(p_hat,N):
    return p_hat-1.96*np.sqrt((p_hat*(1-p_hat)/N))
    
def RE(p_hat,N):
    return p_hat+1.96*np.sqrt((p_hat*(1-p_hat)/N))
    
for N in [30,50,100]:
    perc=[]
    for p in np.arange(0.01,1.0,0.01):
        X=np.random.binomial(N,p,10000)
        p_hat=X/float(N)
        CI_L=LE(p_hat,N)
        CI_R=RE(p_hat,N)
        count=0.0
        for i in range(len(CI_L)):
            if CI_L[i]<=p and CI_R[i]>=p: count=count+1
        perc.append(count/10000.0)
    TCP=pd.DataFrame(perc)
    ax=TCP.plot()
    ax.set_ylabel('True Coverage Probability')
    ax.set_xlabel('True p')
    mpl.pyplot.title("The True Coverage Probability Plot (N=%i)"% N)
mpl.pyplot.show()
