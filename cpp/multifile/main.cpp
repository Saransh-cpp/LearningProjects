// g++ -o test_f main.cpp func.cpp -Iinclude/
#include <iostream>
#include "func.hpp"

int main()
{
    // Call function f
    int x = add(5, 2);
    
    std::cout << "x = " << x << std::endl; // endl stands for end line
    
    return 0;
}

// template<typename T>
// T add(T x, T y) {return x + y;}
