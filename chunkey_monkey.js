/*Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

Example:

#1 chunkArrayInGroups(["a", "b", "c", "d"], 2) should return [["a", "b"], ["c", "d"]]

#2 chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3) should return [[0, 1, 2], [3, 4, 5]]

#3 chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) should return [[0, 1], [2, 3], [4, 5]]

#4 chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4) should return [[0, 1, 2, 3], [4, 5]]

*/

function chunkArrayInGroups(arr, size) {
    //need to sequentially fill this array with sub-arrays containing elements of 'arr' and of length === size.
    var arr_answer = [];
    //loop through the 'arr' and push each element into the arr_answer until the arr_answer is full. 
    for (var i = 0; i < arr.length; i++) {
      /*we splice and push sub-arrays containing 'arr' elements. We pass 'size' as the 2nd parameter of the .splice method which is the number of elements to splice. We repeat size as the 3rd parameter of the splice method to which is the number of copied elements we want to add to the array being returned i.e the sub-array to push to the arr_answer.*/
      arr_answer.push(arr.splice(i,size,size));
    }
    return arr_answer;
  }
  
  /*log to console and pass in an array as the first arg and specify any number you want as the second arg. 
  A constraint exists in that the size of the array passed is the maximum value the 2nd arg can be. 
  So, if you pass an array of 4 elements but pass the 2nd arg as a value of 5, you'll get an array with sub-array === to the arr arg passed.
  Which is correct since the loop ends when there are no more elements left in the passed array. We wanted an array filled with sub-arrays of 5
  sequential elements from passed array, however there's only 4 elements in passed array, so you'll get all of them and then loop ends.*/
  chunkArrayInGroups(["a", "b", "c", "d"], 2);

//this was one of the first JS algorithms i wrote and i'm proud of this one.