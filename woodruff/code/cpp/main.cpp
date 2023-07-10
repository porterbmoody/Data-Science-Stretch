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
    string string_woodruff = "hello my name is taco hello pizza taco coding software c++";
    string string_verse = "hello pizza taco";
    vector<string> tokens_woodruff = StringUtil::tokenize_string(string_woodruff);
    string cool_string = "pizza";

    // bool is_in = StringUtil::string_is_in_vector(tokens_woodruff, cool_string);
    // cout << "is in: " << is_in << endl;
    std::string sub_string = StringUtil::get_sub_string(string_woodruff, 0, 3);
    cout << sub_string << endl;
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

// void display_data(const std::vector<std::vector<std::string>>& data) {
//     // Print the CSV data
//     for (const auto& row : data) {
//         for (const auto& cell : row) {
//             std::cout << cell << "\t";
//         }
//         std::cout << std::endl;
//     }
// }

// void update_progress_bar(int progress, int total, int width = 50, const std::string& description = " range: ") {
//     float percent = static_cast<float>(progress) / total;
//     int filledWidth = static_cast<int>(percent * width);

//     std::cout << description << "[" << std::string(filledWidth, '#') << std::string(width - filledWidth, ' ') << "]";
//     std::cout << " " << std::fixed << std::setprecision(1) << (percent * 100) << "%\r";
//     std::cout.flush();
// }


// float compute_percentage_match(const std::vector<std::string>& string1_words, const std::vector<std::string>& string2_words) {
//     float percentage_match;

//     for (const std::string& string1_word : string1_words) {
//         std::cout << string1_word << std::endl;
//     }
//     return percentage_match;
// }

// std::vector<std::string> extract_matches(const std::string& string1, const std::string& string2) {
//     // print each element of tokenized string
//     std::vector<std::string> matches;
//     std::vector<std::string> string1_words = split_string(string1);
//     std::vector<std::string> string2_words = split_string(string2);
//     std::cout << "phrase length: " << string1_words.size() << "\n" << std::endl;
//     // float percentage_match = compute_percentage_match(string1_words, string2_words);
//     auto match = std::find(string1_words.begin(), string1_words.end(), "company");
//     std::cout << *match << std::endl;
//     // std::cout << percentage_match << std::endl;
//     // print_vector(string1_words);
//     return matches;
// }

    // print_vector(string_tokens1);
    // for (int i = 0; i < string_woodruff_tokens.size(); ++i) {
    //     int min = i;
    //     int max = i + string_verse_tokens.size();
    //     if (max > string_woodruff_tokens.size()) {
    //         max = string_woodruff_tokens.size();
    //     }
    //     std::vector<std::string> window_woodruff = {string_woodruff_tokens.begin() + min, string_woodruff_tokens.begin() + max};
    //     // print_vector(window_woodruff);
    //     // compute_match_percentage(window_woodruff, string_verse_tokens)
    //     // update_progress_bar(min, string1_tokens.size(), 100, "  range: " + std::to_string(min) + " " + std::to_string(max));
    //     // std::this_thread::sleep_for(std::chrono::milliseconds(300));
    //     // std::cout << string1_tokens[min] << " " << string1_tokens[max] << std::endl;

    //     // std::cout << "range: " << min << " " << max << "\n" << std::endl;
    //     // std::cout << "min: " << string1_tokens[min] << " max: " << string1_tokens[min] << std::endl;
    // }
        // int min{i};
        // int max{i + string1_tokens.size()};
        // std::cout << "range: " << min << "\n";
        // std::cout << i;
        // std::cout << string1_tokens[i] << std::endl;

// g++ run.cpp -o run.exe
// run.exe

