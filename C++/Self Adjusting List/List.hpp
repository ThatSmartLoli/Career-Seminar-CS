#pragma once
#include <functional>
template <typename T>
class List {
private:
	class Node {
	public:
		T data;
		Node* prev;
		Node* next;
		bool isHiddenNode = false;
	};
	Node* head;
	Node* tail;

public:
	class const_iterator {

	protected:
		Node* current;
		T& retrieve() const { return current->data; }
		const_iterator(Node* p) : current(p) { }
		friend class List<T>;

	public:
		const_iterator() : current(nullptr) { }

		T& operator*() const {
			return retrieve();
		}

		const_iterator& operator++() {
			current = current->next;
			return *this;
		}

		const_iterator  operator++(int) {
			const_iterator old = *this;
			++(*this);
			return old;
		}

		bool operator==(const const_iterator& rhs) const {
			return current == rhs.current;
		}
		bool operator!=(const const_iterator& rhs) const {
			return !(*this == rhs);
		}
	};

public:
	class iterator : public const_iterator {
	protected:
		iterator(Node* p) : const_iterator(p) { }
		friend class List<T>;

	public:
		iterator() { }

		T& operator *() {
			return const_iterator::retrieve();
		}

		const T& operator* () const {
			return const_iterator::operator*();
		}

		iterator& operator++ () {
			this->current = const_iterator::current->next;
			return *this;
		}

		iterator operator++ (int) {
			iterator old = *this;
			++(*this);
			return old;
		}
	};

private:
	void setupList() {
		Node* newNode = new Node();
		newNode->next = tail;
		newNode->prev = head;
		head->next = newNode;
		tail->prev = newNode;
	}
	void deleteListContents() {
		Node* current = head->next;
		Node* temp = nullptr;
		while (current != tail->prev) {
			temp = current->next;
			delete current;
			current = temp;
		}
	}

public:
	List() {
		head = new Node();
		head->isHiddenNode = true;
		tail = new Node();
		tail->isHiddenNode = true;
		head->prev = nullptr;
		head->next = tail;
		tail->prev = head;
		tail->next = nullptr;

	};
	List(T newData) {
		setupList();
		(head->next)->data = newData;
	}
	List(List& rhs) {
		// copy constructor
		deleteListContents();
		head = rhs.head;
		tail = rhs.tail;
	}
	~List() {
		// And a destructor
		deleteListContents();
		delete head;
		delete tail;
	}
	bool empty() {
		return (head->next == tail);
	}

	// iterator related methods
	iterator begin() { return { head->next }; }

	iterator end() { return tail; }

	const_iterator cbegin() const {
		return { head->next };
	}

	const_iterator cend() const
	{
		return { tail };
	}

	iterator erase(iterator itr) {
		Node* p = itr.current;
		iterator iterToReturn{ p->next };
		p->prev->next = p->next;
		p->next->prev = p->prev;
		return iterToReturn;
	}

	iterator insert(iterator itr, const T& x) {
		Node* p = itr.current;
		Node* newNode = new Node{ x, p->prev, p };
		p->prev = p->prev->next = newNode;
	}
	iterator erase(iterator from, iterator to) {
		iterator itr = from;
		while (itr != to) {
			itr = erase(itr);
		}
		return to;
	}
	// And the methods for the rest 
	void push_front(T data) {
		if (this->empty()) {
			setupList();
			Node* actualHead = head->next;
			actualHead->data = data;
		}
		else {
			Node* actualHead = head->next;
			Node* newNode = new Node();
			newNode->data = data;
			newNode->next = actualHead;
			actualHead->prev = newNode;
			newNode->prev = head;
			head->next = newNode;
		}
	}
	void push_back(T data) {
		if (this->empty()) {
			setupList();
			Node* actualTail = tail->prev;
			actualTail->data = data;
		}
		else {
			Node* actualTail = tail->prev;
			Node* newNode = new Node();
			newNode->data = data;
			newNode->prev = actualTail;
			actualTail->next = newNode;
			newNode->next = tail;
			tail->prev = newNode;
		}
	}
	T front() {
		Node* actualHead = head->next;
		return (actualHead->data);
	}
	T back() {
		Node* actualTail = tail->prev;
		return (actualTail->data);
	}
	void pop_back() {
		if (!empty()) {
			Node* lastNode = tail->prev;
			tail->prev = lastNode->prev;
			Node* newLastNode = tail->prev;
			newLastNode->next = tail;
			delete lastNode;
			lastNode = nullptr;
		}
		else {
			std::cerr << "pop_back(): Attempt to pop from empty list. " << std::endl;
		}
	}
	void pop_front() {
		if (!empty()) {
			Node* firstNode = head->next;
			head->next = firstNode->next;
			Node* newFirstNode = head->next;
			newFirstNode->prev = head;
			delete firstNode;
			firstNode = nullptr;
		}
		else {
			std::cerr << "pop_back(): Attempt to pop from empty list. " << std::endl;
		}
	}
	void traverse(std::function<void(T& data)> doIt) {
		Node* current = head->next;
		while (current != tail) {
			doIt(current->data);
			current = current->next;
		}
	}
};