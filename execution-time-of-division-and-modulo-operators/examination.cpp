// execution time: %100/10 < /10%100 < /10%10 < %10/10


#include <cstdio>
#include <cmath>
#include <ctime>
#define EPOCH 100


int main() {
    puts("          [/ 10 % 100] [/ 10 % 10]");
    double times[EPOCH][2] = {};
    clock_t tStart, tFinish;
    int tmp;
    unsigned i;
    double avg[2] = {};
    for (int n = 0; n < EPOCH; ++n) {
        // Participant 1.
        tStart = clock();
        for (i = 1; i > 0; ++i)
            tmp = i / 10 % 100;
        tFinish = clock();

        times[n][0] = double(tFinish - tStart) / CLOCKS_PER_SEC;
        avg[0]      += times[n][0];

        // Participant 2.
        tStart = clock();
        for (i = 1; i > 0; ++i)
            tmp = i / 10 % 10;
        tFinish = clock();

        times[n][1] = double(tFinish - tStart) / CLOCKS_PER_SEC;
        avg[1]      += times[n][1];

        // Show results in this round.
        printf("%3d) Consume: %8.4lf %8.4lf (secs)   %c\n", n+1, times[n][0], times[n][1], (times[n][0] < times[n][1]) ? 'v' : ' ');
    }
    avg[0] /= EPOCH;
    avg[1] /= EPOCH;

    double var[2] = {};
    for (int n = 0; n < EPOCH; ++n) {
        var[0] += pow(times[n][0] - avg[0], 2);
        var[1] += pow(times[n][1] - avg[1], 2);
    }
    var[0] /= (EPOCH - 1);
    var[1] /= (EPOCH - 1);

    printf("Avg:          %8.4lf %8.4lf\n", avg[0], avg[1]);
    printf("Var:          %8.4lf %8.4lf\n", var[0], var[1]);
}
