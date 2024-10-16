#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

template<typename T>
void partitionList(T& splittingValue, list<T>& startingList, list<T>* lessThanList, list<T>* greaterThanList);

template<typename T>
list<T>* quicksort(list<T>& inputList);

int main() {
    list<int> input = { 5, 2, 1, 3, 4 };

    list<int>* sortedList = quicksort(input);

    cout << "The Sorted List: ";
    for (const auto& it : *sortedList) {
        cout << it << " ";
    }
    cout << endl;

    delete sortedList;

    return 0;
}

template<typename T>
list<T>* quicksort(list<T>& inputList) {
    if (inputList.size() <= 1) {
        return new list<T>(inputList);
    }

    T pivot = inputList.front();
    list<T> lessThan;
    list<T> greaterThan;

    partitionList(pivot, inputList, &lessThan, &greaterThan);

    list<T>* sortedLess = quicksort(lessThan);
    list<T>* sortedGreater = quicksort(greaterThan);
   

    sortedLess->push_back(pivot);
    sortedLess->splice(sortedLess->end() , *sortedGreater);

    delete sortedGreater;

    return sortedLess;
}

template<typename T>
void partitionList(T& splittingValue, list<T>& startingList, list<T>* lessThanList, list<T>* greaterThanList) {
    for (auto& it : startingList) {
        if (it < splittingValue) {
            lessThanList->push_back(it);
        }
        else if (it > splittingValue) {
            greaterThanList->push_back(it);
        }
    }
}