#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//exo 1
int exchange_int(int *x,int *y)
{
    int z=*x;
    *x=*y;
    *y=z;
    return(0);
}

//exo 2
int exchange_first(int *tab_p)
{
    int holder=tab_p[0];
    tab_p[0]=tab_p[1];
    tab_p[1]=holder;
    return(0);
}

//exo 3
int exchange_last(int *tab_p, int size)
{
    int holder=tab_p[0];
    tab_p[0]=tab_p[size-1];
    tab_p[size-1]=holder;
    return(0);
}

//exo 4
int find_n(int *tab_p, int size, int n)
{
    for (int i=0;i<size;i+=1)
    {
        if (tab_p[i]==n)
        {
            return(i);
        }
    }
    return(-1);
}

int nb_a(int *tab_p,int size, int a)
{
    int nb=0;
    for (int i=0;i<size;i+=1)
    {
        if (tab_p[i]==a)
        {
            nb+=1;
        }
    }
    return(nb);
}

//exo 6
int tab_switch(int *tab_p, int a, int b)
{
    int holder=tab_p[a];
    tab_p[a]=tab_p[b];
    tab_p[b]=holder;
    return(0);
}
int bubble_sort(int *tab_p, int size)
{
    int sorted=0;
    while ( sorted==0 )
    {
        int test=0;
        for(int i=0;i<size-1;i+=1)
        {
            if (tab_p[i]>tab_p[i+1]) 
            {
                tab_switch(tab_p,i,i+1);
                test=1;
            }

        }
        if (test==0) sorted=1;
    }
    return(0);
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

    printf("exo 3 \n");
    printf("tab[0] vaut %d, tab[4] vaut %d \n",tab[0],tab[4]);
    exchange_last(tab_p,5);
    printf("tab[0] vaut %d, tab[4] vaut %d \n",tab[0],tab[4]);

    printf("exo 4 \n");
    printf("indice de 3 dans tab : %d \n",find_n(tab_p,5,3));
    printf("indice de 7 dans tab : %d\n",find_n(tab_p,5,7));

    printf("exo 5 \n");
    tab[2]=0;
    tab[3]=0;
    printf("nobre d'occurences de 0 dans tab : %d \n",nb_a(tab_p,5,0));
    printf("nobre d'occurences de 4 dans tab : %d \n",nb_a(tab_p,5,4));
    printf("nobre d'occurences de 7 dans tab : %d \n",nb_a(tab_p,5,7));
    
    printf("exo 6 \n");
    for (int i=0;i<5;i+=1)
    {
        tab[i]=5-i;
    }
    bubble_sort(tab_p,5);
    for (int i=0;i<5;i+=1)
    {
        printf("%d \n",tab[i]);
    }

    exit(0);
}
