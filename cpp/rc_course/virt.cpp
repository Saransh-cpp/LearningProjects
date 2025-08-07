#include<iostream>
#include<string>
using std::string;


class Calc {
    public:
        virtual int add(int x, int y) {return x + y;}
};

class Str : public Calc {
    public:
        int add(int x, int y) {return x;}
};

int main () {
    Calc* c;
    Str s;
    c = &s;
    std::cout << c->add(1, 2);
    return 0;
}