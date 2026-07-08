#include <stdio.h>

const int grid = 20;

long long binomial_distribution(int f, int o) {
    long long j=1;
    for (int i=1; i<=o; i++) {
        j = (j * (f - o + i))/i;
    }
    return j;
}

int main() {
    const long long possible = binomial_distribution(grid*2, grid);
    printf("%lld", possible);
}