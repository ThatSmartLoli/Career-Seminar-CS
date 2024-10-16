#include <iostream>
#include <vector>
#include <cstdint>
#include <bitset>
#include "graph.hpp"

using namespace std;

template<typename N>
class AdjacencyMaxtrix: public graph<N>{
private:
    const static int MaxSize = 100;
    vector<N> nodeVector;
    int adjMatrix[MaxSize][MaxSize];
    unsigned int numNodes = 0;
public:
   
    AdjacencyMaxtrix() : graph<N>() { };
    AdjacencyMaxtrix(const AdjacencyMaxtrix& other) : graph<N>() { }
    AdjacencyMaxtrix& operator= (const AdjacencyMaxtrix& source) {}
    AdjacencyMaxtrix(vector<N> newNodes, vector<pair<N, N>> newEdges) :
        graph<N>(newNodes, newEdges) { }
    ~AdjacencyMaxtrix() { }


    bool adjacent(N x, N y) {
        int nodeX = -1, nodeY = -1;
        if (x < 0 || y < 0 || x >= MaxSize || y >= MaxSize) {
            cerr << "Out of bounds." << endl;
        }

        for (int i = 0; i < numNodes; ++i) {
            if (nodeVector[i] == x) {
                nodeX = i;
            }
            if (nodeVector[i] == y) {
                nodeY = i;
            }
            if (nodeX != -1 && nodeY != -1) {
                break;
            }
        }
        if (adjMatrix[nodeX][nodeY] == 1) {
            return true;
        }
        else if (adjMatrix[nodeX][nodeY] == 0) {
            return false;
        }

        return false;
    }


    vector<N> neighbors(N x) {
        int nodeX = -1;

        for (int node = 0; node < numNodes; ++node) {
            if (nodeVector[node] == x) {
                nodeX = node;
                break;
            }
        }

        vector<N> Neighbors;

        for (int node = 0; node < numNodes; ++node) {
            if (adjMatrix[nodeX][node] == 1) {
                Neighbors.push_back(nodeVector[node]);
            }
        }

        return Neighbors;
    }


    void addNode(N node){
        if (numNodes < MaxSize) {
            nodeVector.push_back(node);
            numNodes++;
        }
        else if (numNodes >= MaxSize) {
            cerr << "Reached Max Size." << endl;
        }
    }


    void addEdge(N x, N y) {       
        int nodeX = -1, nodeY = -1;
        if (x < 0 || y < 0 || x >= MaxSize || y >= MaxSize) {
            cerr << "Out of bounds." << endl;
        }
        else {
            for (int node = 0; node < numNodes; ++node) {
                if (nodeVector[node] == x) {
                    nodeX = node;
                }
                if (nodeVector[node] == y) {
                    nodeY = node;
                }
                if (nodeX != -1 && nodeY != -1) {
                    break;
                }
            }

            if (nodeX == -1 || nodeY == -1) {
                cerr << "Not a valid value." << endl;
                return;
            }

            adjMatrix[nodeX][nodeY] = 1;
        }
    }


    void deleteEdge(N x, N y) {
        int nodeX = -1, nodeY = -1;

        if (x < 0 || y < 0 || x >= MaxSize || y >= MaxSize) {
            cerr << "Out of bounds." << endl;
        } else {

            for (int node = 0; node < numNodes; ++node) {
                if (nodeVector[node] == x) {
                    nodeX = node;
                }
                if (nodeVector[node] == y) {
                    nodeY = node;
                }
                if (nodeX != -1 && nodeY != -1) {
                    break;
                }
            }

            if (nodeX == -1 || nodeY == -1) {
                return;
            }

            adjMatrix[nodeX][nodeY] = 0;
        }
    }
};


