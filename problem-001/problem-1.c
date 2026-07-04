#include <stdio.h>

int sum = 0;

int counter;

int main() {
    for(counter=1; (counter*3)<1000; counter=counter+1) {
        if ((counter*3)%5!=0) {
            sum = sum + (counter*3);
        };
    };
    for(counter=1; (counter*5)<1000; counter=counter+1) {
        sum = sum + (counter*5);
    }
    printf("%d\n", sum);

    //better solution
    sum = 0;
    for(counter=1; counter<1000; counter=counter+1) {
        if (counter%3==0 || counter%5==0) {
            sum = sum + counter;
        }
    }
    printf("%d\n", sum);
};


