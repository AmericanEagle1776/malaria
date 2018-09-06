#include <R.h>
 #include <math.h>
 void obsfn_deriv_zvdc6w6i ( double * x, double * y, double * p, int * n, int * k, int * l ) {
 for(int i = 0; i< *n; i++) {
 y[0+i**l] = (1)*(x[3+i**k]) ;
y[1+i**l] = (1)*(x[4+i**k]) ;
y[2+i**l] = (1)*(x[6+i**k]) ;
y[3+i**l] = (1)*(x[7+i**k]) ;
y[4+i**l] = (1)*(x[9+i**k]) ;
y[5+i**l] = (1)*(x[10+i**k]) ;
y[6+i**l] = (1)*(x[12+i**k]) ;
y[7+i**l] = (1)*(x[13+i**k]) ;
y[8+i**l] = (1)*(x[15+i**k]) ;
y[9+i**l] = (1)*(x[16+i**k]) ;
y[10+i**l] = (1)*(x[18+i**k]) ;
y[11+i**l] = (1)*(x[19+i**k]) ;
y[12+i**l] = (1)*(x[21+i**k]) ;
y[13+i**l] = (1)*(x[22+i**k]) ;
y[14+i**l] = (1)*(x[24+i**k]) ;
y[15+i**l] = (1)*(x[25+i**k]) ; 
}
}