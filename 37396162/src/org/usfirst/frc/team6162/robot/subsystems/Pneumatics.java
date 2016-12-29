package org.usfirst.frc.team6162.robot.subsystems;

import edu.wpi.first.wpilibj.DoubleSolenoid;
import edu.wpi.first.wpilibj.command.Subsystem;
import edu.wpi.first.wpilibj.livewindow.LiveWindow;

/**
 *
 */
public class Pneumatics extends Subsystem {
    
    // Put methods for controlling this subsystem
    // here. Call these from Commands.

    public void initDefaultCommand() {
        // Set the default command for a subsystem here.
        //setDefaultCommand(new MySpecialCommand());
    	DoubleSolenoid testDS=new DoubleSolenoid(1,2);
    	testDS.set(DoubleSolenoid.Value.kOff);
    	LiveWindow.addActuator("Pneumatics", "testDS", testDS);
    	
    }
}

