#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//exo 20
int spitsize(bool tab[],int size)
{
    int nb=1;
    for (int i=0; i<size; i+=1)
    {
        if (tab[i]==tab[0])
        {
            nb+=1;
        }
        else return nb;
    }
}

//exo 21
int lastzero(bool tab[],int size)
{
    int i=size-1;
    while (!tab[i] && i<0)
    {
        i-=1;
    } 
    return i;
}
bool nul(bool tab[], int size)
{
    int t=lastzero(tab,size);
    int nbtrue=0;
    int nbfalse=0;
    for (int i=0;i<t;i+=1)
    {
        if (tab[i]) nbtrue+=1;
        else nbfalse+=1;
        if (nbtrue<nbfalse) return false;
    }
    return true;

}

//exo 22
double modfloat(double a, double b)
{
    double r=a/b-(int)(a/b);
    r*=a;
    if (r<0 && b>=0) return r+b;
    if (r<0 && b<0) return r-b;
    return r;
}

int main()
{

}