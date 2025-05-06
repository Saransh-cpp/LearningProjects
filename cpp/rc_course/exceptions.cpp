#include <iostream>
#include <vector>
#include <stdexcept>

using std::vector;


double InnerProduct(const vector<double> &x, const vector<double> &y)
{
    if(x.size() != y.size())
    {
        std::string errorMessage = "Inner product vectors different sizes: " +
            std::to_string(x.size()) + " and " + std::to_string(y.size()); 
        throw std::range_error(errorMessage);
    }
    
    double product = 0;
    for(size_t i = 0; i < x.size(); i++)
    {
        product += x[i] * y[i];
    }

    return product;
}

class FunctionDomainException: public exception
{
    public:
    FunctionDomainException(std::string func_name, double value) 
    {
        message = "Function Domain error on function " + func_name \
                 + ". Input " + std::to_string(value) + " invalid.";
        bad_input = value;
    }

    const char * what() const noexcept
    {
        return message.c_str();
    }

    std::string message;
    double bad_input;
};

int main()
{
    // vector<int> fibbonacciList = {1, 1, 2, 3, 5, 8, 13};

    // try
    // {
    //     std::cout << fibbonacciList.at(15) << std::endl;
    // }
    // // evaluated in order always
    // catch(const std::out_of_range &e)
    // {
    //     std::cerr << "Problem accessing Fibbonacci list due to range: " << e.what() << std::endl;
    //     std::cerr << "Max index of list is " << fibbonacciList.size() -1 << std::endl;
    // }
    // catch(const std::exception &e)
    // {
    //     std::cerr << "Other error occurred accessing Fibbonacci list: " << e.what() << std::endl;
    // }

    vector<double> a = {0.2, 0.1, 1.2, 5.99};
    vector<double> b = {0.1, 1.8, 2.9};

    double ab;
    try
    {
        ab = InnerProduct(a, b);
    }
    catch(const std::range_error& e)
    {
        std::cerr << e.what() << '\n';
    }

    return 0;
}
