#include <iostream>
#include <vector>
#include "root_finder.hpp"

int main() {
    std::vector<float> coeffs = {1, 0, 0, 0};
    RootFinder rf = RootFinder(coeffs);
    float sol = rf.bisection(-1, 9);
    std::cout << sol << " " << rf.get_fval(sol) << std::endl;
    return 0;
}
