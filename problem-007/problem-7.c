#include <stdio.h>
#include <math.h>

int k = 0;
int f = 0;

long long i = 2;
long long x = 2;

int main() {
    while(k<10001) {
        while(x<=sqrt(i)){
            if((i%x)==0) {
                f=1;
                break;
            }
            x+=1;
        }
        if (f==0) {
            k+=1;
            printf("%lld | %d\n", i, k);
        }
        i+=1;
        f=0;
        x=2;
    }
}
