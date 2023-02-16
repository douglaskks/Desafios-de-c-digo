/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    double nota1, nota2;
    scanf("%lf", &nota1);
    
    while(nota1 < 0 | nota1 > 10){
        printf("nota invalida\n");
        scanf("%lf\n", &nota1);
    }
    
    scanf("%lf", &nota2);
    while(nota2 < 0 | nota2 > 10){
        printf("nota invalida\n");
        scanf("%lf\n", &nota2);
    }
    
    double media = nota1 + nota2;
    double M = media / 2;
    
    printf("media = %.2lf\n", M);
}
