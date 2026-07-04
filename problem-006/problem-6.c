#include <stdio.h>

long sum_squares = 0;
long square_sum = 0;
long count;

int main() {
    for(count=1; count<101; count+=1){
        sum_squares = sum_squares + (count * count);
        square_sum = square_sum + count;
    }
    square_sum = square_sum*square_sum;
    long output = sum_squares - square_sum;
    printf("%ld", output);
}
