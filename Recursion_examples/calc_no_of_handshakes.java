public class MyClass {
    public static void main(String args[]) {
        int z = calc_num_of_handshakes(5);
        System.out.println("No. of handshakes = " + z);
    }
    public static int calc_num_of_handshakes(int N)
    {
        if(N == 0)
        {
            return 0;
        }
        else
        {
            return(calc_num_of_handshakes(N-1) + N-1);
        }
    }
}