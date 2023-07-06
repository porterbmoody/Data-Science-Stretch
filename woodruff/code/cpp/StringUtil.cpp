#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>
#include "StringUtil.h"

using namespace std;


vector<string> StringUtil::tokenize_string(const string& input_string) {
    vector<string> tokens;
    stringstream ss(input_string);
    string token;

    while (ss >> token) {
        tokens.push_back(token);
    }
    return tokens;
}


void StringUtil::print_vector(const vector<string>& vector) {
    for (const auto& string : vector) {
        cout << string << " ";
    }
    cout << endl;
}

bool StringUtil::string_is_in_vector(const vector<string>& vector, const string& string) {
    for (auto element = vector.begin(); element != vector.end(); element++) {
        if (string == *element) {return true;}
    }
    return false;
}

vector<string> StringUtil::get_sub_vector(const vector<string>& vector, int start, int end) {
    std::vector<std::string> sub_vector;
    for (int i = start; i <= end; i++) {
        string current_element = vector[i];
        sub_vector.push_back(current_element);
    }
    return sub_vector;
}

string StringUtil::get_sub_string(const string& string, int start, int end) {
    // vector<string> string1_tokens = {'bro'};
    // std::string string = "bro";
    std::vector<std::string> string_tokens = StringUtil::tokenize_string(string);
    std::vector<std::string> sub_vector = StringUtil::get_sub_vector(string_tokens, start, end);
    // for (int i = start; i < end; i++) {
    //     std::string current_element = string_tokens[i];
    //     sub_vector.push_back(current_element);
    // }
    std::string sub_string = StringUtil::implode_vector(sub_vector);
    return sub_string;
}

string StringUtil::implode_vector(const vector<string>& vector) {
    stringstream ss;
    for(auto element = vector.begin(); element != vector.end(); element++) {
        if(element != vector.begin()) {ss<<" ";}
            ss << *element;
    }

    // cout << ss.str() << endl;
    return ss.str();
}

// vector<string> split_string_into_vector(const string& string, int increment) {
// }

float StringUtil::compute_percentage_match(const string& string1, const string& string2) {
    vector<string> string1_tokens = StringUtil::tokenize_string(string1);
    vector<string> string2_tokens = StringUtil::tokenize_string(string2);
    int start = 2;
    int end = 7;
    print_vector(string1_tokens);

    return .2;
}


