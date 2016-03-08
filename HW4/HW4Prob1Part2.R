#Part 2 - Gibbs Sampling for fitting a Cauchy Regression Model
library(mvtnorm)
library(fMultivar)
library(LaplacesDemon)
Tot_time=800
Sample_size=1000
p=2
cauchy2d<-rcauchy2d(Sample_size, rho = 0.8)
x=cauchy2d[,1]
y=cauchy2d[,2]
plot(x,y,cex=0.5, col = "steelblue",pch='x')
X=cbind(rep(1.0,Sample_size),x)

#Set up the parameters for each iter and initialize the parameter
gamma = matrix(0,Sample_size,Tot_time)
phi=rep(0,Tot_time)
beta=matrix(0,p,Tot_time)
gamma[,1]=1
phi[1]=1
beta[,1]=1
for( t in 2:Tot_time)
{
   for(i in 1:Sample_size) gamma[i,t]=rgamma(1,shape=1,rate=0.5*(phi[t-1]*(y[i]-beta[,t-1]%*%X[i,])^2+1))
   phi[t]=rgamma(1,shape=0.5*Sample_size,rate=0.5*t(y-X%*%beta[,1])%*% diag(gamma[,t])%*%(y-X%*%beta[,1]))
   S=round(matrix(solve(t(X)%*%X)/phi[t],2,2),6)
   beta[,t]=rmvc(n=1, mu = t(solve(t(X)%*%X)%*%(t(X)%*%y)), S=S)
}
hist(beta[1,700:Tot_time],breaks = 40)
hist(beta[2,700:Tot_time],breaks = 40)
#plot(c(1:Tot_time),beta[1,1:Tot_time], cex=0.5,col = "orange",pch='*')
#plot(c(1:Tot_time),beta[2,1:Tot_time], cex=0.5,col = "orange",pch='*')
#plot(beta[1,1:Tot_time],beta[2,1:Tot_time],cex=0.5, col = "red",pch='*')