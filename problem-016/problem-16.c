#include <stdio.h>

char num[350] = {};
int i, x, j, z=0, m=1000;

int main() {
    num[0] = '2';
    int s = 1;
    for (i=1;i<m; i++) {
        for(x=s-1; x>=0; x--) {
            int k = num[x]-'0';
            k = (k * 2)+z;
            z=0;
            if (k > 9) {
                k = k%10;
                num[x] = k+'0';
                z=1;
                if (x==0) {
                    for (j = s+1; j>=0; j--) {
                        num[j+1] = num[j];
                    }
                    s++;
                    x++;
                    num[0]=0+'0';
                }
            } else {
                num[x] = k+'0';
            }
        }
    }
    int sum = 0;
    for (i=0; i<s; i++) {
        sum += num[i]-'0';
    }
    printf("%d", sum);
}