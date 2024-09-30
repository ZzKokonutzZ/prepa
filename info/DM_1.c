#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//exo 10
double fraction(int a,int b)
{
    double fa=a;
    double fb=b;
    double f=fa/fb;
    return(f);
}

//exo 11
bool bissextile(int year)
{
    if(year%400==0) return(true);
    if(year%100==0) return(false);
    if(year%4==0) return(true);
    return(false);
}

//exo 12
double evalue(double coefs[],int size, double x)
{
    double result=coefs[size-1];
    for (int i=1;i<size;i+=1)
    {
        result*=x;
        result+=coefs[size-i-1];
    }
    return(result);
}

//exo 13
int ecart_min(int tab[], int size)
{
    int e_min=abs(tab[0]-tab[1]);
    for (int i=1;i<size;i+=1)
    {
        if (abs(tab[i-1]-tab[i])<e_min) e_min=abs(tab[i-1]-tab[i]);
    }
    return(e_min);
}

int main()
{
    printf("[exo 10] \n");
    int a=5;
    int b=2;
    printf("a/b=%f \n",fraction(a,b));

    printf("\n[exo 11] \n");
    printf("2042 est bissextile : %d \n",bissextile(2042));
    printf("2420 est bissextile : %d \n",bissextile(2420));
    printf("2100 est bissextile : %d \n",bissextile(2100));
    printf("2400 est bissextile : %d \n",bissextile(2400));

    printf("\n[exo 12] \n");
    double x=42.0;
    double deg_0[]={5.0};
    double deg_1[]={0.0,10.0};
    double deg_2[]={8.0,4.0,-2.0};
    printf("f(x)=5 evaluee en 42 : %f \n",evalue(deg_0,1,x));
    printf("f(x)=10x+0 evaluee en 42 : %f \n",evalue(deg_1,2,x));
    printf("f(x)=-2x^2+4x+8 evaluee en 42 : %f \n",evalue(deg_2,3,x));

    printf("\n[exo 13] \n");
    

    return(0);
}