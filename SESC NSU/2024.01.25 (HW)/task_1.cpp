#include "iostream"
#include "stack"
#include "string"
#include "map"

#define ll long long

using namespace std;


int main() {
    ios::sync_with_stdio(false);

    map<char, char> parentheses;
    parentheses['['] = ']';
    parentheses[']'] = '[';
    parentheses['{'] = '}';
    parentheses['}'] = '{';
    parentheses['('] = ')';
    parentheses[')'] = '(';

    cout << "Input a sequence of parentheses:\n";
    string seq;
    cin >> seq;

    for (ll i = 0; i < seq.size(); ++i) {
        if (seq[i] == '{' or seq[i] == '[' or seq[i] == '(') {

        }
    }

}