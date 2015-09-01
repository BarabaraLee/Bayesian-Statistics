library(xtable)

X=matrix(c(-3:4,0.5,2,1,3,1,3,2,0.5,0.1,0.3,0.05,0.15,0.05,0.1,0.2,0.05),nrow=3,ncol=8,byrow = TRUE)
Likelihood=X[2,]
Prior=X[3,]
Den=sum(Likelihood*Prior)#=1.925
Posterior=Likelihood*Prior/Den
xtable(rbind(X,Posterior), digits=4)

matplot(X[1,], cbind(Likelihood,Prior,Posterior), pch=c(1,2,3),lwd=c(2,2,2),xlab='??',ylab='Likelihood, Prior and Posterior')
legend("topleft",bty="n", inset=0, legend=c("Likelihood","Prior","Posterior"),pch=c(1,2,3))

EXt=sum(X[1,]*Posterior)#=0.2857143