#include<iostream>
#include<omp.h>
#include<math.h>

using namespace std;

int main(int argc, char* argv[]) {

    // #pragma omp parallel
    // {
    //     cout << omp_get_thread_num() << " " << endl;
    // }

    // #pragma omp parallel
    // {
    //     #pragma omp critical  // no race condition
    //     {
    //         cout << omp_get_thread_num() << " " << endl; 
    //     }
    // }

    // set number of threads using OMP_NUM_THREADS env variable

    // shared and private memory
    // int x = 0;  // shared memory
    // #pragma omp parallel private(x)  // do this to make it private or put it inside
    // #pragma omp parallel
    // {
    //     int x = omp_get_thread_num(); // private to each thread
    //     #pragma omp critical  // no race condition
    //     {
    //         cout << x << " " << endl; 
    //     }
    // }

    // #pragma omp parallel
    // {
    //     int x = omp_get_thread_num(); // private to each thread
    //     #pragma omp master  // 0th thread
    //     {
    //         cout << x << " " << endl; 
    //     }
    // }

    int N = stoi(argv[1]);

    double sum = 0;  // shared
    double start = omp_get_wtime();
    #pragma omp parallel
    {
        // double loc_sum = 0;  // could do this
        #pragma omp for reduction(+:sum)
        for (size_t i = 0; i < N; i++)
        {
            sum += sin(M_PI*double(i)/N);
        }
        // sum += loc_sum;  // could do this
    }
    double end = omp_get_wtime(); 
    cout.precision(15);
    cout << M_PI*sum/N << " " << end - start << endl;

    return 0;
}
