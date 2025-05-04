#include <iostream>
#include <list>
#include <set>
#include <unordered_set>
#include <map>
using namespace std;


bool comp(pair<int, int> p1, pair<int, int> p2) {
    if (p1.second < p2.second) return true;
    if (p1.second > p2.second) return false;

    if (p1.first > p2.first) return true;
    return false;
}

int main() {
    // pairs
    // pair<int, int> p1 = {1, 3};
    // cout << p1.first << " " << p1.second << endl;
    // pair<int, int> arr[] = {{1, 2}, {3, 4}, {5, 6}};
    // cout << arr[0].first << " " << arr[0].second << endl;

    // vector<int> v = {1, 2, 3, 4, 5};
    // v.reserve(20);  // reserve a chunk of memory, efficient (does not copy but limits elements to 20)
    // v.push_back(6);
    // v.emplace_back(7);
    // cout << "Vector: ";
    // for (int i = 0; i < v.size(); i++) {
    //     cout << v[i] << " ";
    // }

    // vector<int> v(5, 10); // 5 elements of value 10
    // cout << "Vector with 5 elements of value 10: ";
    // for (int i = 0; i < v.size(); i++) {
    //     cout << v[i] << " ";
    // }

    // vector<pair<int, int>> v = {{1, 2}, {3, 4}, {5, 6}};
    // cout << "Vector of pairs: ";
    // for (int i = 0; i < v.size(); i++) {
    //     cout << "(" << v[i].first << ", " << v[i].second << ") ";
    // }

    // vector<int> v = {1, 2, 3, 4, 5};
    // vector<int>::iterator it = v.begin();
    // vector<int>::iterator itb = v.end();

    // it++;
    // cout << "Iterator: " << *it << endl;
    // cout << "Iterator: " << *(itb-1) << endl;

    // cout << v.back() << " " << v.at(0);

    // for(vector<int>::iterator it = v.begin(); it != v.end(); it++) {
    //     cout << *it << " ";
    // }

    // for(auto it = v.begin(); it != v.end(); it++) {
    //     cout << *it << " ";
    // }

    // for (auto el : v) {
    //     cout << el << " ";
    // }

    // v.erase(v.begin() + 2); // erase element at index 2
    // v.erase(v.begin() + 1, v.begin() + 3); // erase elements from index 1 to 2
    // int x = v.size();

    // v.insert(v.begin(), 5);
    // v.insert(v.begin() + 1, 2, 10);

    // vector<int> copy(2, 500);
    // v.insert(v.begin() + 2, copy.begin(), copy.end());

    // v.pop_back();

    // swap
    // clear
    // empty

    // doubly linked list internally
    // list<int> ls;

    // ls.push_back(5);
    // ls.emplace_back(5);
    // ls.push_front(2);
    // ls.emplace_front(2);

    // deque<int> dq;
    // dq.push_back(5);
    // dq.emplace_back(5);
    // dq.push_front(2);
    // dq.emplace_front(2);

    // stack<int> st;

    // st.push(2);
    // st.emplace(3);

    // cout << st.top() << st.size() << st.empty();
    // st.pop();

    // stack<int> st1, st2;
    // st1.swap(st2);

    // queue<int> q;

    // q.push(5);
    // q.push(6);

    // cout << q.front() << q.back() << q.empty();
    // q.pop();

    // tree inside
    // max heap
    // lookup is o(1) and everything else is logn
    // priority_queue<int> pq;

    // pq.push(5);
    // pq.push(2);
    // pq.push(3);

    // cout << pq.top(); // 5
    // pq.pop();
    // cout << pq.top(); // 3

    // Min heap
    // priority_queue<int, vector<int>, greater<int>> pq;
    // pq.push(5);
    // pq.push(2);
    // pq.push(3);

    // cout << pq.top(); // 2
    // pq.pop();
    // cout << pq.top(); // 3

    // everything in logn complexity
    // set<int> st;

    // st.insert(1);
    // st.insert(2);
    // st.insert(2);
    // st.insert(0);

    // auto it = st.find(3); // returns an iterator that points to 3 (st.end() - points after 2)

    // int cnt = st.count(3);

    // multiset<int> ms;
    // ms.insert(1);
    // ms.insert(1);
    // ms.insert(1);

    // ms.erase(1); // erases all 1
    // ms.erase(ms.find(1)); // find is iterator pointing to first 1
    // ms.erase(ms.find(1), next(ms.find(1), 2)); // use next and prev for bidirectional iterators - https://stackoverflow.com/a/68056663

    // unordered_set<int> uset; // no sorted order, all operations are O(1), worst case is O(n)

    // map<int, int> m;  // same as dict and set
    // multimap<int, int> mp;  // same as dict and multiset
    // unordered_map<int, int> mpp;  // same

    vector<int> a = {1, 3, 4, 5, 2, 8, 7};
    // sort(a.begin(), a.end());

    // reverse sort
    // sort(a.begin(), next(a.begin(), 2), greater<int>());
    // for (auto el : a)
    // {
    //     cout << el << " ";
    // }

    // pair<int, int> p[] = {{8, 8}, {2, 3}, {4, 3}};
    // sort(p, p+3, comp);
    // for (int i = 0; i < 3; i++)
    // {
    //     cout << p[i].first << " ";
    // }

    // int num = 7;
    // int cnt = __builtin_popcount(num);  // return number of set bits

    // long long num = 7483927563819;
    // int llcnt = __builtin_popcountll(num);

    // string s = "123";
    // do
    // {
    //     cout << s << endl;
    // } while (next_permutation(s.begin(), s.end())); // s must be sorted
    
    // int maxel = *max_element(a.begin(), a.end());
    
    return 0;
}