# Creates a visualization of 2D random walk steps
# This visualization code was written by Vincent Granville
# and was included in his blog post on Data Science Central

vv<-read.table("rw.txt",header=TRUE);
iter<-vv$iter;
minx=min(vv$x);
maxx=max(vv$x);
miny=min(vv$y);
maxy=max(vv$y);
for (n in 1:2000) {

  x<-vv$x[iter == n]; 
  y<-vv$y[iter == n]; 
  p<-vv$x[iter == n-1]; 
  q<-vv$y[iter == n-1];
  if (n==1) { 
          plot(x,y,xlim=c(minx,maxx),ylim=c(miny,maxy),pch=40, cex=0,col=rgb(1,1,0),xlab="",ylab="",axes=TRUE);
  }
  s=1/sqrt(1+n);
  points(p,q,col=rgb(1-s,1-s,1-s),pch=20,cex=0.01);
  points(x,y,col=rgb(1,0,0),pch=20,cex=0.01);
# Sys.sleep(0.2); 
}