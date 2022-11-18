import java.net.*;
import java.util.*;
class DHCPServer
    {
        public static void main(String args[]) throws Exception
        {
            final String ip="192.167.23.";
            List<Integer> assigned = new ArrayList<Integer>();  
            Random rand = new Random();                      
            DatagramSocket ds = new DatagramSocket(12345);
            byte[] receive = new byte[65535];
            DatagramPacket dp = new DatagramPacket(receive, receive.length);
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter number of Client:");
            int client=sc.nextInt();
            for(int i=0;i<client;i++)
            {            
            ds.receive(dp);
            String r=decode(dp);
            if(r.equals("Are you a DHCP Server?"))
                {   
                    int rd=1;
                    while(assigned.contains(rd))
                    {
                     rd=rand.nextInt(1,254);
                    }
                    String available=ip+Integer.toString(rd);
                    DatagramPacket dp2 = new DatagramPacket(available.getBytes(),available.length(),InetAddress.getByName("127.0.0.1"),12346);
                    ds.send(dp2);
                    ds.receive(dp);
                    String q= decode(dp);
                    if(q.equals("Okay for me :-)"))
                    {
                        dp2 = new DatagramPacket("Assigned for You".getBytes(),"Assigned for You".length(),InetAddress.getByName("127.0.0.1"),12346);
                        ds.send(dp2);
                        assigned.add(rd);

                    }  
                }
       
            }
            ds.close();
        }
        public static String decode(DatagramPacket dp)
        {
            String str = new String(dp.getData(), 0, dp.getLength());
            System.out.println("From Client:"+str);
            return str;  
        }
        
    }
    