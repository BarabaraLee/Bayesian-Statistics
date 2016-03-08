import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

alpha=0.5
beta=1
gamma=1.0
mu=0.0

def rv_y_phi(alpha,beta,gamma,mu):
    phi=np.random.gamma(alpha,1.0/beta)
    return np.random.normal(mu,np.sqrt(gamma/phi))

sample=[]
for i in range(1000):
    sample.append(rv_y_phi(alpha,beta,gamma,mu))
    
plt.figure()
bins= np.sort([0,1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])
n, bins, patches = plt.hist(sample, bins, normed=1, histtype='bar', rwidth=0.8,color='w')
plt.show()
print np.min(sample)
print np.max(sample)
