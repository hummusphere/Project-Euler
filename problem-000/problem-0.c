#include <stdio.h>

// init varibles
const int odd_squares = 666000;
long long counter;
long long sum = 0;

int main() {
    for(counter=1; counter<odd_squares; counter=counter+2){
        sum = sum + (counter * counter);
    }
    printf("%lld", sum);
};