#include <stdio.h>
int main(){
    
    
    
    int a, b;
    
    int a1, a2, a3;
    int b1, b2, b3;
    
    scanf("%d %d", &a, &b);
    
    a1 = a%10;
    a2 = (a%100) - a1;
    a3 = a - a2 - a1;
    
    b1 = b%10;
    b2 = (b%100) - b1;
    b3 = b - b2 -b1;
    
    
    printf("%d\n", (b1*a1+b1*a2+b1*a3));
    printf("%d\n", (b2*a1+b2*a2+b2*a3)/10);
    printf("%d\n",(b3*a1+b3*a2+b3*a3)/100);
    printf("%d\n",(b1*a1+b1*a2+b1*a3+b2*a1+b2*a2+b2*a3+b3*a1+b3*a2+b3*a3));
    
    //코드가 마음에 들지는 않지만, 작동은 잘 된다.
    
    return 0;
}
