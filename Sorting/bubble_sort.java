import java.lang.*;
public class Sort
{
    public static void bubble_sort(int[] arr)
    {
        int temp;
        boolean swapped;
        do
        {
            swapped=false;
            for(int i = 0; i < arr.length-1; i++)
            {
                if(arr[i] > arr[i+1])
                {
                    temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    swapped = true;
                }
            }
        }while(swapped);
        for(int j=0; j< arr.length; j++){
            System.out.println(arr[j]);
        }
    }

    public static void main(String[] args)
    {
        int[] arr = {4,5,1,3,2, 1};
        bubble_sort(arr);
    }
}