/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main (){
    
    int N, count, count1, otherV;
    int add = 0;
    scanf("%d", &N);
    
    for(count = 1; count <= N; count++){
        int X, Y;
        scanf("%d%d", &X, &Y);
        
        if(X > Y){
            for(count1 = Y+1; count1 < X; count1++){
                if(count1 % 2 != 0){
                add+=count1;
                }
            }
            printf("%d\n", add);
            add = 0;
        }else{
            for(count1 = X+1; count1 < Y; count1++){
                if(count1 % 2 != 0){
                    add+=count1;
                }
            }
            printf("%d\n", add);
            add = 0;
        }
    }
}