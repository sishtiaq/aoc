#include <iostream>
#include <string>


int main()
{
  std::string line;
  int h = 0;
  int d = 0;
  std::string cmd;
  int num = 0;
  while (std::cin >> cmd >> num) {
    std::cout << cmd << ":" << num << '\n';
    if (cmd == "forward") {
      h += num;
    } else if (cmd == "down") {
      d += num;
    } else if (cmd == "up") {
      d -= num;
    } else {
      std::cout << "error: " << cmd << " " << num << std::endl;
    }
  }

  std::cout << "h:" << h << " 8 d:" << d << " = " << h*d << std::endl;

  return 0;
}
