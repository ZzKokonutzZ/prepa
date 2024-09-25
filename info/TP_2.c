#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//exo 1
int exchange_int(int *x,int *y)
{
    int z=*x;
    *x=*y;
    *y=z;
}

//exo 2
int exchange_first(int *tab_pp)
{
    int holder=tab_pp[0];
    tab_pp[0]=tab_pp[1];
    tab_pp[1]=holder;
}

int main()
{
    printf("exo 1 \n");
    int x=42;
    int y=120;
    printf("x vaut %d, y vaut %d \n",x,y);
    exchange_int(&x,&y);
    printf("x vaut %d, y vaut %d \n",x,y);

    printf("exo 2 \n");
    int tab[5]={1,0,2,3,4};
    printf("tab[0] vaut %d, tab[1] vaut %d \n",tab[0],tab[1]);
    int *tab_p=tab;
    exchange_first(tab_p);
    printf("tab[0] vaut %d, tab[1] vaut %d \n",tab[0],tab[1]);

    exit(0);
}
