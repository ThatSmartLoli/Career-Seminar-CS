#pragma once
#include "List.hpp"

template <typename T>
class SelfAdjustingList : public List<T> {
public:
    SelfAdjustingList() : List<T>() {}

    T* find(T itemToFind) {
        typename List<T>::iterator FindingItem = this->begin();
        while (FindingItem != this->end()) {
            if (*FindingItem == itemToFind) {
                T foundItem = *FindingItem;
                this->erase(FindingItem);
                this->push_front(foundItem);
                T found = this->front();
                return &(found);
            }
            ++FindingItem;
        }
        return nullptr;
    }


};