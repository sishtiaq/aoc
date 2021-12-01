#include <iostream>
#include <string>
#include <vector>

int main()
{
  std::string line;
  std::vector<int> vv;
  int larger=0;
  while (std::getline(std::cin, line)) {
    int n = std::stoi(line);
    vv.push_back(n);
  }
  std::cout << "Got " << vv.size() << std::endl;

  for (unsigned int i = 0; i < vv.size() -3; i++) {
    //    std::cout << vv[i+3] << " " << vv[i] << std::endl;
    if (vv[i+3] > vv[i]) {
      larger++;
      std::cout << vv[i+3] << ">" << vv[i] << '\n';       
    }
  }

  std::cout << "larger=" << larger << std::endl;
  return 0;
}
