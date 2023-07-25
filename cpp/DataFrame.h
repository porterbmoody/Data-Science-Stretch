#ifndef DATAFRAME_H
#define DATAFRAME_H

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;


class DataFrame {
    public:
    // void create_dataframe(const vector<vector<string>>& data) {
        // vector<vector<string>> data = data;
    // }

    vector<vector<string>> DataUtil::read_csv(const string& path);

    void print() {
        for (const auto& row : data) {
            for (const auto& cell : row) {
                cout << cell << endl;
            }
        }
    }
}

#endif
