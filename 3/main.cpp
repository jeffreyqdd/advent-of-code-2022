#include <bits/stdc++.h>
using namespace std;

int priority(char c) {
  if (c >= 'a' && c <= 'z') {
    return c - 'a' + 1;
  } else {
    return c - 'A' + 27;
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int total = 0;
  while(!cin.eof()) {
    string s1, s2, s3; cin >> s1 >> s2 >> s3;
    set<char> round1, round2, round3;
    if (s1 == "" || s1 == "" || s1 == "") break;

    for(char c : s1) round1.insert(c);
    for(char c : s2) if (round1.find(c) != round1.end()) round2.insert(c);
    for(char c : s3) if (round2.find(c) != round2.end()) round3.insert(c);

    total += priority(*round3.begin());
  }
//    string sack; cin >> sack;
//    cout << sack << endl;
//    if (sack == "") break;
//    set<char> memory;
//    set<char> repeat;
//
//    for(int i = 0; i < sack.size() / 2; i ++) {
//      cout << "inserting " << sack[i] << endl;;
//      memory.insert(sack[i]);
//    }
//    for(int i = sack.size() / 2; i < sack.size(); i++) {
//      if (memory.find(sack[i]) != memory.end()) {
//        repeat.insert(sack[i]);
//      }
//    }
//
//    for(char c : repeat) {
//        total += priority(c);
//    }
//  }
  cout << total << endl;
  return 0;
}
