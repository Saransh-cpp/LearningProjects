#include<iostream>
#include<thread>
#include<mutex>


std::mutex mx;

void print_func(int id) {
    // mx.lock();
    // RAII
    std::lock_guard<std::mutex> g(mx);
    std::cout << "ID is: " << id << std::endl;
    // mx.unlock();
}

int main () {
    std::thread t1(print_func, 0);
    std::thread t2(print_func, 1);
    std::thread t3(print_func, 2);
    std::thread t4(print_func, 3);

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    return 0;
}
