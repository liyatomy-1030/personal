#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s = "nhoj ayil";
    std::cout << "Original string: " << s << std::endl;

    std::reverse(s.begin(), s.end()); // Reverse the string

    std::cout << "Reversed string: " << s << std::endl;
    return 0;
}