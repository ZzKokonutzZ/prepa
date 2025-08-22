#include<stdio.h>
#include<stdlib.h>


int main()
{
    double n=1-1/5-1/5-1/5-1/5-1/5;
    printf("%d \n",n);
    int b=0;
    double x=101.0;
    while (x!=100)
    {
        x=(x+100.0)/2.0;
        b+=1;
    }
    printf("%d",b);
    exit(0);
}