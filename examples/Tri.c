#include <iostream>
#include <stdio.h>
#include <stdlib.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void counting_sort(int *tab, int taille)
{
  int i, min, max;
 
  min = max = tab[0];
  for(i=1; i < taille; i++) {
    if ( tab[i] < min ) {
      min = tab[i];
    } else if ( tab[i] > max ) {
      max = tab[i];
    }
  }
}
int partition(int * tab, int d, int f)
{
    int tabInter[f+1-d];
    int i;
    int l=0;
    int k=f-d;
    int indice;
    for(i=d+1;i<=f;i++)
    {
        if(tab[i]<tab[d])
        {
            tabInter[l]=tab[i];
            l++;
        }
        else
        {
            tabInter[k]=tab[i];
            k--;
        }
    }
    tabInter[l]=tab[d];
    for(i=d;i<=f;i++)
    {
        tab[i]=tabInter[i-d];
    }
    return l+d;
}
void quick_sort(int * tab, long premier, long dernier)
{
  if( premier < dernier ) {
         int pivot = partition (tab,premier , dernier ) ;     
         quick_sort (tab,premier , pivot -1);
         quick_sort ( tab,pivot +1 , dernier) ;
   }  
}
void bubble_sort(int* tab,int taille)
{
    int tmp,i,j;
    for(i = 0; i < taille; i++)
    {
        for(j = 0; j < taille-i-1; j++)
        {
            if (tab[j] > tab[j+1])
            {
                tmp        = tab[j];
                tab[j]     = tab[j+1];
                tab[j+1]   = tmp;
            }
        }
    }
}
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
void swap(int *a, int *b)
{
	int aux;
	aux = *a;
	*a = *b;
	*b = aux;
}
void cocktail_sort(int *tab,int taille) {
	
	int i,j,continu,k,tmp;
	do {
	for(i = 0; i < taille/2; i++)
	{
		continu = 0;
		for(j = i; j < taille-i-1; j++)
		{
			if(*(tab+j) > *(tab+j+1))
			{
				tmp = tab[j];
				tab[j]=tab[j+1];
				tab[j+1]=tmp;
				continu = 1;
			}
		}
		for(k = taille-2-i; k > i; k--)
		{
			if(*(tab+k) < *(tab+k-1))
			{
				tmp = tab[k];
				tab[k]=tab[k-1];
				tab[k-1]=tmp;
				continu = 1;
			}
		}

	}
} while(continu == 1);

}
int main(int argc, char** argv) {
	int tab[5]={3,2,6,1,7};
	cocktail_sort(tab,5);
	if(is_sorted(tab,5)) printf("ok");
	return 0;
}
