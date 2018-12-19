#include <iostream>
#include <string>
#include <set>
#include <cassert> 

unsigned int diff(const std::string s, const std::string t)
{
    assert(s.length() == t.length());
    unsigned int d = 0;
    for (auto i=0; i<s.length(); i++) {
        if (s[i] != t[i]) { 
            d++;
        }
    }
    return d;
}

std::string common(const std::string s, const std::string t)
{
    std::string c;
    assert(s.length() == t.length());
    for (auto i=0; i<s.length(); i++) {
        if (s[i] == t[i]) { 
            c += s[i]; 
        }
    }
    return c;
}

int main()
{
  std::string line;
  std::set<std::string> ss; 
  
  // put all lines into ss. 
  while (std::getline(std::cin, line)) {
      ss.insert(line);
  }

  // O(n^2)
  for (auto &s : ss) { 
    std::cout << "Considering " << s << " "; 
    std::set<std::string> ss_s = ss;
    ss_s.erase(s); 
    for (auto &t : ss_s) { 
        if (diff(s,t) ==  1) {
            std::cout << s << " - " << t << " ==  1. "  
                << "common = " << common(s,t) << " "; 
        }
    }
    std::cout << "\n"; 
  }
}

