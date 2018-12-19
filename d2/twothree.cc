#include <iostream>
#include <string>
#include <map>


int main()
{
  std::string line;
  unsigned int two=0, three=0;
  
  while (std::getline(std::cin, line)) {
    std::map<char,int> m;
    // parse line
    for (unsigned int i=0; i<line.length(); i++) {
      char c = line[i];
      std::cout << "char:" << c << " ";
      auto search = m.find(c); 
      if (search != m.end()) {
	      m[c] = m[c]+1;
            std::cout << "updated. ";
      } else {
	      m[c] = 1;
            std::cout << "inited. ";
      }
    }

    // if there are any 2s or 3s in this line, add them to the count. Once.  
    bool btwo = false, bthree = false;
    for (auto &kv : m) {
      auto k = kv.first;
      auto v = kv.second;
      if (v == 2) {
            btwo = true;
      }
      if (v == 3) {
            bthree = true;
      }
      std::cout << k << "->" << v << " ";
    }
    if (btwo) two++;
    if (bthree) three++;
    std::cout << std::endl;
  }
  std::cout << "#2=" << two << " #3=" << three << "\n";
}

