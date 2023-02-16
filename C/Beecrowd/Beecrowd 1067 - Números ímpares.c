/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int X, count;
    scanf("%d", &X);
    
    for(count = 0; count <= X; count++){
        if(count % 2 != 0){
            printf("%d\n", count);
    }
  }
}