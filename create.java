
/*//program for create a file
import java.io.File;
import java.io.IOException;
public class create
{
    public static void main(String[] args)
    {
        try{
            File Obj=new File("yuva.txt");
            System.out.println(Obj.createNewFile());
            System.out.println(Obj.getName());
             
            
        }
        catch(IOException e)
        {
            System.out.println(e);
        }
    }
}

//program for read a file
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
public class create
{
    public static void main(String[] args)
    {
        try
        {
            File Obj=new File("yuva.txt");
            Scanner Reader=new Scanner(Obj);
            while(Reader.hasNextLine())
            {
                String data=Reader.nextLine();
                System.out.println(data);
            }
            
            Reader.close();
        }
        catch(IOException e)
        {
            System.out.println(e);
        }
    }
}

import java.io.FileWriter;
import java.io.IOException;
public class create
{
    public static void main(String[] args) 
    {
        try
        {
            FileWriter yuvaa=new FileWriter("yuva.txt",true);
            yuvaa.write(" Yuva Copy pannatha....");
            yuvaa.close();
            System.out.println("Succesfully written");
        }
        catch(IOException e)
        {
            System.out.println(e);
        }
        
    }
    System.out.println("This is github");
}*/
import java.util.*;
public class create
{
    public static void main(String[] args)
    { 
        String s1="CSE";
        String s2 ="CSE";
        System.out.println(System.identityHashCode(s1));
        System.out.println(System.identityHashCode(s2)); 
        s1 = "AI";
        System.out.println(s1);
        System.out.println(System.identityHashCode(s1));
        System.out.println(System.identityHashCode(s2)); 
    }
}
