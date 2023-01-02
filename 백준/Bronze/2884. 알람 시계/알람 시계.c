#include <stdio.h>

int get45mins_back(int h, int m);

int main(){
    int hour, minute;
    
    scanf("%d %d", &hour, &minute);
    
    if (minute >= 45)
        printf("%d %d", hour, minute - 45);
    else if ((minute < 45) && ( hour == 0))
        printf("%d %d", 23, 60 - (45 - minute));
    else
        printf("%d %d", hour - 1, 60 - (45 - minute));
    

    return 0;
}
