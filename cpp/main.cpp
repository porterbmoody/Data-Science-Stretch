#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <iomanip>
#include <chrono>
#include <thread>
#include <algorithm>
// #include "DataFrame.h"
#include "StringUtil.h"


using namespace std;



int main() {
    cout << "importing class StringUtil" << endl;
    string cool_string = "hello pizza taco";
    vector<string> cool_tokens = StringUtil::tokenize_string(cool_string);

    StringUtil::print_vector(cool_tokens);
    // bool is_in = StringUtil::string_is_in_vector(tokens_woodruff, cool_string);
    // cout << "is in: " << is_in << endl;
    // std::string sub_string = StringUtil::get_sub_string(string_woodruff, 0, 3);
    // cout << sub_string << endl;
    // float percentage_match = StringUtil::compute_percentage_match(string_woodruff, string_verse);
    // cout << percentage_match << endl;

    // string path = "test.csv";
    // vector<vector<string>> data = DataFrame::read_csv(path);
    // DataFrame::print_data(data);
    return 0;
}

    // string string_woodruff = "sept traveling in company with elder benjamin lynn clapp";
    // string string_verse = "hearken o ye people";

    // vector<string> tokens_woodruff = data_util.tokenize_string(string_woodruff);
    // std::vector<std::vector<std::string>> data = read_csv("../test.csv");
    // display_data(data);
    // std::vector<std::string> = matches;
    // vector<string> matches;
    // string string_woodruff = "sept traveling in company with elder benjamin lynn clapp";
    // string string_verse = "hearken o ye people";
    // cout << "extracting matches...\n";
    // extract_matches(string_woodruff, string_verse);
    // print_vector(matches);
    // int totalProgress = 100;
    // simulateProgress(totalProgress);
    // std::vector<std::vector<std::string>> data = read_csv("../test.csv");
    // display_data(data);
    // std::vector<std::string> = matches;
    // vector<string> matches;
    // cout << "extracting matches...\n";

	// vector<string> tokens_woodruff = StringUtil::tokenize_string(string_woodruff);
	// StringUtil::print_vector(tokens_woodruff);
    // extract_matches(string_woodruff, string_verse);
    // print_vector(matches);
    // int totalProgress = 100;
    // simulateProgress(totalProgress);


// g++ run.cpp -o run.exe
// run.exe

