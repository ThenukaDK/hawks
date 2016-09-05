package gui;

import java.awt.*;     
import java.awt.event.*; 
import javax.swing.*;    


@SuppressWarnings("serial")
public class CCShortestPath extends JFrame implements MouseMotionListener,MouseListener{
  
   // Define constants for the various dimensions
   public JLabel label; 
   public JLabel lblx;
   public JLabel lbly;
   public JLabel ldis;
   public JLabel lindex;
   public static final int CANVAS_WIDTH = 1024;
   public static final int CANVAS_HEIGHT = 780;
   public static final Color LINE_COLOR = Color.RED;
   public static final Color CANVAS_BACKGROUND =Color.lightGray;
   private static Font serifFont = new Font("Serif", Font.BOLD, 14);
   public double x;
   public double y;
 
   private DrawCanvas canvas; // The custom drawing canvas an innder class extends JPanel
 
   // Constructor to set up the GUI components and event handlers
   public CCShortestPath() {
      
      // Set up a custom drawing JPanel
      canvas = new DrawCanvas();
      canvas.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));
      canvas.setCursor(new Cursor(Cursor.CROSSHAIR_CURSOR));
      
      JPanel lPanel = new JPanel(new FlowLayout());
      label = new JLabel("No Mouse Event Captured", JLabel.CENTER);
      label.setFont(new Font("Serif", Font.BOLD, 20));
      lPanel.add(label);
      lblx = new JLabel("");
      lblx.setFont(new Font("Serif", Font.BOLD, 20));
      lPanel.add(lblx);
      lbly = new JLabel("");
      lbly.setFont(new Font("Serif", Font.BOLD, 20));
      lPanel.add(lbly);
      JPanel lPanel1 = new JPanel(new FlowLayout());
      ldis = new JLabel("   ");
      ldis.setFont(new Font("Serif", Font.BOLD, 20));
      lPanel1.add(ldis);
      lindex = new JLabel("   ");
      lindex.setFont(new Font("Serif", Font.BOLD, 20));
      lPanel1.add(lindex);
      addMouseMotionListener(this);
      addMouseListener(this);
       
      // Add panels to this JFrame's content-pane
      Container cp = getContentPane();
      cp.setLayout(new BorderLayout());
      cp.add(canvas, BorderLayout.CENTER);
      cp.add(lPanel, BorderLayout.PAGE_START);
      cp.add(lPanel1, BorderLayout.PAGE_END);
     
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
      setTitle("Shortest Path Calculated Map");
      pack();           // pack all the components in the JFrame
      setVisible(true); 
      requestFocus();   // set the focus to JFrame to receive KeyEvent
      setResizable(false);
   }
   
   public double getCo(double x, double y){
            
            double [][] points = {{250,15},{150,200},{900,230},{480,400},{800,600},{50,700}};
            double[] dis = new double[6];
            System.out.println("x="+x+"y="+y);
            for (int i=0; i<6; i++)
                {
                double dx = points[i][0] - x;
                double dy = points[i][1] - y;
                dis[i] = Math.sqrt(dx*dx + dy*dy);
                System.out.println(dis[i]);
                }   
            double shortestDistance = getMin(dis);
            ldis.setText("Shortest distence is => "+shortestDistance+"      ");
            System.out.println("Shortest distence is = "+shortestDistance);
            return 0;
            }

    
    @Override
    public void mouseMoved(MouseEvent e) {
        label.setText("Quad Copter Coordinates => X:"+e.getX()+" |Y:"+e.getY()+"    "); 
	}

    @Override
    public void mouseDragged(MouseEvent e) {
        }

    @Override
    public void mouseClicked(MouseEvent e) {
	  lblx.setText("X="+e.getX());
	  lbly.setText("Y="+e.getY());
          double x=e.getX();
          double y=e.getY();
          getCo(x,y); 
        }

    @Override
    public void mousePressed(MouseEvent e) {
        }

    @Override
    public void mouseReleased(MouseEvent e) {
        }

    @Override
    public void mouseEntered(MouseEvent e) {
        }

    @Override
    public void mouseExited(MouseEvent e) {
       }
   
    public double getMin(double[] inputArray){
            double minValue = inputArray[0]; 
            int index=1;
            for(int i=0;i<inputArray.length;i++){ 
                if(inputArray[i] < minValue){ 
                    minValue = inputArray[i]; 
                    index = i+1;
                } 
            } 
            
            System.out.println("min index "+index);
            lindex.setText("&       Nearest Chargning Node => "+index);
            return minValue; 
        } 
    
    
    //Define inner class DrawCanvas, which is a JPanel used for custom drawing.
 
   class DrawCanvas extends JPanel {
 
      @Override
      public void paintComponent(Graphics g) {
         super.paintComponent(g);
         setBackground(CANVAS_BACKGROUND);
         g.setColor(LINE_COLOR);
         g.fillOval(250, 15, 30, 30); 
         g.fillOval(150, 200, 30, 30);
         g.fillOval(900, 230, 30, 30);
         g.fillOval(480, 400, 30, 30);
         g.fillOval(800, 600, 30, 30);
         g.fillOval(50, 700, 30, 30);
         g.setColor(Color.BLACK);
         g.setFont(serifFont);
         g.drawString("C.Spot_1", 240,15);
         g.drawString("C.Spot_2", 140,200);
         g.drawString("C.Spot_3", 890,230);
         g.drawString("C.Spot_4", 470,400);
         g.drawString("C.Spot_5", 790,600);
         g.drawString("C.Spot_6", 40,700);    
      }
}
   
 
   public static void main(String[] args) {
      // Run GUI codes on the Event-Dispatcher Thread for thread safety  
        SwingUtilities.invokeLater(new Runnable() {
         @Override
         public void run() {
            new CCShortestPath(); // Let the constructor do the job
         }
      });
   }
}