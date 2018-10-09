import java.util.*;
public class Test
{
    public static void main( String args[] )
    {
        int l, r, n ,i;
        int flag = 0;
        ArrayList prime_list = new ArrayList(); 
        System.out.println("Enter lower and upper limits:\n");
        l = Integer.parseInt("1");
        r = Integer.parseInt("10");
        for( n=l; n<=r; n++ )
        {
            for( i=2; i <= n/2; i++ )
            {
                if( n % i == 0 )
                {
                    flag = 1;
                    break;
                }
            }
            System.out.println(n);
            if(flag == 1)
            {
                System.out.println("is not prime");
                prime_list.add(new Integer(n));
                flag=0;
            }
            else
            {
                System.out.println("is prime");
            }
        }
        System.out.println("No: of prime numbers: ");
        System.out.println( prime_list.size() );
    }
}

