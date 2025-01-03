#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//gamma1 : 
int findstr(char** tabc, int size)
{
	int imax = -1;
	int maxlen = 0;
	for (int i=0; i<size; i+=1)
	{
		int l = strlen(tabc[i]);
		if (l > maxlen)
		{
			bool check = true;
			for (int j=1; j<l; j+=1) check = check && tabc[i][j]>=tabc[i][j-1];
			if (check) 
			{
				imax = i;
				maxlen = l;
			}
		}
	}
	return imax;
}

//gamma2 :
int* countsort(int* tab, int size)
{
	int* auxtab = malloc(size*sizeof(int*));
	for (int i=0; i<size; i+=1)
	{
		auxtab[i] = 0;
	}
	for (int i=0; i<size; i+=1)
	{
		auxtab[tab[i]]+=1;
	}
    int k=0;
    for (int i=0; i<size; i+=1)
    {
        for (int j=0; j<auxtab[i];j+=1)
        {
            tab[k]=i;
            k+=1;
        }
    }
    free(auxtab);
    return tab;
}

int main()
{
    char* tabstr[4] = {"zae","abc","abcd","dqhfkj"};
    int tabint[7] = {3,6,5,2,3,5,6};
    printf("%d \n",findstr(tabstr,4));
    int* newtab = countsort(tabint,7);
    for (int i=0; i<7;i+=1) printf("%d ",newtab[i]);
    exit(0);
}
