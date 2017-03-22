package org.usfirst.frc.team6162.robot;
import java.math.*;
import edu.wpi.first.wpilibj.networktables.NetworkTable;
public class RobotFunctions {
	private final double HeightBenchmark = 30;
	private final double WidthBenchmark = 20;
	private final double RangeFactor = 2.65;
	private double TargetRange = 0;
	private double Angle = 0;
	private final double DimensionRatio = HeightBenchmark/WidthBenchmark;
	NetworkTable table;
	
	public RobotFunctions(){
		table = NetworkTable.getTable("datatable");
		}
	
	private void CalculateRange(double Width, double Height){
		TargetRange = RangeFactor*(Height/HeightBenchmark);
		Angle = Math.atan(Height/Width*DimensionRatio);
		
	}
	
	public double[] getRange(double Width, double Height){
		double[] RangeValues = {0,0};
		CalculateRange(Width, Height);
		RangeValues[0]=TargetRange;
		RangeValues[1]=Angle;
		
		return RangeValues;
	}
	
	public void driverStationComm(){
		table.putNumber("TargetRange", TargetRange);
		table.putNumber("Angle", Angle);
		
	}
}
	
	
