/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

/*Faca um programa que receba 3 numeros inteiros e mostre a soma deles no final*/

int
main ()
{
  int n, n2, n3, soma;
  printf ("Digite um numero inteiro: ");
  scanf ("%d", &n);
  
  printf ("Digite outro numero inteiro: ");
  scanf ("%d", &n2);
  
  printf ("Digite o ultimo numero inteiro: ");
  scanf ("%d", &n3);
  
  soma = n + n2 + n3;

  printf ("A soma dos 3 numeros e %d", soma);

  return 0;
}
