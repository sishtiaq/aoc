#include <iostream>
#include <string>


int main()
{
  std::string line;
  int prev = 0;
  int larger=0;
  while (std::getline(std::cin, line)) {
    int n = std::stoi(line);
    if (n > prev) {
      larger++;
      std::cout << n << ">" << prev << '\n'; 
    }
    prev = n;
  }

  std::cout << "larger=" << larger << std::endl;
  return 0;
}
