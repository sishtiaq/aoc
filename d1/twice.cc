#include <iostream>
#include <string>
#include <set>


int main()
{
  std::string line;
  std::multiset<int> m;
  int sum = 0 ;
  
  while (std::getline(std::cin, line)) {
    int n = std::stoi(line);
    sum += n;
    std::cout << "n=" << n <<"\tsum=" << sum ;
    m.insert(sum);
    if (m.count(sum) == 2) {
      std::cout << "\t#" << sum << " = 2";
    }      

    std::cout << '\n'; 
  }

  return 0;
}
