#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>

// Returns a hash code (number) for the given string
int stringToNumber(const std::string& s) {
    int hash = 0;
    for (char c : s) {
        hash = 31 * hash + c;
    }
    return hash;
}

// Case-insensitive string comparison
bool equalsIgnoreCase(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) return false;
    for (size_t i = 0; i < a.size(); ++i) {
        if (std::tolower(a[i]) != std::tolower(b[i])) return false;
    }
    return true;
}

int main() {
    // Vector of pairs: {name, price}
    std::vector<std::pair<std::string, std::string>> items = {
        {"apple", "1.69"},
        {"banana", "0.59"},
        {"orange", "1.99"}
    };

    std::string inputName;
    std::cout << "Enter name: ";
    std::getline(std::cin, inputName);
    // Trim whitespace
    inputName.erase(0, inputName.find_first_not_of(" \t\n\r\f\v"));
    inputName.erase(inputName.find_last_not_of(" \t\n\r\f\v") + 1);

    bool found = false;
    for (const auto& item : items) {
        if (equalsIgnoreCase(item.first, inputName)) {
            std::cout << "Price: " << item.second << std::endl;
            found = true;
            break;
        }
    }

    if (!found) {
        std::cout << "Name not found." << std::endl;
    }

    return 0;
}
