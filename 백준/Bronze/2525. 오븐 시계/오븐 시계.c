#include <stdio.h>


int main(){
    int hour, minute, cooking_time;

    scanf("%d %d %d", &hour, &minute, &cooking_time);
    
    // cooking time을 60으로 나눈 몫과 나머지를 알아야 한다.
    
    int quotient = cooking_time / 60;
    int remainder = cooking_time % 60; // 0 <= remainder <= 59
    
    //printf("%d %d", quotient, remainder);
    
    hour += quotient;
    minute += remainder;
    
    if (minute > 59) {
        hour += minute / 60;
        minute = minute % 60;
    }
    
    if (hour > 23 && hour % 24 != 0){
            hour = hour - 24;
    }
    else if (hour % 24 == 0)
        hour = 0;
    
    printf("%d %d", hour, minute);

    return 0;
}
