#include <iostream>
#include <stdio.h>
#include <stdlib.h>
int is_sorted(int *tableau, int n)
{
int j;
    for(j= 1; j < n; i++)
    {
        if(tableau[j-1] > tableau[j])
        {
            return 0;
        }
    }
    return 1;
}
