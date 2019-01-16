#include <iostream>
#include <stdio.h>
#include <stdlib.h>
int is_sorted(int *tab, int taille)
{
int i;
    for(i= 1; i < taille; i++)
    {
        if(tab[i-1] > tab[i])
        {
            return 0;
        }
    }
    return 1;
}
