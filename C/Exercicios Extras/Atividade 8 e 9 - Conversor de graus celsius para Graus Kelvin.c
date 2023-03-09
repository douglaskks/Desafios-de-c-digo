/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    float temperatura, tmpK, tmpC;
    char tmp = 'a';
    
    printf("Digite a temperatura: ");
    scanf("%f", &temperatura);
    
    printf("Você digitou a temperatura em K° ou em C°? (K ou C) ");
    scanf(" %c", &tmp);
    
    if(tmp == 'K'){
        printf("Você digitou a temperatura em Graus Kelvin!\n");
        tmpK = temperatura - 273;
        printf("A conversão de K° para C°: %.2f Graus Celsius", tmpK);
    }
    
    if(tmp == 'C'){
        printf("Você digitou a temperatura em Graus Celsius!\n");
        tmpC = temperatura + 273;
        printf("A conversão de C° para K°: %.2f Graus Kelvin", tmpC);
    }
}
