#include <iostream>
#include <optional>
#include <vector>

using std::vector;
using std::optional;
using std::nullopt;

optional<int> head(const vector<int> &v)
{
    return v.size() > 0 ? optional<int>(v[0]) : nullopt;
}


// This function defines the << operator for streaming an std::option
// to an output stream such as std::cout.  
std::ostream& operator<<(std::ostream &os, optional<int> x)
{
    if(x)   // this is defined as: "if x has a value"
    {
        os << x.value();
    } 
    else    // otherwise it must be nullopt
    {
        os << "nothing";
    }
    return os;
} 

int main()
{
    vector<int> v1{5,9,4,3};
    optional<int> x = head(v);
    
    vector<int> v2;
    optional<int> y = head(v2);

    std::cout << x << ", " << y << std::endl;

    return 0;
}
