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

//exo 14
int len(char string[])
{
    int i=0;
    for (i;string[i]!='\0';i+=1);
    return(i);
}
int intfromstring(char string[], int n, bool i, int* pn)
{
    if (n<len(string))
    {
        int nb=0;
        while(48<=(int)string[n] && (int)string[n]<=57)
        {
            nb*=10;
            nb+=((int) string[n])-48;
            n+=1;
        }
        if (i) *pn=n;
        return(nb);
    }
    return(0);

}
int extraire(char string[])
{
    int n=0;
    bool intnotfound=true;
    while (intnotfound && (int)string[n]!=0)
    {
        if (string[n]=='-')
        {
            return(-intfromstring(string,n+1,false,&n));
        }
        if (48<=(int)string[n] && (int)string[n]<=57)
        {
            return(intfromstring(string,n,false,&n));
        }
        n+=1;

    }
    return(0);

}

//exo 15


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
    int tab[]={5,3,6,7,1,2};
    printf("ecart minimum entre deux elements consecutifs de tab : %d \n",ecart_min(tab,6));

    printf("\n[exo 14] \n");
    printf("le premier entier dans la chaine \"lorem ipsum 42\" est : %d",extraire("lorem ipsum 42"));

    return(0);
}