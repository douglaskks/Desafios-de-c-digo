/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    double x, y;
    scanf("%lf %lf", &x, &y);
    
    if(x > 0 && y > 0){
        printf("Q1\n");
    }else if(x == 0 && y != 0){
        printf("Eixo Y\n");
    }else if(x != 0 && y == 0){
        printf("Eixo X\n");
    }else if(x < 0 && y > 0){
        printf("Q2\n");
    }else if(x < 0 && y < 0){
        printf("Q3\n");
    }else if(x > 0 && y < 0){
        printf("Q4\n");
    }else if(x == 0 && y == 0){
        printf("Origem\n");
    }
}