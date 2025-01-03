#include <stdio.h>
#include <stdlib.h>
struct t_r_i {int taille; int capacite; int* donnees;};
typedef struct t_r_i itr;
itr creer_itr(int capacite)
{
    itr rep;
    rep.capacite=capacite;
    rep.taille=0;
    rep.donnees=malloc(capacite*sizeof(int));
    return rep;
}

int taille(itr t) 
{
    return t.taille;
}

int access_itr(itr t, int i)
{
    if (i>=t.taille) exit(1);
    else return t.donnees[i];
}

void modif_itr(itr t, int i, int x)
{
    if (i>=t.taille) exit(1);
    else t.donnees[i]=x;
}

void append_itr(itr* t, int x)
{
    if ((*t).taille+1<=(*t).taille) 
    {
        (*t).donnees[(*t).taille]=x;
        (*t).taille+=1;
    }
    else 
    {
        int size=taille(*t);
        int* newtab=malloc(2*size*sizeof(int));
        for (int i=0;i<size;i+=1)
        {
            newtab[i]=(*t).donnees[i];
        }
        newtab[size]=x;
        free(t->donnees);
        t->donnees=newtab;
        t->taille=size+1;
        t->capacite=2*t->capacite;
    }
}

int main()
{
    itr tab=creer_itr(1);
    append_itr(&tab,1);
    append_itr(&tab,2);
    for (int i=0;i<taille(tab);i+=1) printf("%d",tab.donnees[i]);
    exit(0);
}




