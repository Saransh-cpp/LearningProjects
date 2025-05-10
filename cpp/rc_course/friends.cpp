#include <iostream>

// forward definition
class Complex;

// either make the entire class friend or make addReal friend
class Calc {
    public:
        // can only declare here as n.a requires Complex to be defined completely
        inline float addReal(Complex n, Complex m);
};

class Complex {
    float a, b;
    public:
        Complex () {};
        Complex(float a, float b) : a(a), b(b) {};
        // not in the scope of the class
        // can be in private too, can never access private member by their name - only through object
        friend Complex sumComplex(Complex, Complex);
        friend float Calc :: addReal(Complex, Complex);
        inline void printNum() {std::cout << a << " + " << b << "i" << std::endl;}
};

inline float Calc :: addReal(Complex n, Complex m) {return n.a + m.a;}

inline Complex sumComplex (Complex num1, Complex num2) {return Complex(num1.a + num2.a, num1.b + num2.b);}


int main () {
    Complex num1, num2, sum;
    num1 = Complex(1, 2);
    num2 = Complex(3, 4);
    sum = sumComplex(num1, num2);
    sum.printNum();
    return 0;
}
