import edu.wpi.first.wpilibj.RobotDrive;
import edu.wpi.first.wpilibj.SampleRobot;

import org.opencv.core.Rect;
import org.opencv.imgproc.Imgproc;
import org.usfirst.frc.team6162.robot.Grippipeline;

import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import edu.wpi.first.wpilibj.vision.VisionThread;
import edu.wpi.first.wpilibj.vision.VisionRunner;
import edu.wpi.first.wpilibj.vision.VisionPipeline;
import edu.wpi.cscore.UsbCamera;
import edu.wpi.first.wpilibj.CameraServer;


public class FinalRobot extends SampleRobot {
	RobotDrive myRobot = new RobotDrive(0, 1);
	 Joystick stick = new Joystick(0);
	 final String defaultAuto = "Default";
	 final String customAuto = "My Auto";
	 SendableChooser<String> chooser = new SendableChooser<>();
	 private static final int IMG_HEIGHT = 320;
	 private static final int IMG_WIDTH = 240;
	 private VisionThread visionThread;
	 private double centerX = 0.0;
	 private final Object imgLock = new Object();
	 //VisionPipeline Pipeline;
	 UsbCamera Camera;
	 Grippipeline GP = new Grippipeline();
	 

	 public FinalRobot() {
	  myRobot.setExpiration(0.1);
	 }

	 @Override
	 public void robotInit() {
	  chooser.addDefault("Default Auto", defaultAuto);
	  chooser.addObject("My Auto", customAuto);
	  SmartDashboard.putData("Auto modes", chooser);
	  UsbCamera camera = CameraServer.getInstance().startAutomaticCapture();
	  camera.setResolution(IMG_WIDTH, IMG_HEIGHT);
	  
	  visionThread = new VisionThread(Camera, new Grippipeline(), pipeline -> { 
	         if (!pipeline.filterContoursOutput().isEmpty()) {
	             Rect r = Imgproc.boundingRect(pipeline.findContoursOutput().get(0));
	                 centerX = r.x + (r.width / 2);
	         }
	     });
	 }

	 /**
	  * This autonomous (along with the chooser code above) shows how to select
	  * between different autonomous modes using the dashboard. The sendable
	  * chooser code works with the Java SmartDashboard. If you prefer the
	  * LabVIEW Dashboard, remove all of the chooser code and uncomment the
	  * getString line to get the auto name from the text box below the Gyro
	  *
	  * You can add additional auto modes by adding additional comparisons to the
	  * if-else structure below with additional strings. If using the
	  * SendableChooser make sure to add them to the chooser code above as well.
	  */
	 @Override
	 public void autonomous() {
	  
	    
	  String autoSelected = chooser.getSelected();
	  // String autoSelected = SmartDashboard.getString("Auto Selector",
	  // defaultAuto);
	  System.out.println("Auto selected: " + autoSelected);

	  switch (autoSelected) {
	  case customAuto:
	   myRobot.setSafetyEnabled(false);
	   myRobot.drive(-0.5, 1.0); // spin at half speed
	   Timer.delay(2.0); // for 2 seconds
	   myRobot.drive(0.0, 0.0); // stop robot
	   break;
	  case defaultAuto:
	  default:
	   myRobot.setSafetyEnabled(false);
	   myRobot.drive(-0.5, 0.0); // drive forwards half speed
	   Timer.delay(2.0); // for 2 seconds
	   myRobot.drive(0.0, 0.0); // stop robot
	   break;
	  }
	 }

	 /**
	  * Runs the motors with arcade steering.
	  */
	 @Override
	 public void operatorControl() {
	  myRobot.setSafetyEnabled(true);
	  while (isOperatorControl() && isEnabled()) {
	   myRobot.arcadeDrive(stick); // drive with arcade style (use right
	          // stick)
	   Timer.delay(0.005); // wait for a motor update time
	  }
	 }

	 /**
	  * Runs during test mode
	  */
	 @Override
	 public void test() {
	 }
	}
	
