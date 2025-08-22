#include <stdlib.h>
#include <stdbool.h>
int* creer_pile(int capacite)
{
    int* pile = malloc((capacite+2)*(sizeof(int)));
    pile[0]=capacite;
    pile[1]=0;
}

void empiler_pile(int* pile, int x)
{
    pile[pile[1]]=x;
    pile[1]+=1;
    if (pile[1]>pile[2]) exit(1);
}

int depiler_pile(int* pile)
{
    if (pile[1]==0) exit(1);
    pile[1]-=1;
    return pile[pile[1]+2];

}

bool vide_pile(int* pile)
{
    return (pile[1]==0);
}

