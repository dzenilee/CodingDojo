// There is an old tale about a king who offered a servant $10,000 as a reward. The servant instead asked that for 30 days he be given an amount that would double, starting with a penny. (1 penny for the first day, 2 for the second, 4 for the third, then 8, 16, 32 pennies, and so on).
//
// Use for loops to answer the following:
//
// How much was the reward after 30 days?

var total = 0.01;
for (var day = 1; day < 3; day++){
  total *= 2;
  console.log(total);
}
console.log(total);

day 1: 0.01
day 2: 0.1*2 = 0.2
day 3: 0.2* 2 = 0.4 

day1 = .01
day2 = .02
day3 = .04
--> 0.07
