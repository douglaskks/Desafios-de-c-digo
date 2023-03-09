/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main (){
 
 int firstV;
 int secondV = 1;
 
 for(firstV = 60; firstV >= 0; firstV -= 5){
     printf("I=%d ", secondV);
     secondV = secondV + 3;
     printf("J=%d\n", firstV);
 }
}
