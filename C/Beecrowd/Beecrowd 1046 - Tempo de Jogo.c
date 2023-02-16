/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
 int hourI, hourF, count = 0;
 scanf("%d %d", &hourI, &hourF);
 do{
     hourI++;
     count++;
     if(hourI==24){
         hourI = 0;
     }
 }while(hourI!=hourF);
 printf("O JOGO DUROU %d HORA(S)\n", count);
}