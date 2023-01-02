#include <stdio.h>

int main(){
    int a, b;
    
    scanf("%d %d", &a, &b);
    
    if(a == 0 && b == 0)
        return 0;
    
    else{
        printf("%d\n", a+b);
        while(a != 0 && b != 0){
            scanf("%d %d", &a, &b);
            if(a == 0 && b == 0)
                return 0;
            else
                printf("%d\n", a+b);
        }
        
        
        return 0;
    }
}