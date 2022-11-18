import java.net.*;
import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
class DHCPServer
    {
        public static void main(String args[])
        {
            final String ip="192.167.23.0";
            Map <String,Integer> mp = new HashMap<String,Integer>();
            int a[]= new int[253];
            for(int i=0;i<a.length;i++)
                a[i]=i+1;            
                        
            try
            {
                DatagramSocket ds = new DatagramSocket();
                byte[] receive = new byte[65535];
                DatagramPacket DpReceive = null;
                DpReceive = new DatagramPacket(receive, receive.length);
                ds.receive(DpReceive);
                System.out.println("Client:-" + data(receive));

            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }
        public static StringBuilder data(byte[] a)
        {
            if (a == null)
                return null;
            StringBuilder ret = new StringBuilder();
            int i = 0;
            while (a[i] != 0)
            {
                ret.append((char) a[i]);
                i++;
            }
            return ret;
        }
    }
    