#include <iostream>
#include <benchmark/benchmark.h>
#include <random>
#include <vector>


static void baseline(benchmark::State& state) {
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_real_distribution<> dist(0.0, 1.0);

    const int num_elements = 1 << 20;
    std::vector<float> v_in[num_elements];
    // float myarray[num_elements];
    std::generate_n(v_in, num_elements, [&]{return dist(mt);});

}

BENCHMARK(baseline);
// Run the benchmark
BENCHMARK_MAIN();
