// Mr. Cerise teaches high school math. Write a function that assigns and prints a letter grade, given an integer representing a score from 0 to 100? Those getting 90+ get an ‘A’, 80-89 earn ‘B’, 70-79 is a ‘C’, 60-69 should get a ‘D’, and lower than 60 receive ‘F’.
//
// Example: given 88, you should log "Score:88. Grade: B". Given the score 61, log the string "Score: 61. Grade: D".

function letter_grade(num){
  if (num >= 90){
    var grade = 'A';
  } else if (num >= 80){
    var grade = 'B';
  } else if (num >= 70){
    var grade = 'C';
  } else if (num >= 60){
    var grade = 'D';
  } else {
    var grade = 'F'
  }
  console.log("Score: " + num + ". Grade: " + grade);
}

letter_grade(99);
letter_grade(61);
