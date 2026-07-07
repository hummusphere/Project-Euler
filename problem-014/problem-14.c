#include <stdio.h>

long long m = 1000000, h = 0, mh = 0, i, k, j;

int main() {
    for (i = 1; i <= m; i++) {
        k=i;
        j=0;
        for (;;) {
            j++;
            if (k==1) {
                break;
            } else if (k%2==0) {
                k=k/2;
            } else {
                k=(k*3)+1;
            }
        }
        if (j>h) {
            h=j;
            mh = i;
        }
    }
    printf("\n\n%lld\n", mh);
}