import java.util.*;
public class employee
{
    String emp_name;
    int emp_id;
    int emp_contro;
    int emp_sal;
    public void info (n,id,contro,sal)
    {
        emp_name=n;
        emp_id=id;
        emp_contro=contro;
        emp_sal=sal;
    }
    public void display()
 
 {
    System.out.println("emp_name" + n);
    System.out.println("emp_id" + id);
    System.out.println("emp_contro" + contro);
    System.out.println("emp_sal" + sal);
 }
 public static void main(String[] args)
{
  
  employee e1= new employee();
  employee e2= new employee();
  e1.info("aazil","19","123456", "2345");
   e2.info("aazi", "18", "1234456", "23450");

  e1.display();
  e2.display();
}
}






   
