using System;
using System.Text;
using System.Net.Sockets;
using System.Net;
// check whether all required namespaces are imported
namespace Client
{
public class SynchronousSocketClient
{

    public static void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            // check if the port is defined or not
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 8080);

            // Check whether TCP Socket is created correctly
            Socket sender = new Socket(ipAddress.AddressFamily,SocketType.Stream, ProtocolType.Tcp);

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                sender.Connect(remoteEP);

                Console.WriteLine("Socket connected to {0}",
                    sender.RemoteEndPoint.ToString());

                // check if the variable is defined correctly or not
                Console.WriteLine("Enter the Person Name: ");
                string name = Console.ReadLine();
                Console.WriteLine("Enter the Person Intrest: ");
                string intrests = Console.ReadLine();
                Console.WriteLine("Enter the Person Email: ");
                string mail = Console.ReadLine();
                // Encode the data string into a byte array.  
                // check the data type of the data you are sending.
                byte[] msg = Encoding.ASCII.GetBytes(name + "," + intrests + "," + mail);

                // Send the data through the socket.  
                int bytesSent = sender.Send(msg);

                //int bytesRec = sender.Receive(bytes);
                //Console.Writeline("Echoed test = {0}",Encoding.ASCII.GetString(bytes,0,bytesRec));

                // Close the socket.
                sender.Shutdown(SocketShutdown.Both);
                sender.Close();

            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    // check the main function
    public static int Main(String[] args)
    {
        StartClient();
        return 0;
    }
}
}