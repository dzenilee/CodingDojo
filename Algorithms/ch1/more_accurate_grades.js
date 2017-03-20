// For an additional challenge, add ‘-’ signs to scores in the bottom two percent of A, B, C and D scores, and “ +” signs to the top two percent of B, C and D scores (sorry, Mr. Cerise never gives an A+).
//
// Example: Given 88, console.log "Score: 88. Grade: B+". Given 61, log "Score: 61. Grade: D-".

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
