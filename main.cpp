#include <bits/stdc++.h>
using namespace std;
// A, B C = rock papers scissors
// X, Y, Z = rock paper scissors
// 1 2 3
// loss = 0
// draw = 3
// win = 6

int num_points_for_move(string s) {
  if (s == "X") return 1;
  if (s == "Y") return 2;
  return 3;
}

int win_loss_draw(string a, string b) {
  if (a[0] - 'A' == b[0]-'X') {
    return 3; //draw
  } else if (a == "A") {
    // opponent rock
    if (b == "Y") {
      return 6;
    } else {
      return 0;
    }

  } else if (a == "B") {
    // paper
    if (b == "X") {
      return 0;
    } else {
      return 6;
    }
  } else  {
    //scissors
    if(b == "X") {
      return 6;
    } else {
      return 0;
    }
  }
}
string which_to_choose(string a, string b) {
  if (a == "A") {
    if (b == "X") {
      return "Z";
    } else if (b == "Y") {
      return "X";
    } else if (b == "Z") {
      return "Y";
    }
  } else if (a == "B") {
    if (b == "X") {
      return "X";
    } else if (b == "Y") {
      return "Y";
    } else if (b == "Z") {
      return "Z";
    }
  } else {
    if (b == "X") {
      return "Y";
    } else if (b == "Y") {
      return "Z";
    } else {
      return "X";
    }
  }
  return "yeet";
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int total_points = 0;
  while(!cin.eof()) {
    string a, b; cin >> a >> b;
    cout << a << ", " << b << endl;
    if (a == "" || b == "") break;
    string adjusted = which_to_choose(a, b);
    int gain =  num_points_for_move(adjusted) + win_loss_draw(a,adjusted);
    cout << gain << endl;
    total_points += gain;
  }
  cout << total_points << endl;
  return 0;
}
