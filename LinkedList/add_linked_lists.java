import java.util.*;
public class LinkedList
{
	//Class variables for the Linked List
	private static Node head;
	private static int numNodes;
	private static String num1_str;
	private static String num2_str;
	private static int sum;
	private static String sum_str;

	public static void main(String [] args)
	{
		//System.out.println("/=/=/=/= TESTING /=/=/=/=");
		LinkedList num1 = new LinkedList(3);
		LinkedList l;
		num1.addAtHead(6);
		num1.addAtHead(1);
		num1.addAtHead(7);
		num1_str = num1.generate_num(head);
		//System.out.println(num1_str);

		LinkedList num2 = new LinkedList(3);
		num1.addAtHead(2);
		num2.addAtHead(9);
		num2.addAtHead(5);
		num2_str = num2.generate_num(head);
		//System.out.println(num2_str);
		sum = Integer.parseInt(num1_str) + Integer.parseInt(num2_str);
		sum_str = Integer.toString(sum);
		//System.out.println(sum_str);
		LinkedList.calc_result(sum_str);
	}

	public LinkedList(Object dat)
	{
		head = new Node(dat);
	}

	public int add(int num1, int num2)
	{
	    return (num1 + num2);
	}

	public static void calc_result(String res)
	{
	    //System.out.println(res.charAt(0));
	    int s;
	    LinkedList result = new LinkedList(res.length());
	    for( s=0; s<res.length(); s++ )
	    {
	       result.addAtHead(res.charAt(s));
	    }
	    printList(head);

	}

	public String generate_num(Node num)
	{
	    String num_str="";
	    Stack s = new Stack();
	    while(num.next != null)
	    {
	        //System.out.println(num.data);
	        s.push(num.data);
	        num = num.next;
	    }
	    while(!s.empty())
	    {
	        num_str += s.pop();
	    }
	    return(num_str);
	}

	public void addAtHead(Object dat)
	{
		Node temp = head;
		head = new Node(dat);
		head.next = temp;
		numNodes++;
	}

	public static void printList(Node v)
	{
		Node temp = v;
		while(temp.next != null)
		{
			System.out.print(temp.data);
			//System.out.print("-->");
			temp = temp.next;
		}
	}


	class Node
	{
		//Declare class variables
		private Node next;
		private Object data;

		public Node(Object dat)
		{
			data = dat;
		}

		public Object getData()
		{
			return data;
		}
	}
}