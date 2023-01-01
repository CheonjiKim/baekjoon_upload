#include <stdio.h>



int main(){
    int x, y;
    
// 두 값의 곱이 0보다 큰지 작은지를 비교
    
    scanf("%d %d", &x, &y);
    if (x * y > 0 && y > 0)
        printf("1");
    else if (x * y > 0 && y < 0)
        printf("3");
        
    if (x * y < 0 && y > 0)
        printf("2");
    else if (x * y < 0 && y < 0)
        printf("4");
    
    return 0;
}