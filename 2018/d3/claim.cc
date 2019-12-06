#include <iostream>
#include <string>
#include <vector>
#include <sstream>

//const int M=1000;
 const int M=8;


class Claim
{
  public: 
    Claim(int claim, int x, int y, int w, int h) {
      m_claim = claim;
      // zero all
      for (auto i=0; i<M; i++) {
        for (auto j=0; j<M; j++) {
          m[i][j] = 0;
        }
      }
      // set some
      for (auto i=x; i<x+h; i++) {
        for (auto j=y; j<y+w; j++) { 
          m[i][j] = claim; 
        }
      }

    }

    void print() {
      for (auto i=0; i<M; i++) {
        for (auto j=0; j<M; j++) {
          auto d = m[i][j]; 
          std::string s; 
          switch (d) {
            case -1 : s = "X"; break; 
            case 0 : s = "-"; break;
            default : s = std::to_string(d); break; 
          }
          std::cout << s << " "; 
        }
        std::cout << '\n';
      }
    }

    void overlap(Claim& that)
    {
      for (auto i=0; i<M; i++) {
        for (auto j=0; j<M; j++) {
          if (m[i][j] != 0 && that.m[i][j] != 0) {
            m[i][j] = -1;
          }
          if (m[i][j] != 0 && that.m[i][j] == 0) {
            // m[i][j] = 
          }
          if (m[i][j] == 0 && that.m[i][j] != 0) {
            m[i][j] = that.m[i][j]; 
          }          
        }
      }
    }

  protected:  
    int m_claim;
    int m[M][M]; 
};

// #123 @ 3,2: 5x4 
Claim parse(std::string l)
{
  std::string drop; 
  int claim;
  int x, y;
  int w, h;
  std::stringstream s(l); 
  // Every number seems to be uniquely seprarated. 
  std::getline(s,drop,'#'); 
  s >> claim;
  std::getline(s,drop,'@');
  s >> y;
  std::getline(s,drop,',');
  s >> x; 
  std::getline(s,drop,':');
  s >> w; 
  std::getline(s,drop,'x');
  s >> h; 
  std::getline(s,drop);
  std::cout << "#" << claim << " @ " << y << "," << x << ": " << w << "x" << h << '\n';
  // return Claim(claim,x,y,w,h);
  return Claim(claim,0,0,0,0); 
}

int main()
{
  std::string line;
  std::vector<Claim> claims;

  // accumlator
  Claim r(0,0,0,0,0);   
  claims.push_back(r); 

  // get and store all claims
  while (std::getline(std::cin, line)) {
    Claim c = parse(line);
    claims.push_back(c);
  }

  std::cout << "Got all claims\n";
  for (auto c : claims) { 
    c.print(); 
    std::cout << "\n";
  }

  // accumlate.   
  for (auto c : claims) {
    r.overlap(c);
  }
  r.print(); 
}

