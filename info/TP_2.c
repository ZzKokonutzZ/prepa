#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//exo 1
int exchange(int *x,int *y)
{
    int z=*x;
    *x=*y;
    *y=z;
}

int main()
{
    printf("exo 1 \n");
    int x=42;
    int y=120;
    printf("x vaut %d, y vaut %d \n",x,y);
    exchange(&x,&y);
    printf("x vaut %d, y vaut %d \n",x,y);

    exit(0);
}
