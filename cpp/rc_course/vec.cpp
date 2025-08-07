#include<iostream>

template<typename T>
class Vec {
    public:
        int t;
        T * arr;
        Vec(int t, T * arr) : t(t), arr(arr) {
            // arr = new T[t];
        };
        T dot(Vec v) {
            T sum = 0;
            for (size_t i = 0; i < t; i++)
            {
                sum += arr[i] * v.arr[i];
            }
            return sum;
        }
};

int main() {
    int arr[] = {1, 2, 3};
    Vec<int>v(3, arr);
    std::cout << v.dot(v);
    return 0;
}
