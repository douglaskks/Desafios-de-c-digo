/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    double A, B, C;
    double pTriangulo, aTrapezio;
    scanf("%lf%lf%lf", &A, &B, &C);
    
    if((A < B + C) && (B < A + C) && (C < A + B)){
        pTriangulo = A + B + C;
        printf("Perimetro = %.1lf\n", pTriangulo);
    }else{
    
        aTrapezio = ((A + B)*C) / 2;
        
        printf("Area = %.1lf\n", aTrapezio);
    }
    
}
