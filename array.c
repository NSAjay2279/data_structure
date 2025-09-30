#include<stdio.h>
int main()
{
  int A[4];
  printf("%d\n", &A); // address of the entire array
  printf("%d\n", A);  // A decays to &A[0] (address of first element)
}
