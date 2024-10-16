#include <iostream>
#include "SelfAdjusting.hpp"

using namespace std;

int main() {
    SelfAdjustingList<int> myList;

    int number = 9;

    myList.push_back(0);
    myList.push_back(1);
    myList.push_back(2);
    myList.push_back(3);
    myList.push_back(4);
    myList.push_back(5);
    myList.push_back(6);
    myList.push_back(7);
    myList.push_back(8);
    myList.push_back(9);

    cout << "The List: ";
    myList.traverse([](int& data) {cout << data;});
    int* foundItem = myList.find(number);

    cout << endl << "Number to find: " << number << endl;

    if (foundItem != nullptr) {
    cout << "The List after Adjusting: ";
        myList.traverse([](int& data) {cout << data;});
    cout << endl;
    }
    else {
    cout << "Item not found." << endl;
    }

    return 0;
}