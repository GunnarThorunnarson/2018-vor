#include <iostream>

using namespace std;

// recursive collatz function
// we are interested in finding the longest chain, so we'll
// want the function to return the number of terms required to
// reach 1.
int c(long n) {
  if (n==1) return 1;
  if (n%2) return 1 + c(3*n+1);
  return 1 + c(n/2);
}

struct COLLATZ {
  int num;
  int count;
};

int main() {
  COLLATZ longest;
  longest.count = 0;
  longest.num = 0;
  for ( int i = 1; i <= 1000000; i++) {
    int count = c(i);
    if (count > longest.count) {
        longest.count = count;
        longest.num = i;
    }
  }
  cout << "The longest sequence is generated by the number " << longest.num << " with " << longest.count << " terms!" << endl;
  return 0;
}
