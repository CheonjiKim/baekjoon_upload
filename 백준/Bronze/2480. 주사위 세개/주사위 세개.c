#include <stdio.h>

int max_num(int a, int b, int c);

int main(){
    int a, b, c;
    
    
    
    scanf("%d %d %d", &a, &b, &c);
    
    if (a == b && b == c)
        printf("%d", 10000 + (a * 1000));
    else if (a == b)
        printf("%d", 1000 + (a * 100));
    else if (b == c)
        printf("%d", 1000 + (b * 100));
    else if (c == a)
        printf("%d", 1000 + (c * 100));
    else
        printf("%d", max_num(a, b, c) * 100);
    
    return 0;
}

int max_num(int a, int b, int c){
    int temp;
    if (a >= b)
        temp = a;
    else
        temp = b;
    
    if (temp >= c)
        return temp;
    else
        return c;
        
}