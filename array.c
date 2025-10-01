#include<stdio.h>

int SumOFElements(int A[])  // int A[] is int* A
{
  int i, sum = 0;
  int size = sizeof(A) ...
  ...
}
int main()
{
  int A[4];
  printf("%d\n", &A); // address of the entire array
  printf("%d\n", A);  // A decays to &A[0] (address of first element)
}
