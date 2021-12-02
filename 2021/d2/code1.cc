#include <iostream>
#include <string>
#include <map>


int main()
{
  std::map<std::string, int> parse_op {
    {"forward", 1},
    {"down", 2},
    {"up", 4},
  };
  
  int h = 0;
  int d = 0;
  std::string cmd;
  int num = 0;
  while (std::cin >> cmd >> num) {
    std::cout << cmd << ":" << num << '\n';
    // SI: could have string->op map
    int op = parse_op[cmd];
    switch (op) {
    case 1: h += num; break;
    case 2: d += num; break;
    case 4: d -= num; break;
    default:
      std::cout << "error: " << cmd << " " << num << std::endl;
      break;
    }
  }

  std::cout << "h:" << h << " 8 d:" << d << " = " << h*d << std::endl;

  return 0;
}
