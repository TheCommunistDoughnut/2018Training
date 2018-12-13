


class RobotMap():
    """gathers hardcoded values to interface w/ hardware"""
    def __init__(self):
        """Initialize robotmap"""
        self.motorsMap = ()
        self.pneumaticsMap = PneumaticMap()
        self.controllerMan = ControllerMap()
        
        
        
        
        
        
        
        
class CANMap():
    def __init__(self):
        #self.driveMotors = ()
        self.shooterMotors = ()
        self.intakeMotors = ()
        
        driveMotors['leftMotor'] = 0
        driveMotors['rightMotor'] = 1
        self.driveMotors = driveMotors
        
        
        

class PneumaticsMao():
    def __init__(self):
        self.pnaCan = 1
        self.loaderOpen = 1
        self.loaderClose = 0
        
class ControllerMap():
    def __init__(self):
        driveController = {}
        auxController = {}
        
        driveController['controllerId'] = 0
        driveController['leaftTread'] = 1
        
        if hal.isSimulation():
            driveController['rightTread'] = 3
        else:
            driveController['rightTread'] = 5
            
        driveController['voldRumble'] = 8.0
        
        self.driveController = driveController
        self.auxController = auxController