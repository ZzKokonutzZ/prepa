#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

struct Personnage { char nom[80]; int pv; int atq; int def; };
typedef struct Personnage personnage;

//exo 1
personnage pythagore={.nom="Pythagore",.pv=25,.atq=50,.def=10};
personnage thales={.nom="Thales",.pv=25,.atq=10,.def=50};

//exo 2
void stats(personnage perso)
{
    printf("nom : %s \n",perso.nom);
    printf("PV : %d \n",perso.pv);
    printf("attaque : %d \n",perso.atq);
    printf("defense : %d \n",perso.def);
    printf("\n");
}

//exo 3
int max(int a, int b)
{
    if (a>b) return(a);
    return(b);
}
void attaque(personnage *perso1,personnage *perso2)
{
    (*perso2).pv=max(0 , (*perso2).pv-max(1,(*perso1).atq-(*perso2).def));
}

//exo 4
void combat(personnage *perso1,personnage *perso2)
{
    while((*perso1).pv>0 && (*perso2).pv>0)
    {
        attaque(perso1,perso2);
        if ((*perso2).pv>0)
        {
        attaque(perso2,perso1);
        }
    }
}

//exo 5
personnage physiciens[3]={{.nom="Hawking",.pv=40,.atq=50,.def=20},{.nom="Einstein",.pv=50,.atq=40,.def=30},{.nom="Newton",.pv=50,.atq=25,.def=25}};
personnage mathematiciens[3]={{.nom="Euler",.pv=50,.atq=20,.def=40},{.nom="Euclide",.pv=50,.atq=15,.def=50},{.nom="Poincare",.pv=50,.atq=30,.def=25}};

//exo 6
void stats_tab(personnage tab[],int size)
{
    for (int i=0;i<size;i+=1)
    {
        stats(tab[i]);
    }
}

//exo 7
void guerre(personnage **tab1,int size1, personnage **tab2, int size2)
{
    int i=0;
    int ii=0;
    while (i<size1 && ii<size2)
    {
        combat(tab1[i],tab2[ii]);
        if ((*tab1[i]).pv==0) 
        {
            printf("%s a vaincu %s \n",(*tab2[ii]).nom,(*tab1[i]).nom);
            i+=1;
        }
        else
        {
            printf("%s a vaincu %s \n",(*tab1[i]).nom,(*tab2[ii]).nom);
            ii+=1;
        }
    }
    if (i==3)
    {
        printf("victoire pour l'equipe de %s",(*tab2[ii]).nom);
    }
    else
    {
        printf("victoire pour l'equipe de %s \n",(*tab1[i]).nom);
    }
}

struct day { int annee; int mois; int jour; int jdls; };
typedef struct day date;

//exo 8
date anniversaire={.annee=2007,.mois=6,.jour=27};

//exo 9
void print_date(date d,bool jdls)
{
    if (jdls)
    {
        char tab_jdls[7][25]={"Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"};
        printf("%s ",tab_jdls[d.jdls-1]);
    }
    char tab_mois[12][25]={"Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"};
    printf("%d %s %d \n",d.jour,tab_mois[d.mois-1],d.annee);
}

int main()
{
    stats(pythagore);
    stats(thales);

    printf("Pythagore attaque Thales \n");
    attaque(&pythagore,&thales);
    stats(pythagore);
    stats(thales);

    printf("Thales repond ! le combat s'engage \n");
    combat(&pythagore,&thales);
    stats(pythagore);
    stats(thales);

    stats_tab(physiciens,3);
    stats_tab(mathematiciens,3);

    personnage *phy_p[3];
    personnage *math_p[3];
    for (int i=0;i<3;i+=1)
    {
        phy_p[i]=&physiciens[i];
        math_p[i]=&mathematiciens[i];
    }

    guerre(math_p,3,phy_p,3);
    
    
    print_date(anniversaire, false);

    return(0);
}