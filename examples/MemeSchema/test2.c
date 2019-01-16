#include <iostream>
#include <stdio.h>
#include <stdlib.h>
void fake_sort(int* tab,int taille)
{
	int i,tmp,j,f;
	for(i=0;i<taille;i++)
	{
		tmp=tab[i];
		j=i;
		f=12;
		while(f>5){
			tab[j]=tab[j-1];
			j--;
		}
		
	}
}
