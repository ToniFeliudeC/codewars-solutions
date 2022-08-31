//You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
//We want to create the text that should be displayed next to such an item.

//Implement the function which takes an array containing the names of people that like an item.
//It must return the display text as shown in the examples:

//[]                                -->  "no one likes this"
//["Peter"]                         -->  "Peter likes this"
//["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
//["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
//["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
//Note: For 4 or more names, the number in "and 2 others" simply increases.

//My solution

class Solution {
    public static String whoLikesIt(String... names) {
      //In case no one likes it we just need to return the an static string "no one likes this".
      if (names.length == 0) {
        return "no one likes this";
      }

      //In case only 1 person likes it, we can just return the 1st and only string of the list "names" and add the string " likes it".
      else if (names.length == 1) {
        return names[0] + " likes this";
      }

      //In case 2 people like it, we concatenate both elements of the list "names" with the string " and ", after that, we add the string " like this" at the end.
      else if (names.length == 2) {
        return names[0] + " and " + names[1] + " like this";
      }

      //In case 3 people like it we repeat the same process as for "2 people case" but the first concatenaion being made with a ", ".
      else if (names.length == 3) {
        return names[0] + ", " + names[1] + " and " + names[2] + " like this";
      }

      //In case more than 3 people like it we concatenate the first 2 elements with a ", ".
      //Then we concatenate the resulting string with the number of elements in the array "names" having substracted 2, 
      //since those are already  mentioned on the names.
      //Then we concatenate all of that with " others like this".
      else {
        return names[0] + ", " + names[1] + " and " + (names.length-2) + " others like this";
      }
    }
}