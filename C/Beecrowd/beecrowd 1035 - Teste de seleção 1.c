/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int A, B, C, D;
    
    scanf("%d%d%d%d", &A, &B, &C, &D);
    
    if ((B > C && D > A) && (C + D > A + B) && (C >= 0) && (D >= 0) && (A % 2 == 0)){
        printf("Valores aceitos\n");
    }else{
        printf("Valores nao aceitos\n");
    }
}
