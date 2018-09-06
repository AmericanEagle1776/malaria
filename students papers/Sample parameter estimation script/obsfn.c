#include <R.h>
 #include <math.h>
 void obsfn_oou2rt84 ( double * x, double * y, double * p, int * n, int * k, int * l ) {
 for(int i = 0; i< *n; i++) {
 y[0+i**l] = x[0+i**k] ;
y[1+i**l] = x[1+i**k] ; 
}
}