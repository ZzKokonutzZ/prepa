#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    for (int index = 0; index < argc; index++)
    {
        printf("%s\n", argv[index]);
    }
    exit(0);
}