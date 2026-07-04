#include <stdio.h>

int io = 1;
int num = 2520;
int count;

int main() {
    while (io==1) {
        num+=1;
        for(count=20; count>1; count-=1) {
            if(num%count!=0) {
                break;
            } else if (count==2) {
                io=0;
            }
        }
    }
    printf("%d", num);
}