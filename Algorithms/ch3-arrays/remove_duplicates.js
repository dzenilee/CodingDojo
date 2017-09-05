/*
Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. As with all these array challenges, do this without using any built-in array methods.
*/

var arr1 = ['app1', 'app2', 'app3', 'app2']

function remove_duplicates(arr){
  var newArray = [];
  for (var i = 0; i < arr.length; 1++){
    for (var j = 0; i < arr.length-1; 1++){
      if (arr[i] == arr[i+1]){
        arr.pop(i) 
      }
    }
  }
}
