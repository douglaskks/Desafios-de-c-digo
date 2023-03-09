/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main (){
 
 int firstV;
 int contador = 0;
 int contador1 = 1;
 
while(contador <= 4){
    
    for(firstV = 7; firstV >= 5; firstV -= 1){
     printf("I=%d ", contador1);
     printf("J=%d\n", firstV);
    }
    contador++;
    contador1+=2;
  }
}