public class Test{

   public static void main(String args[]){
      int rem, sum=0;
      int num=1234;
      while(num>0)
      {
          rem = num % 10;
          sum = sum + rem;
          num = num / 10;
      }
      System.out.println(sum); 
   }
}