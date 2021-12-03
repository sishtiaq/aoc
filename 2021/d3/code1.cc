#include <iostream>
#include <string>
#include <vector>
#include <cmath>

int int_of_binary(std::vector<int> ii)
{
  int r = 0;
  int power = (int)(std::pow(2,ii.size()-1));
  int sum = 0;
  for (auto i: ii) {
    sum += (power * i);
    power /= 2;
  }
  return sum;
}

int main()
{
  std::vector<int> zeros = {0,0,0,0,0,0,0,0,0,0,0,0};
  std::vector<int> ones  = {0,0,0,0,0,0,0,0,0,0,0,0};  
  std::string line;

  while (std::getline(std::cin, line)) {
    std::vector<char> vv(line.begin(), line.end());
    uint i = 0; 
    for (auto v: vv) {
      if (v == '0') {
	zeros[i] += 1;
      } else {
	ones[i] += 1;
      }
      i++;
    }
  }
  
  std::vector<int> gamma = {0,0,0,0,0,0,0,0,0,0,0,0};
  std::vector<int> delta = {0,0,0,0,0,0,0,0,0,0,0,0};
  
  for (int i=0; i<12; i++) {
    if (zeros[i] > ones[i]) {
      gamma[i] = 0;
      delta[i] = 1;
    } else {
      gamma[i] = 1;
      delta[i] = 0;
    }
  }

  std::cout << "gamma=";
  for (auto i: gamma) {
    std::cout << i;
  }
  auto g = int_of_binary(gamma);
  std::cout << " " << g;
  
  std::cout << " delta=";
  for (auto i: delta) {
    std::cout << i;
  }
  auto d = int_of_binary(delta);
  std::cout << " " << d << " gamma*delta=" << g*d << std::endl;
  
  return 0;
}
