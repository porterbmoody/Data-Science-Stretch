#ifndef STRINGUTIL_H
#define STRINGUTIL_H
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;


class StringUtil {


public:
    static void print_vector(const vector<string>& input_vector);
    static vector<string> tokenize_string(const string& input_string);
    static float compute_percentage_match(const string& string1, const string& string2);
	static string implode_vector(const vector<string>& vector);
	static bool string_is_in_vector(const vector<string>& vector, const string& string);
	static vector<string> get_sub_vector(const vector<string>& vector, int start, int end);
	static string get_sub_string(const string& string, int start, int end);
};



#endif