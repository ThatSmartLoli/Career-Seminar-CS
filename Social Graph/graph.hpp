#pragma once
#include <iostream>
#include <vector>

using namespace std;

template <typename N>
class graph {
public:
    graph() {};
    graph(vector<N> nodes, vector<pair<N, N>> edges) {};
    virtual ~graph() {};

    virtual bool adjacent(N x, N y) = 0;
    virtual vector<N> neighbors(N x) = 0;
    virtual void addNode(N x) = 0;
    virtual void addEdge(N x, N y) = 0;
    virtual void deleteEdge(N x, N y) = 0;
};
