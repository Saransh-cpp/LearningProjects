#include <iostream>

using namespace std;

class Obj
{
    public:
    int a, b, c, d, e, f, g, h;

    Obj(int a, int b, int c, int d, int e, int f, int g, int h) : a(a), b(b), c(c), d(d), e(e), f(f), g(g), h(h) {}
};

Obj makeObj()
{
    Obj myObj(1, 2, 3, 4, 5, 6, 7, 8);
    cout << "In makeObj, myObj is at address " << &myObj << endl;
    cout << "myObj.a is at " << &myObj.a << endl;
    cout << "myObj.b is at " << &myObj.b << endl;
    return myObj;
}

int makeInt()
{
    int x = 5;
    cout << "In makeInt, x is at address " << &x << endl;
    return x;
}

int main() {

    // int x = 15;
    // std::cout << &x << std::endl;
    // x++;
    // std::cout << &x << std::endl;

    Obj newObj = makeObj();
    cout << "Outside the function, newObj is at address " << &newObj << endl;
    cout << "newObj.a is at " << &newObj.a << endl;
    cout << "newObj.b is at " << &newObj.b << endl;

    int y = makeInt();
    cout << "Outside the function, y is at address " << &y << endl;

    return 0;
}
