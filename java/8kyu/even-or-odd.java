//Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

//My solution

class EvenOrOdd {
    public static String even_or_odd(int number) {
        if (number % 2 == 0) {
          return "Even";
        }else {
          return "Odd";
        }
        
    }
}

//My 2nd solution

class EvenOrOdd2 {
    public static String even_or_odd(int number) {
        return number % 2 == 0 ? "Even" : "Odd";
    }
}