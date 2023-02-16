/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    double area, pi, raio;
    pi = 3.14159;
    scanf("%lf", &raio);
    
    area = (pi*(raio*raio));
    printf("A=%.4lf\n", area);
}