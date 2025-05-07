#include <vector>

class RootFinder {
    std::vector<float> coefficients;
    float f(float val);
    public:
        RootFinder(const std::vector<float> coeffs);

        float get_fval(float val) {return f(val);}
        std::vector<float> get_coefficients() {return coefficients;}
    
        // TODO: add verbose output support
        float bisection(float a, float b, float tol = 1e-6);
        float iterative();
        float newton_raphson();
        float secant();
};
