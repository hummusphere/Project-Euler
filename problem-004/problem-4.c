#include <stdio.h>

long mult_one, mult_two;
long biggest = 0;

int main() {
    for(mult_one=100; mult_one<1000; mult_one+=1){
        for(mult_two=100; mult_two<1000; mult_two+=1) {
            long mult = mult_one*mult_two;
            long remainder = 0;
            long reversed = 0;
            while (mult!=0){
                remainder = mult % 10;
                reversed = (reversed * 10) + remainder;
                mult /= 10;
            }
            if (mult_one*mult_two == reversed) {
                if (mult_one*mult_two > biggest) {
                    biggest = mult_one*mult_two;
                }
            }
        }
    }
    printf("%ld\n", biggest);
}