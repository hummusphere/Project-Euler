#include <stdio.h>

long sum = 0;
int fib1 = 0;
int fib2 = 1;
int placeholder;

int main() {
    while (fib2 < 4000000) {
        placeholder = fib1 + fib2;
        fib1 = fib2;
        fib2 = placeholder;
        if (fib2%2==0) {
            sum = sum + fib2;
        }
    }
    printf("%ld", sum);
}