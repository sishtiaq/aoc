#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>

int int_of_binary(std::vector<int> ii)
{
  int power = (int)(std::pow(2,ii.size()-1));
  int sum = 0;
  for (auto i: ii) {
    sum += (power * i);
    power /= 2;
  }
  return sum;
}  

int int_of_binary(std::string ss)
{
  int power = (int)(std::pow(2,ss.size()-1));
  int sum = 0;
  for (auto s: ss) {
    std::string c(1,s);
    sum += (power * std::stoi(c));
    power /= 2;
  }
  return sum;
}

template<typename T>
void pvec(std::vector<T> ii)
{
  for (auto i: ii) {
    std::cout << i << ',';
  }
  std::cout << " ";
}

std::tuple<std::vector<int>, std::vector<int>> zeroones_per_idx(std::vector<std::string> numbers)
{
  // find how many 0s or 1s per idx.
  int len = numbers[0].size();
  std::vector<int> zeros(len,0);
  std::vector<int> ones(len,0);

  for (auto it = numbers.begin(); it != numbers.end(); ++it) {
    std::vector<char> vv((*it).begin(), (*it).end());
    uint i = 0; 
    for (auto v: vv) {
      if (v == '0') {
	zeros[i] += 1;
      } else {
	ones[i] += 1;
      }
      i++;
    }
  }
  
  return std::make_tuple(zeros, ones);
}

// SI: the $calc$ functions are mostly the same. Should be parametric,
// somehow. 
int calc_o2_generator_rating(std::vector<std::string> numbers)
{
  std::cout << "calc_o2:\n";
  // const uint len = numbers[0].size();
  uint i = 0;
  bool flag = true;
  std::string result;
  
  // ****
  while (flag) {
    uint rm = 0;
    std::cout << "idx:" << i << ", ";
    auto [ zeros, ones ] = zeroones_per_idx(numbers);
    char most_common = (ones[i] >= zeros[i]) ? '1' : '0';
    std::cout << " mc=" << most_common << "\n";
    
    for (auto it = numbers.begin(); it != numbers.end(); ) {
      auto number_char_i = (*it)[i];
      std::cout << "number:" << *it << " ";
      if (number_char_i == most_common) {
	++it;
	std::cout << "\n";	
      } else {
	std::cout << " ** marked for rm\n";
	it = numbers.erase(it);
	++rm;
      }
      if (numbers.size() == 1) {
	std::cout << "one item left ("; pvec<std::string>(numbers); std::cout << ")\n";
	flag = false;
	result = numbers[0];
	break;
      }
    }
    std::cout << rm << " items rm-ed. " << numbers.size() << " items left.\n";
    ++i;
  }
  
  return int_of_binary(result);
}

int calc_co2_scrubber_rating(std::vector<std::string> numbers)
{
  std::cout << "calc_co2:\n";
  //  const uint len = numbers[0].size();
  uint i = 0;
  bool flag = true;
  std::string result;
  
  // ****
  while (flag) {
    uint rm = 0;
    std::cout << "idx:" << i << ", ";
    auto [ zeros, ones ] = zeroones_per_idx(numbers);
    char least_common = (zeros[i] <= ones[i]) ? '0' : '1';
    std::cout << " lc=" << least_common << "\n";
    
    for (auto it = numbers.begin(); it != numbers.end(); ) {
      auto number_char_i = (*it)[i];
      std::cout << "number:" << *it << " ";
      if (number_char_i == least_common) {
	++it;
	std::cout << "\n";	
      } else {
	std::cout << " ** marked for rm\n";
	it = numbers.erase(it);
	++rm;
      }
      if (numbers.size() == 1) {
	std::cout << "one item left ("; pvec<std::string>(numbers); std::cout << ")\n";
	flag = false;
	result = numbers[0];
	break;
      }
    }
    std::cout << rm << " items rm-ed. " << numbers.size() << " items left.\n";
    ++i;
  }
  
  return int_of_binary(result);
}



int main()
{
  std::string line;
  std::vector<std::string> numbers;

  while (std::getline(std::cin, line)) {
    numbers.push_back(line);
  }
  std::cout << "numbers: "; pvec<std::string>(numbers); std::cout << std::endl;
  
  int o2_generator_rating = calc_o2_generator_rating(numbers);
  std::cout << "o2_gen_rating=" << o2_generator_rating << '\n';
  int co2_scrubber_rating = calc_co2_scrubber_rating(numbers);
  std::cout << "co2_scrubber_rating=" << co2_scrubber_rating << '\n';
  
  int life_support_rating = o2_generator_rating * co2_scrubber_rating;
  std::cout << "life_support_rating=" << life_support_rating << '\n';  
  return life_support_rating;

}
