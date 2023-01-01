#include <stdio.h>

int is_leap_year(int y);

int main(){
    int a;
    
    //printf("input a year\n");
    scanf("%d", &a);
    printf("%d\n", is_leap_year(a));
    
    
    return 0;
}

int is_leap_year(int y){
    // 4의 배수 && 400의 배수 => 1
    // 4의 배수 && 100의 배수 !(400의 배수) => 0
    // !(4의 배수) => 0
    
    if (y % 4 == 0){
        if ((y % 400 == 0))
            return 1;// 4로 나눠지고 400으로도 나눠지는 경우
        else if (y % 100 == 0)
            return 0;// 4로 나눠지고 400으로는 안 나눠지고 100으로는 나눠지는 경우
        else
            return 1; // 4로 나눠지는데 100으로도 안 나눠지고, 400으로도 안 나눠지는 경우
    }
    return 0; // 4의 배수가 아닌 경우
}
