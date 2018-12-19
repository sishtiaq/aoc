#include <iostream>
#include <string>


int main()
{
  std::string line;
  int sum = 0; 
  while (std::getline(std::cin, line)) {
    int n = std::stoi(line);
    sum += n;
    std::cout << "n=" << n << ", sum=" << sum << '\n'; 
  }

  return 0;
}
