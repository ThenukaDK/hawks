
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import gnu.io.CommPortIdentifier;
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent;
import gnu.io.SerialPortEventListener;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Enumeration;
import java.util.concurrent.TimeUnit;


public class SerialConnect implements SerialPortEventListener {

    SerialPort serialPort;

    private static final String PORT_NAMES[] = {
        "/dev/tty.usbserial-A9007UX1", // Mac OS X
        "/dev/ttyACM0", // Raspberry Pi
        "/dev/ttyUSB0", // Linux
        "COM11", // Windows
    };
    //read byte and convert to char
    private BufferedReader input;

    //send output to port
    private OutputStream output;
  
    //wait for port open
    private static final int TIME_OUT = 2000;

    //data rate
    private static final int DATA_RATE = 9600;

    public void initialize() {

        CommPortIdentifier portId = null;
        Enumeration portEnum = CommPortIdentifier.getPortIdentifiers();

       //port put into port_name
        while (portEnum.hasMoreElements()) {
            CommPortIdentifier currPortId = (CommPortIdentifier) portEnum.nextElement();
            for (String portName : PORT_NAMES) {
                if (currPortId.getName().equals(portName)) {
                    portId = currPortId;
                    break;
                }
            }
        }
        
        //if port not exist
        if (portId == null) {
            System.out.println("Could not find COM port.");
            return;
        }

        try {
            // open serial port
            serialPort = (SerialPort) portId.open(this.getClass().getName(),
                    TIME_OUT);

           
            serialPort.setSerialPortParams(DATA_RATE,
                    SerialPort.DATABITS_8,
                    SerialPort.STOPBITS_1,
                    SerialPort.PARITY_NONE);

            // open the streams
            input = new BufferedReader(new InputStreamReader(serialPort.getInputStream()));
            output = serialPort.getOutputStream();

            // add event listeners
            serialPort.addEventListener(this);
            serialPort.notifyOnDataAvailable(true);
        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }

  /// if the port is stop it will remove from os assinging
    public synchronized void close() {
        if (serialPort != null) {
            serialPort.removeEventListener();
            serialPort.close();
        }
    }

 //get rfid data
    public synchronized void serialEvent(SerialPortEvent oEvent) {

        if (oEvent.getEventType() == SerialPortEvent.DATA_AVAILABLE) {
            try {
                String inputLine = input.readLine();
                String output = inputLine;

                String rfid = "95E8287722";

                System.out.println(inputLine);

                if (output.equals(rfid) && geth() == 0) {

                    seth(1);
                    System.out.println("hotspot on");
                    
                    //caling hotsopt create
                    hoon();
                    System.out.println("wait .....");
                    
                    //wait for image transfer
                    TimeUnit.SECONDS.sleep(200);

                    //calling off hotspot
                    System.out.println("offf hotspot");
                    hooff();
                    
                    
                    System.out.println("h " + geth());
                    
                    
                    //if the rfid detect again within time period it will not swtich on again
                    //if other card detected it will show error message
                } else if (output.equals(rfid) && geth() == 1) {
                    System.out.println("card again");
                } else {
                    System.out.println("hotspot off or unidentify card");
                    seth(0);
                }

                // System.out.println("final hotspot off");
                //ui.setMyLabel(output);
            } catch (Exception e) {
                System.err.println(e.toString());
            }
        }

    }
    
    //variale for detecting 
    public int ho;

    public void seth(int a) {
        ho = a;
    }

    public int geth() {
        return ho;
    }

    
  
    public void hoon() {
        try {

            //creating hotspot start
            String cmd = "cmd /c start";
            System.out.println("-- Setting up WLAN --");

 
            String netshCommand = "netsh wlan set hostednetwork mode=allow ssid=\"t3\" key=\"123456789";

            Process p1 = Runtime.getRuntime().exec(cmd + " " + netshCommand);
            p1.waitFor();

            System.out.println("-- Starting WLAN --");
            netshCommand = "netsh wlan start hostednetwork";
            Process p2 = Runtime.getRuntime().exec(cmd + " " + netshCommand);
 

            System.out.println("-- Finished --");


        } catch (Exception ex) {
            System.out.println("Error creating hotspot");
        }

    }

    public void hooff() {
        try {
            String cmd = "cmd /c start";
            System.out.println("-- Stoping WLAN --");

                 
            String netshCommand = "netsh wlan stop hostednetwork";
            Process p2 = Runtime.getRuntime().exec(cmd + " " + netshCommand);
    

            System.out.println("-- Finished --");


        } catch (Exception ex) {
            System.out.println("Error stoping hotspot");
        }
    }

    public static void main(String[] args) throws Exception {

        SerialConnect main = new SerialConnect();
        main.initialize();
        Thread t = new Thread() {
            public void run() {
                //the following line will keep this app alive for 1000 seconds,
                //waiting for events to occur and responding to them (printing incoming messages to console).
                try {
                    Thread.sleep(1000000);
                } catch (InterruptedException ie) {
                }
            }
        };
        t.start();
        System.out.println("Started");

    }
}
