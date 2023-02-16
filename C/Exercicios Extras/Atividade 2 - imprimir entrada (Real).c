/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

/*FaC'a um programa que leia um número Real e o imprima*/

int
main ()
{
  float n;
  printf ("Digite um numero inteiro: ");
  scanf ("%f", &n);

  printf ("%.2f", n);

  return 0;
}
