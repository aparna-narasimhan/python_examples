import java.util.*;
import java.io.*;
public class SetDemo {

  public static void main(String args[]) {
      int orig_len;
      int new_len;
      String str = new String("bhar");
      orig_len = str.length();
      Set<Character> set = new HashSet<Character>();
      for(int c=0; c < str.length(); c++)
		  set.add(str.charAt(c));
      new_len = set.size();
      if( orig_len == new_len )
      {
      System.out.println("String is unique");
      }
      else
      {
      System.out.println("String is not unique");
      }



  }
}