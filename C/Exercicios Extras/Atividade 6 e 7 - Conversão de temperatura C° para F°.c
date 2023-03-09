/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    float temperatura, tmpC, tmpF;
    char tmp = 'a';
    
    printf("Digite a temperatura: ");
    scanf("%f", &temperatura);
    
    printf("Você digitou a temperatura em C° ou em F°? (C ou F) ");
    scanf(" %c", &tmp);
    
    if(tmp == 'C'){
        printf("Você digitou a temperatura em Graus Celsius!\n");
        tmpF = (temperatura * 1.8) + 32;
        printf("A conversão de C° para F°: %.2f", tmpF);
    }
    
    if(tmp == 'F'){
        printf("Você digitou a temperatura em graus fahrenheit!\n");
        tmpC = (temperatura - 32) / 1.8;
        printf("A conversão de F° para C°: %.2f", tmpC);
    }
}
