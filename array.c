#include<stdio.h>

int SumOFElements(int A[])  // int A[] is int* A
{
  int i, sum = 0;
  for (i =0; i<size; i++)
  {
    sum+= A[i];  // A[i] is *(A+i)
  }
  return sum;
}

int main()
{
  int A[4];
  int size = sizeof(A)/sizeof(A[0])
  int total = SumOfElements(A, size);  // A can be used for &A[0]
  printf("%d\n", &A); // address of the entire array
  printf("%d\n", A);  // A decays to &A[0] (address of first element)
}
