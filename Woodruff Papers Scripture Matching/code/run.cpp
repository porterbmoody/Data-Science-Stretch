#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>


// std::vector<std::vector<std::string>> read_csv(const std::string& path) {
//     std::ifstream file(path);

//     if (!file) {
//         std::cerr << "Failed to open file." << std::endl;
//         return {};
//     }

//     std::vector<std::vector<std::string>> data;
//     std::string line;

//     while (std::getline(file, line)) {
//         std::vector<std::string> row;
//         std::stringstream lineStream(line);
//         std::string cell;

//         while (std::getline(lineStream, cell, ',')) {
//             row.push_back(cell);
//         }

//         data.push_back(row);
//     }

//     return data;
// }

// void display_data(const std::vector<std::vector<std::string>>& data) {
//     // Print the CSV data
//     for (const auto& row : data) {
//         for (const auto& cell : row) {
//             std::cout << cell << "\t";
//         }
//         std::cout << std::endl;
//     }
// }

void print_vector(const std::vector<std::string> vector) {
    for (const std::string& str : vector) {
        std::cout << str << std::endl;
    }
}

std::vector<std::string> tokenize_string(const std::string& string) {
    std::vector<std::string> tokens;
    std::stringstream ss(string);
    std::string token;

    while (ss >> token) {
        tokens.push_back(token);
    }
    return tokens;
}


std::vector<std::string> extract_matches(const std::string& string1, const std::string& string2) {
    // std::cout << "string1: " << string1 << std::endl;
    // std::cout << "string2: " << string2 << std::endl;
    // tokenize string
    std::vector<std::string> matches;
    std::vector<std::string> string1_tokens = tokenize_string(string1);
    // std::cout << "length of string1 token vector: " << string1_tokens.size() << std::endl;

    std::cout << "string1 tokens: " << string1_tokens.size();
    print_vector(string1_tokens);
    // for (int i = 0; string1_tokens.size(); ++i) {
    //     std::cout << "hello" << std::endl;
    // }
    //     int min{i};
        // int max{i + string1_tokens.size()};
        // std::cout << "range: " << min << "\n";
        // std::cout << i;
        // std::cout << string1_tokens[i] << std::endl;
    return matches;
}



int main() {
    // std::vector<std::vector<std::string>> data = read_csv("../test.csv");
    // display_data(data);
    // std::vector<std::string> = matches;
    std::vector<std::string> matches;
    std::string string1 = "hello my name is";
    std::string string2 = "pizza pizza taco";
    std::cout << string1 << "\n";
    matches = extract_matches(string1, string2);
    return 0;
}


// g++ run.cpp -o run.exe
// run.exe