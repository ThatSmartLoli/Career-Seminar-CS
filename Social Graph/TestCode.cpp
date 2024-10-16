#include <iostream>
#include "AdiacencyMaxtrixGraph.hpp"
#include <vector>
#include <queue>
#include <map>

using namespace std;

void populatingData(AdjacencyMaxtrix<int>&, vector<int>&, vector<string>&, map<int, string>&);
bool isPathToKevinBacon(AdjacencyMaxtrix<int>& socialGraph, int begin, vector<int>& path);

int main() {
    AdjacencyMaxtrix<int> socialGraph;
    vector<int> path, playersNumber;
    vector<string> playerNames;
    map<int, string> nameMap;
    int firstPerson = 0;
    populatingData(socialGraph, playersNumber, playerNames, nameMap);
   
    firstPerson = playersNumber[0];
    bool isConnectedToKevinBacon = isPathToKevinBacon(socialGraph, firstPerson, path);

    if (isConnectedToKevinBacon) {
        cout << "The Path: " << endl;
        for (const int person : path) {
            cout << nameMap[person] ;
            if (person != path.back()) {
                cout << " -> ";
            }           
        }
        cout << endl;
    }
    else if(!isConnectedToKevinBacon) {
        cerr << "You are not connected to Kevin Bacon." << endl;
    }

    return 0;
}



void populatingData(AdjacencyMaxtrix<int>& social, vector<int>& playerNumber, vector<string>& playerName, map<int, string>& connection) {

    playerName = {
        "Austen", "Kevin Bacon", "Cody", "Paul", "Jill", "Kathryn", "Lexy", "Jack", "Tom", "Cythia", "Austin", "Inuyasha", "Phil", "Danial",
        "Jessie", "Zack", "Jackson", "Hosa", "AAron", "Terry"
    };

    playerNumber = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 };

    for (int i = 0; i < playerNumber.size(); i++) {
        social.addNode(playerNumber[i]);
        connection[playerNumber[i]] = playerName[i];
    }

    social.addEdge(0, 4);
    social.addEdge(4, 19);
    social.addEdge(19, 9);
    social.addEdge(9, 3);
    social.addEdge(3, 11);
    social.addEdge(11, 16);
    social.addEdge(16, 1);
}

bool isPathToKevinBacon(AdjacencyMaxtrix<int>& socialGraph, int begin, vector<int>& path) {

    queue<int> queues;
    map<int, bool> visited;
    map<int, int> temp;
    int maxLimitOfTries = 0;


    visited[begin] = true;
    queues.push(begin);


    while (!queues.empty()) {

        if (maxLimitOfTries > 7) {
            return false;
        }

        int current = queues.front();
        queues.pop();

        if (current == 1) {
            while (current != begin) {
                path.push_back(current);
                current = temp[current];
            }
            path.push_back(begin);
            reverse(path.begin(), path.end());
            cout << "You are connected to Kevin Bacon!" << endl;
            return true;
        }

        for (int neighbor : socialGraph.neighbors(current)) {
            if (!visited[neighbor]) {
                temp[neighbor] = current;
                visited[neighbor] = true;
                queues.push(neighbor);
            }
        }
        maxLimitOfTries++;
    }


    return false;
}
