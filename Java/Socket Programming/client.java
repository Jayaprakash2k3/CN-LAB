import java.io.*;
import java.net.*;
class client
    {
        public static void main(String args[])
        {

            try{      
                Socket s=new Socket("localhost",12345);  
                DataInputStream din=new DataInputStream(s.getInputStream());  
                String msg=(String)din.readUTF();
                System.out.println(msg);
                din.close();  
                s.close();  
                }catch(Exception e){System.out.println(e);}  
                }  

        }
    