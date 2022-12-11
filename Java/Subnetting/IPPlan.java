import java.util.*;
class IPPlan
    {
        public static void main(String args[])
        {
            List<Integer> hosts = new ArrayList<Integer>();
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the Base Class C IP Address:");
            // Since the Plan is for Mid-Size Org Enter upto 3 octant eg. 196.168.12
            String s=sc.next();
            System.out.println("Enter the Number of Subnets Required:");
            int a=sc.nextInt();
            for(int i=0;i<a;i++)
            {
                System.out.println("Enter Number of Hosts in Subnet-"+(i+1)+":");
                hosts.add(sc.nextInt());
            }
            int total=0;
            for(int k :hosts)
                total+=k;
                
            if(total>253)
                System.out.println("Total Host must be less than or equal to 252");
            else
            {
            int prev=0;
            for(int k=0;k<hosts.size();k++)
            {
                int minHost=(int)Math.pow(2,Math.ceil((Math.log(hosts.get(k)+2) / Math.log(2))));
                System.out.println("Range for Subnet-"+k+" is "+s+"."+prev+"-"+(prev+minHost-1));
                prev+=minHost; 
                //(k+2) since fist and last is not usable 
                }


            }
            sc.close();

        }
    }