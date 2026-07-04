#include <stdio.h>
#include <math.h>

float i = 0, k = 0;
int max = 1000;

int main() {
    while (i<max) {
        while (k<max) {
            float c = sqrt((i*i) + (k*k));
            if (c+k+i == max && c!=k && c!=i) {printf("%f\n", c*i*k);}
            k++;
        }
        i++;
        k=0;
    }
}