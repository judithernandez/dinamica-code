#Initial Values
CarMass = 5.5 #kg
PilotMass = 2.2 #kg
TotalCarMass = (CarMass+PilotMass) #kg
AxisDistance = 1.6 #m
LongitudeWFtoCM = 3 #m
HeightCenterOfMass = 2 #m
DistanceBetweenAxes = 4 #m
g = 9.81 #m/s^2

RollingRadius = 0.3 #m (radio del centro hasta el suelo)

#"guiacoche" Pg 8 del libro (Pg 19 PDF)
#Static axe load
W = TotalCarMass*9.81 #Weight of car (N)
WR = W*(LongitudeWFtoCM/AxisDistance) #Rear static axe load (N)
WF = W-WR #Front static axe load (N)

#Percentage front/rear distribution (static)
PF = (WF/W)*100 #% to front
PR = 100-PF #% to rear
def GetStaticDistribution():
    print("Static Weight distribution on the front: "+PF)
    print("Static Weight distribution on the Rear: "+PR)
    
#Individual static wheel loads
WRLs = WRRs = WR/2 #Rear static wheel loads (N)
WFLs = WFRs = WF/2 #Front static wheel loads (N)

#"guiacoche" Pg 13 del libro (Pg 24 PDF)
#Individual wheel loads during maximum acceleration
def GetIndividualWheelLoadsma(fricctionCoeficcient,):
    TF = [(WR*fricctionCoeficcient)/(1-((HeightCenterOfMass*fricctionCoeficcient)/DistanceBetweenAxes))] #Traction force (N)
    IWxma = (TF*HeightCenterOfMass)/DistanceBetweenAxes #Longitudinal load transfer with Tractiion Force (N)
    WRLma = WRRma = (WR+IWxma)/2 #Rear wheel loads [maximum acceleration] (N)
    WFLma = WFRma = (WF-IWxma)/2 #Front wheel loads [maximum acceleration] (N)
    print("Front Wheel Loads at Max Acceleration: "+WFRma)
    print("Rear Wheel Loads At Max Acceleration: "+WRLma)

#Peak torque through the transmission when acceleting off-the-line
def TorqueWheels(fricctionCoefccient):
    TorqueWheels = (WRLs + WFRs)*RollingRadius*fricctionCoefccient
    return TorqueWheels

#Maximum acceleration in both m/s^2 and equivalent g forces
ama = GetIndividualWheelLoadsma.TF/TotalCarMass #Acceleration (m/s^2)
amaG = ama/g #Acceleration in g

#"guiacoche" PG 14 del libro (PGP 25 PDF)
def Work(force, distance):
    Work = force*distance
    return Work
    
def Power(force, distance_opcion1, time_opcion1,speed_opcion2): #rellenar opcion 1 o 2; sino 0
    if distance_opcion1 == 0:
        Power = force*speed_opcion2
    else:
        Power = force*(distance_opcion1/time_opcion1)
    return Power

def Force(power, speed):
    Force = power/speed
    return Force

#"guiacoche" PG 16 del libro (PG 27 PDF)
#Individual wheel loads during maximum breaking
def GetIndividualWheelLoadsmb(fricctionCoeficcient,):
    BF = W*fricctionCoeficcient #Breaking force (N)
    IWxmb = (BF*HeightCenterOfMass)/DistanceBetweenAxes  #Longitudinal weight transfer With Braking Force (N)
    WRLmb = WRRmb = (WR-IWxmb)/2 #Rear wheel loads [maximum braking] (N)
    WFLmb = WFRmb = (WR+IWxmb)/2 #Front wheel loads [maximum braking] (N)
    PRmb = ((WRLmb+WRRmb)/IWxmb)*100 #% to front maximum breaking
    PFmb = (100-PRmb)/IWxmb #% to rear maximum breaking

#Maximum deceleration in both m/s^2 and equivalent g forces
amb = GetIndividualWheelLoadsmb.BF/TotalCarMass #Deceleration (m/s^2)
ambG = amb/g #Deceleration in g

#"guiacoche" PG 21 del libro (PG 32 PDF)
#Cornering force
def GetCorneringForce (fricctionCoeficcient):
    CF = W*fricctionCoeficcient #Maximum cornering force (N)

#Maximum total lateral load transfer
LWTy = (GetCorneringForce.CF*HeightCenterOfMass)/AxisDistance #Total lateral weight transfer (N)

#Velocity that the car can travel arround a RadC (m) radius corner
def GetVelocityArroundXRadiusCroner (RadC):
    vRC = (LWTy*RadC)/TotalCarMass #The velocity that the car can travel arround a radius corner (m/s)
    vRC2 = vRC*(3600/1000) #The velocity that the car can travel arround a radius corner (km/h)

#"guiacoche" PG 27 del libro (PG 38 PDF)
#Individual wheel loads during maximum braking with downforce
def GetIndividualWheelLoadsWithDownforce (ADF, fricctionCoeficcient): #ADF in g
    DF = W*ADF #Downfroce (N)
    ETWD = W*DF #Effective total weight of the car (N)
    DWR = WR+DF #Rear axe load with downforce (N)
    DWF = DF-DWR #Front axe load with downforce (N)
    DBF = ETWD*fricctionCoeficcient #Braking force with doenforce (N)
    DWx = (DBF*HeightCenterOfMass)/AxisDistance

#Maximum deceleration in both m/s^2 and equivalent g forces with downforce
DWFL = DWFR = (GetIndividualWheelLoadsWithDownforce.DWF + GetIndividualWheelLoadsWithDownforce.DBF)/2 #Front wheel loads with downforce (N)
DWRL = DWRR = (GetIndividualWheelLoadsWithDownforce.DWR - GetIndividualWheelLoadsWithDownforce.DBF)/2 #Rear wheel loads with downforce (N)
def GetDecelerationWithDownforce(DragBraking): #DragBraking in g
    ABF = W*DragBraking #Air braking force with downforce (N)
    DFT = ABF+GetIndividualWheelLoadsWithDownforce.DBF #Total braking force with downfroce (N)
    da = DFT/TotalCarMass #Deceleation with downforce (m/s^2)
    daG = da/g #Deceleation with downforce in g