#include <stdio.h>
#include <math.h>

const long long num = 600851475143;
long long counter;
long long second_counter;

int main() {
    for(counter=2; counter < sqrt(num); counter+=1){
        if (num%counter==0) {

            printf("%lld", counter);
            for(second_counter=2; second_counter < sqrt(counter); second_counter+=1) {
                if (counter%second_counter==0) {
                    printf(" is not a prime\n");
                    break;
                }
            }
            printf("\n");
            printf("%lld", num/counter);
            for(second_counter=2; second_counter < sqrt(num/counter); second_counter+=1) {
                if ((num/counter)%second_counter==0) {
                    printf(" is not a prime\n");
                    break;
                }
            }
            printf("\n");
        }
    }
};