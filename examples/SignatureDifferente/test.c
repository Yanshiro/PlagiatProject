#include <iostream>
#include <stdio.h>
#include <stdlib.h>
void insertion_sort(int* tab,int taille)
{
	int i,tmp,j;
	for(i=0;i<taille;i++)
	{
		tmp=tab[i];
		j=i;
		while(j>0 && tab[j-1]>tmp){
			tab[j]=tab[j-1];
			j--;
		}
		tab[j]=tmp;
	}
}
