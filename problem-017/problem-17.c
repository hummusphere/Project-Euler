#include <stdio.h>

int m=1000, s=0, i;
int ones[] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
int teens[] = {0, 6, 6, 8, 8, 7, 7, 9, 8, 8};
int tens[] = {0, 3, 6, 6, 5, 5, 5, 7, 6, 6};

int main() {
    for (i=1; i<=m; i++) {
        if (i<10) {
            s+=ones[i];
        } else if (i==10) {
            s+=tens[i/10];
        } else if (i > 10 && i < 20) {
            s+=teens[i%10];
        } else if (i > 19 && i < 100) {
            s+=tens[i/10];
            s+=ones[i%10];
        } else if (i > 99 && i < 1000) {
            int k = s;
            s+=ones[i/100];
            if (i%100 != 0) {s+=10;} else {s+=7;}
            if (i-((i/100)*100) > 10 && i-((i/100)*100) < 20) {
                s+=teens[(i-((i/100)*100))%10];
            } else {
                s+=tens[(i-((i/100)*100))/10];
                s+=ones[i-((i/10)*10)];
            }
        } else if (i==1000) {
            s+=11;
        }
    }
    printf("%d", s); 
}