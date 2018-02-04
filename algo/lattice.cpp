#include <iostream>
using namespace std;

// Because we cannot go left or up, we can think about the grid shrinking when
// we make any move. Go right and the width of the remaining grid is reduced
// by 1, and thus for down and the height. The base case is either the height
// or the width reaching 0, because at that point there are no more choices
// to be made and the remaining path is known.
//
long lattice(int w, int h){
  if (w == 0 || h == 0) return 1;
  int count = 0;
  count += lattice(w-1, h);
  count += lattice(w, h-1);
  return count;
}

int main() {
  // should return 2
  cout << lattice(20, 20) << endl;
  return 0;
}
