#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <array>

template<class T>
void pr_vec(std::vector<T> ii)
{
  for (auto i: ii) {
    std::cout << i;
  }
}

// split "n,m,..." into a vector of ints.
// n,m are numbers. delim is some "," delim.
std::vector<int> parse_draws(std::string line, char delim) {
  std::vector<int> draws;
  std::istringstream iss(line); 
  for (std::string word; std::getline(iss, word, ',');) {
    draws.push_back(std::stoi(word));
  }

  return draws;
}



// 5x5 board
typedef std::array<std::array<int,5>,5> board_t;

struct game {
  std::vector<int> draws;
  std::vector<std::array<std::array<int,5>,5>> boards;
  std::vector<std::array<std::array<int,5>,5>> marked;  
};

void pr_board(std::array<std::array<int,5>,5> board)
{
  std::cout << "Board: "; 
  for(int i=0; i<5; i++) {
    for(int j=0; j<5; j++) {
      std::cout << board[i][j] << " ";
    }
  }
  std::cout << "\n"; 
}

void pr_game(game &g)
{
  pr_vec(g.draws); std::cout << '\n';
  for (auto b: g.boards) {
    pr_board(b);
    std::cout << '\n';    
  }
}

// 5 numbers per line
std::array<int,5> mk_row(std::string line) {
  std::array<int,5> a;
  std::istringstream iss(line);
  int i = 0;
  std::string word;
  while (std::getline(iss, word, ' ')) {
    if (word.empty()) continue;
    a[i] = std::stoi(word);
    i++;
  }
  return a;
}


void parse_game(game& g)
{
  std::cout << "parsing draws\n";
  std::string draw_line;
  std::vector<int> draws;
  std::getline(std::cin,draw_line);
  draws = parse_draws(draw_line, ',');

  std::cout << "getting boards\n";
  std::vector<std::array<std::array<int,5>,5>> boards;  
  // get all boards
  std::string line;
  while (std::getline(std::cin, line)) {
    // beginning of board
    if (line.empty()) {
      std::array<std::array<int,5>,5> board;
      for (int i=0; i<5; i++) {
	std::string board_line;
	std::getline(std::cin, board_line);
	std::array<int,5> row;
	row = mk_row(board_line); // relying upon move
	board[i] = row;
      }
      boards.push_back(board);
    }
  }

  g.draws = draws;
  g.boards = boards;
  g.marked = {{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}};
  
}

int main()
{
  game g;
  parse_game(g);
  pr_game(g);

  return 0;
}
