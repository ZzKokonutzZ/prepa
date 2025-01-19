#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
void insertsort(int* tab, int size)
{
    for (int i=0; i<size; i+=1)
    {
        int e = tab[i];
        for (int j=0; j<=i; j+=1)
        {
            if (tab[j]<e) 
            {
                tab[i]=tab[j];
                tab[j]=e;
            }

        }
    }
}

void selectsort(int* tab, int taille)
{
    for (int i=0; i<taille-1; i+=1)
    {
        int min=tab[i];
        int j=i+1;
        for ( j; j<taille; j+=1)
        {
            if (tab[j]<min) min=tab[j];
        }
        tab[j]=tab[i];
        tab[i]=min;
    }
}

void cocktailsort(int* tab, int taille)
{
    bool flag = false;
    while (!flag)
    {
        flag=true;
        for (int i=0; i<taille-1; i+=1)
        {
            if (tab[i]>tab[i+1]) 
            {
                int h=tab[i];
                tab[i]=tab[i+1];
                tab[i+1]=h;
                flag=false;
            }

            if (tab[taille-i-2]>tab[taille-i-1])
            {
                int h=tab[taille-i-1];
                tab[taille-i-1]=tab[taille-i-2];
                tab[taille-i-2]=h;
                flag=false;

            }
        }
    }
}

void decaler(int* tab, int size)
{
    for (int i=size; i>0; i-=0)
    {
        tab[i]=tab[i-1];
    }
}
void colle(int* tab1, int size1, int* tab2, int size2)
{
    int i=0;
    int j=0;
    int t=0;
    int k=0;
    int n=0;
    while (i<size1 || j<size2)
    {
        if (tab1[i+t]<=tab2[j+k]);
    }
}
void ipfs(int* tab, int size)
{
    if (size>=2)
    {
        int i = size/2;
        ipfs(tab,i);
        ipfs(&tab[i],size-i);
    }

}