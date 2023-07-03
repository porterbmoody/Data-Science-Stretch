#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include "DataFrame.h"

using namespace std;


vector<vector<string>> DataUtil::read_csv(const string& path) {
    ifstream file(path);

    if (!file) {
        cerr << "Failed to open file." << endl;
        return {};
    }
    vector<vector<string>> data;
    string line;

    while (getline(file, line)) {
        vector<string> row;
        stringstream lineStream(line);
        string cell;

        while (getline(lineStream, cell, ',')) {
            row.push_back(cell);
        }

        data.push_back(row);
    }

    return data;
}


    void print() {
        cout << "printing csv..." << endl;
        for (const auto& row : data) {
            for (const auto& cell : row) {
                cout << cell << endl;
            }
        }
    }