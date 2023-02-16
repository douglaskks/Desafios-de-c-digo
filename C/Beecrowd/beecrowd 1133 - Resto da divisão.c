/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>


int main () {
int X, Y, count, soma;
scanf("%d %d", &X, &Y);

if (X > Y){
   soma = X;
   X = Y;
   Y = soma;
}

for (count = X + 1; count < Y; count++){
  if (count % 5 == 2 || count % 5 == 3){
    printf("%d\n", count);
        }
    }
}