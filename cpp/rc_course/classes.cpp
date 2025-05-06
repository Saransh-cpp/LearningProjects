#include <iostream>
#include <array>
#include "ball.hpp"

class Mine {
    public:
    int x;
    double y;

    private:
    std::string name;

    protected:
    double z;
};


class Counter {
    public:
    Counter() {
        count += 1;
    }
    ~Counter() {
        count -= 1;
    }
    // static int count;
    static int getCount() {
        return count;
    }
    private:
    static int count;
};

int Counter::count = 0;

// class Ball {
//     public:
//     Ball(std::array<double, 3> p, double r, double m): radius(r), mass(m), position(p) {
//         // radius = r;
//         // mass = m;
//         // position = p;
//         setDensity();
//     }
//     std::array<double, 3> position;
//     double getRadius() { return radius; }
//     double getMass() { return mass; }
//     double getDensity() { return density; }
//     void setMass(double m) {
//         mass = m;
//         setDensity();
//     }
//     double setRadius(double r) {
//         radius = r;
//         setDensity();
//     }

//     private:
//     void setDensity()
//     {
//         density =  3 * mass / (4 * M_PI * pow(radius, 3));
//     }
//     double radius;
//     double mass;
//     double density;
// };

// constructor definition
// Ball:: tells us that the function Ball(...) is part of the Ball class
Ball::Ball(std::array<double, 3> p, double r, double m): position(p), radius(r), mass(m)
{
    setDensity();
}

// Again, Ball:: tells us that this function is part of the Ball class definition
// Because this is a member function, it has access to all the data members of this class.
void Ball::setDensity()
{
    density =  3 * mass / (4 * M_PI * pow(radius, 3));
}

int main() {
    // Counter c = Counter();
    // std::cout << Counter::count << std::endl;

    // Counter c2 = Counter();
    // std::cout << c2.count << std::endl;

    // Counter c = Counter();
    // std::cout << Counter::getCount() << std::endl;

    // Counter c2 = Counter();
    // std::cout << c2.getCount() << std::endl;
    
    return 0;
}
