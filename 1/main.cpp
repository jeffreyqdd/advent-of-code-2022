#include <bits/stdc++.h>
using namespace std;

int main() {
  std::ios_base::sync_with_stdio(false);

  int current_total = 0;
  vector<int> answers;
  while(!cin.eof()) {
    string s;
    getline(cin, s);
    if (s.length() == 0) {
      // new
      answers.push_back(current_total);
      current_total = 0;
    } else {
      current_total += stoi(s);
    }
  }

  sort(answers.rbegin(), answers.rend());
  int sum = 0;
  for(int i = 0; i < 3; i++) {
    sum += answers[i];
  }
  cout << sum << endl;

  return 0;
}
