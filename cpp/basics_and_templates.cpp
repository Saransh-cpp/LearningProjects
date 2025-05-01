#include<iostream>
using namespace std;

template<typename T>
void data_types(T x, T y) {
    float a, b;
    a = 0.5;
    b = 0.7;
    double c, d;
    c = 0.5;
    d = 0.7;
    char ch;
    ch = 'A';
    bool flag;
    flag = true;
    string str; 
    getline(cin, str);
    cout << x << y << a << b << c << d << ch << flag << str << endl;
}

template<typename T>
void if_else(T x) {
    if (typeid(x) == typeid(int)) {
        cout << "int" << endl;
    } else if (typeid(x) == typeid(float)) {
        cout << "float" << endl;
    } else if (typeid(x) == typeid(double)) {
        cout << "double" << endl;
    } else if (typeid(x) == typeid(char)) {
        cout << "char" << endl;
    } else if (typeid(x) == typeid(bool)) {
        cout << "bool" << endl;
    } else if (typeid(x) == typeid(string) || typeid(x) == typeid(char)) {
        cout << "string" << endl;
    }
    else {
        cout << "Unknown type" << endl;
    }
}

void switch_case() {
    int x;
    cin >> x;
    switch (x) {
        case 1:
            cout << "one" << endl;
            break;
        case 2:
            cout << "two" << endl;
            break;
        case 3:
            cout << "three" << endl;
            break;
        default:
            cout << "default" << endl;
    }
}

namespace s {
    int l = 5;
} // namespace s

// https://isocpp.org/wiki/faq/templates#overview-templates
template<typename T>
T add(T a, T b) {
    if (typeid(T) != typeid(int) && typeid(T) != typeid(float) && typeid(T) != typeid(double)) {
        string msg = typeid(a).name();
        throw invalid_argument(msg);
    }
    return a + b;
}

template<> const char* add<const char*>(const char* a, const char* b) {return a;}

template<typename T> void foo(T* x)
{ std::cout << "foo<" << typeid(T).name() << ">(T*)\n"; }

void foo(int x)
{ std::cout << "foo(int)\n"; }

void foo(double x)
{ std::cout << "foo(double)\n"; }

template<typename T>
void swap_custom(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int arr_sum(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    // cout << "Hello, World!" << endl;
    // data_types<int>(5, 6);
    // if_else<int>(5);
    // if_else<float>(5.5);
    // if_else<long long>(5);
    // switch_case();

    // int arr[] = {1, 2, 3, 4, 5};
    // int n[2][2] = {{1, 2}, {3, 4}};
    // string s = "something";
    // cout << s[s.size() - 1] << endl;
    // cout << s::l << endl;

    // for (auto i = 0; i < 5; i++)
    // {
    //     cout << i << endl;
    // }

    // auto i = 0;
    // while (i < 5)
    // {
    //     cout << i << endl;
    //     i++;
    // }

    // cout << add(2.3, 3.3);
    // string a = "d";
    // string b = "c";
    // cout << add(true, false);
    // cout << add(a, b);
    // cout << add<int>(2, 3);
    // cout << add<string>("a", "b");  
    // char a = 'a';
    // char b = 'b';
    // cout << add("a", "b");

    // foo(42);        // matches foo(int) exactly
    // foo(42.0);      // matches foo(double) exactly
    // foo("abcdef");  // matches foo<T>(T*) with T = char

    // int a = 5;
    // int b = 6;

    // swap_custom(a, b);
    // cout << "a: " << a << ", b: " << b << endl;

    // char a = 'a';
    // char b = 'b';
    // swap_custom(a, b);
    // cout << "a: " << a << ", b: " << b << endl;

    // int arr[] = {1, 2, 3, 4, 5};
    // cout << arr_sum(arr, 5);

    return 0;
}
