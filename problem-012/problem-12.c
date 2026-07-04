#include <stdio.h>
#include <math.h>

int k=1, s=0, c=1, i=1, j=0; 

int main() {
    while (c) {
        s+=k;
        for (i=1; i<=sqrt(s); i++) {
            if (s%i==0){j+=2;}
        }
        if (j>=500) {printf("%d | %d \n", s, j); c=0;}
        j=0;
        k++;
    }
}