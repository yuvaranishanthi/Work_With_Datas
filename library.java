import java.util.*;

interface LibraryItem
{
  String getTitle();
  void setTitle(String Title);
  void displayInfo();
}
class Book implements LibraryItem
{
  private String Title;

  public String getTitle()
  {
    return Title;
  }
  public void setTitle(String Title)
  {
    this.Title=Title;
  }
   public void displayInfo()
  {
    System.out.println("book:"+ Title);
  }
}
class CD implements LibraryItem
{
  private String Title;
  public String getTitle()
  {
    return Title;
  }
  public void setTitle(String Title)
  {
    this.Title=Title;
  }
   public void displayInfo()
  {
    System.out.println("CD:"+ Title);
  }
}
class DVD implements LibraryItem
{
  private String Title;
  public String getTitle()
  {
    return Title;
  }
   public void setTitle(String Title)
  {
    this.Title = Title;
  }
   public void displayInfo()
  {
    System.out.println("DVD:"+ Title);
  }
}
public class library
{
    public static void main(String[] args)
    {
        Book book=new Book();
        book.setTitle("this is the library book!!!");
        CD cd=new CD();
        cd.setTitle("this is library cd!");
        DVD dvd=new DVD();
        dvd.setTitle("This is library DVD!");

        book.displayInfo();
        cd.displayInfo();
        dvd.displayInfo();
    }
}