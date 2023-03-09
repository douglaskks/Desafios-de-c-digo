/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main (){
 
 int firstV, secondV;
 int contador = 0;
 int contador1 = 1;
 int novaV = 5;
 int outraV = 7;
 
while(contador <= 4){
    
    for(firstV = outraV; firstV >= novaV; firstV -= 1){
     printf("I=%d ", contador1);
     printf("J=%d\n", firstV);
    }
    contador++;
    contador1+=2;
    firstV+=2;
    outraV+=2;
    novaV+=2;
}
 
}