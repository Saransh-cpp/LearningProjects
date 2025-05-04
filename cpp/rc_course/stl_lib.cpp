#include <iostream>
// using namespace std;
using std::cout;


bool isEven(int x)
{
    return x % 2 == 0;
}

int main() {
    typedef std::vector<std::vector<int>> IntMatrix; 

    std::vector<int> a = {1, 2, 3, 4};
    std::vector<int> b = {5, 6, 7, 8};
    std::vector<int> c(4); // create a vector with size 4

    // size_t is an unsigned (cannot be negative) integral numerical type which is often used for the sizes of objects
    // The max value of size_t is large enough for the largest objects that can be stored in memory
    // for(size_t i = 0; i < 4; i++)
    // {
    //     c.at(i) = a.at(i) + b.at(i);
    // }

    // std::vector<int> myNums = {1, 6, 5, 8, 3, 5, 4, 2, 8, 9, 9, 7, 6};
    // int numEvens = std::count_if(myNums.begin(), myNums.end(), &isEven);
    // std::cout << "num evens = " << numEvens << std::endl; 

    // int numEvens = std::count_if(myNums.begin(), myNums.end(), [](int x){return x%2 == 0;});
    // std::cout << "num evens = " << numEvens << std::endl; 

    // auto isEven = [](int x){return x%2 == 0;};
    // auto isEven = [](int x) -> bool {return x%2 == 0;};

    // int n = getSomeNumber();  // Don't know the number n at compile time
    // int numDivisibleN = std::count_if(myNums.begin(), myNums.end(), [n](int x){return x%n == 0;});
    // std::cout << "Number divisible by n = " << numDivisibleN << std::endl;
    return 0;
}