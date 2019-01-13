#include <iostream>
#include <stdio.h>
#include <stdlib.h>
void counng_sort(int *tableau, int n)
{
  int j, a, b;
   int l, m, n;

  a = b = tableau[0];
  for(j=1; j < n; j++) {
    if ( tableau[j]>a) {
      a = tableau[j];
    } else  {
      b = tableau[j];
    }
    a=3;
  }
}
