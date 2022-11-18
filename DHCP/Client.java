import java.net.*;
import java.util.Scanner;
class Client
    {
        public static void main(String args[]) throws Exception
        {
            Scanner sc = new Scanner(System.in);
            DatagramSocket ds = new DatagramSocket(12346);
            String k="Are you a DHCP Server?";
            DatagramPacket dp = new DatagramPacket(k.getBytes(),k.length(),InetAddress.getByName("255.255.255.255"),12345);
            byte[] receive = new byte[65535];
            DatagramPacket dp2 = new DatagramPacket(receive, receive.length);
            DatagramPacket dp3 = new DatagramPacket("Okay for me :-)".getBytes(),"Okay for me :-)".length(),InetAddress.getByName("127.0.0.1"),12345);
            System.out.println("Enter the Number of Clients:");
            int clients= sc.nextInt();
            for(int i=0;i<clients;i++)
            {                                
                    ds.send(dp);  // P1: BroadCast for Discovery
                    ds.receive(dp2); // P2: Gets the Available Address

                    if(decode(dp2)!=null)
                    {
                        ds.send(dp3); // P3: Sends the Selected Address
                        ds.receive(dp2);// P4: Acknowledgement Received 
                        decode(dp2); 

                    }
                   
          
        }  
        ds.close();
                }
        
        public static String decode(DatagramPacket dp)
        {
            String str = new String(dp.getData(), 0, dp.getLength());
            System.out.println("From Server: "+str);
            return str;  
        }
        }

