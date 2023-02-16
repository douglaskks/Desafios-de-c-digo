/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

/*Leia um numero real e imprima a quinta parte de numero*/

int
main ()
{
  double numero, divisao;
  printf("Digite o valor a ver a quinta parte: ");
  scanf("%lf", &numero);
  
  divisao = numero / 5;
  
  printf("A quinta parte de %.2lf e %.2lf", numero, divisao);
  
}
