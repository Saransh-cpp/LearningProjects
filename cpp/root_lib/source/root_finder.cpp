#include <iostream>
#include <vector>
#include <exception>
#include <string>
#include <cmath>
#include "root_finder.hpp"


RootFinder::RootFinder(const std::vector<float> coeffs) {
    coefficients.reserve(10);
    coefficients = coeffs;
}

float RootFinder::f(float val) {
    if (coefficients.empty()) return 0;

    float f_val = 0;
    int i = coefficients.size() - 1;
    for (auto coeff : coefficients) {
        f_val += coeff * std::pow(val, i);
        i--;
    }

    return f_val;
}

float RootFinder::bisection(float a, float b, float tol) {
    if (!(a < b)) {
        std::string msg = "a must be less than b, got a = " + std::to_string(a) + ", b = " + std::to_string(b);
        throw std::invalid_argument(msg);
    }
    if (f(a) * f(b) >= 0) throw std::invalid_argument(std::string("f(a) and f(b) must have opposite signs"));

    float c = a;
	while ((b - a) >= tol) {
		c = (a + b) / 2;
		
        if (f(c) == 0.0) return c;
		else if (f(c) * f(a) < 0) b = c;
		else a = c;
	}

    return c;
}

