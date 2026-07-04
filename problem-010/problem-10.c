#include <stdio.h>
#include <math.h>

long long m = 2000000, s = 0, i = 2, k = 2, c = 0;

int main() {
    while (i<m) {
        for (k=2; k<=sqrt(i); k++) {
            if ((i%k) == 0) {
                c = 1;
            }
        }
        if (c == 0) {
            s += i;
        }
        i++;
        c=0;
    }
    printf("%lld", s);
}