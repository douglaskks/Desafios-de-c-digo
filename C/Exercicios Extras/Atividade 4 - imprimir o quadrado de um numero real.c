/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

/*Leia um numero real e mostre o quadrado do numero digitado*/

int
main ()
{
  double n, qua;
  printf("Digite um numero real: ");
  scanf("%lf", &n);
  
  qua = n*n;
  
  printf("%.2lf", qua);

  return 0;
}
