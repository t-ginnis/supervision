#include<stdio.h>
#include<armadillo>
#include<cmath>
using namespace std;
using namespace arma;

int main()
{
  int N=10000, M=1000;
  double D;
  //initialising vectors and matrices
  mat A(N,N,fill::randu);
  vec x(N,fill::randu);
  vec y(N,fill::randu);
  
  //generating matrix and vectors
  for (int j=0;j<N;j++){
    x(j)=cos(j+1);
    y(j)=cos(2*(j+1));
    for (int i=0;i<N;i++){
      A(i,j)=sin(i-j+1); //done this way as 1st element is contiguous 

    }

  }

  //need to transpose A as it is reversed
  A=A.t();

  // calculating D
  for(int i=0;i<M;i++){
    D=dot(y,(A.t())*(A*x));
  }

  cout << D <<endl;
  return 0;
}
