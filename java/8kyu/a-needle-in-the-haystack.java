//Can you find the needle in the haystack?

//Write a function findNeedle() that takes an array full of junk but containing one "needle"

//After your function finds the needle it should return a message (as a string) that says:

//"found the needle at position " plus the index it found the needle, so:

//Example(Input --> Output)

//["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

//My solution

//We travel the haystack array untile the element (i) equals "needle", so that we return the index of the element
//converted into string.
class Kata {
    public static String findNeedle(Object[] haystack) {
      String solution = new String();
      for (int i = 0; i < haystack.length; i++) {
        if (haystack[i] == "needle") {
          solution = "found the needle at position " + String.valueOf(i);
        }
      }
      return solution;
    }
  }
