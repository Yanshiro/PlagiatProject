#include <iostream>
#include <stdio.h>
#include <stdlib.h>
void selection_sort( int*tab,int taille)
{
    int i, k, t, min;
    for( i = 0; i < taille-1; i++)
    {
        min = i;
        for( k = i+1; k < taille; k++)
        {
            if( tab[k] < tab[min])
                min = k;
        }
        t = tab[min];
        tab[min] = tab[i];
        tab[i] = t;
    }
 }
