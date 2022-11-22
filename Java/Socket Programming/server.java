import java.io.*;
import java.net.*;
class server
    {
        public static void main(String args[])
        {
            try{ 
                ServerSocket ss=new ServerSocket(12345);  
                Socket s=ss.accept();
                System.out.println("Connected to "+s);
                DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
                dout.writeUTF("Thanks for Connecting");  
                ss.close();  
                }catch(Exception e){System.out.println(e);}  
                }
        }
    