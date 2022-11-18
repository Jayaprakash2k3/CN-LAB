import java.io.*;
import java.net.*;
import java.util.Scanner;
class Client
    {
        public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the Number of Clients:");
            int clients= sc.nextInt();
            for(int i=0;i<clients;i++)
            {
                try
                {
                    DatagramSocket ds = new DatagramSocket();
                    ds.setBroadcast(true);
                    byte [] k="Are you a DHCP Server?".getBytes();
                    DatagramPacket dp = new DatagramPacket(k,k.length,InetAddress.getByName("192.168.0.255"),12345);
                    ds.send(dp);
                }catch(Exception e){System.out.println(e);}  
                }  
                }
            }

