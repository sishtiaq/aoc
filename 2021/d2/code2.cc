#include <iostream>
#include <string>
#include <map>


enum op { OP_FWD, OP_DOWN, OP_UP };
std::map<std::string, int> parse_op {
  {"forward", OP_FWD},
  {"down", OP_DOWN},
  {"up", OP_UP},
};

int main()
{
  // state
  int aim = 0;
  int horizontal = 0;
  int depth = 0;

  std::string cmd;
  int num = 0;

  while (std::cin >> cmd >> num) {
    std::cout << cmd << ":" << num << '\n';
    int op = parse_op[cmd];
    switch (op) {
    case OP_DOWN: {
      aim += num;
      break;
    };
    case OP_UP: {
      aim -= num;
      break;
    };
    case OP_FWD: {
      horizontal += num;
      depth += (aim * num);
      break; 
    };
    default:
      std::cout << "error: " << cmd << " " << num << std::endl;
      break;
    }
  }

  std::cout << "(aim,horizontal,depth) horizontal*depth= (" << aim << "," << horizontal << "," << depth << ") " << horizontal*depth << std::endl;

  return 0;
}
