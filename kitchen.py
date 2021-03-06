#kitchen.py

import pymysql
from device import *
import datetime


# class room:
#     def __init__(self, name, dbCursor):
#         self.name = name
#         self.dbCursor = dbCursor
#         self.devices = []

class kitchen:
    def __init__(self, name, dbCursor):
        self.name = name
        self.dbCursor = dbCursor
        self.DELTAT = 100 #100 degrees per second

        #-------------------------------------------------------------
        #   DEFINITION AND DATA MEMBERS
        #-------------------------------------------------------------
        #   OVEN
        #-------------------------------------------------------------

        self.oven = device("Oven",dbCursor)
        self.oven.sensors.append(tempSensor("OTS1","Oven",dbCursor))
        self.oven.actuators.append(actuator("Oven Actuator", "Oven",dbCursor))

        #-------------------------------------------------------------
        #   FRIDGE
        #-------------------------------------------------------------
        self.fridge = device("Fridge",dbCursor)
        self.fridge.sensors.append(tempSensor("FTS1","Fridge",dbCursor))
        self.fridge.sensors.append(openCloseSensors("Fridge Door OCS","Fridge",dbCursor))

        #-------------------------------------------------------------
        #   STOVE
        #-------------------------------------------------------------

        self.stove = device("Stove",dbCursor)
        for i in range(4):
            self.stove.sensors.append(tempSensor("STS"+str(i+1),"Stove",dbCursor))
            self.stove.actuators.append(actuator("Burner"+str(i+1)+" Actuator","Stove",dbCursor))

        #-------------------------------------------------------------
        #   SINK
        #-------------------------------------------------------------

        self.sink = device("Sink", dbCursor)
        self.sink.actuators.append(actuator("Sink Actuator","Sink",dbCursor))
        self.sink.sensors.append(liquidFlowSensor("SLFS","Sink",dbCursor))

        #-------------------------------------------------------------
        #   MICROWAVE
        #-------------------------------------------------------------

        self.microwave = device("Microwave",dbCursor)
        self.microwave.actuators.append(actuator("Microwave Actuator", "Microwave", dbCursor))
        self.microwave.sensors.append(tempSensor("MTS", "Microwave",dbCursor))

        #-------------------------------------------------------------
        #   DISH WASHER
        #-------------------------------------------------------------

        self.dishwasher = device("Dishwasher",dbCursor)
        self.dishwasher.actuators.append(actuator("Dishwasher Actuator", "Dishwasher", dbCursor))
        self.dishwasher.sensors.append(liquidFlowSensor("DWLFS","Dishwasher", dbCursor))

        #-------------------------------------------------------------
        #   COFFEE MAKER
        #-------------------------------------------------------------

        self.coffeemaker = device("Coffee Maker",dbCursor)
        self.coffeemaker.actuators.append(actuator("Coffee Maker Actuator", "Coffee Maker",dbCursor))
        self.coffeemaker.sensors.append(tempSensor("CMTS","Coffee Maker",dbCursor))
        self.coffeemaker.sensors.append(liquidFlowSensor("CMLFS","Coffee Maker",dbCursor))

        #-------------------------------------------------------------
        #   TOASTER
        #-------------------------------------------------------------

        self.toaster = device("Toaster", dbCursor)
        self.toaster.actuators.append(actuator("Toaster Actuator", "Toaster", dbCursor))
        self.toaster.sensors.append(tempSensor("TTS","Toaster",dbCursor))

        #-------------------------------------------------------------
        #   GARBAGE DISPOSAL
        #-------------------------------------------------------------

        self.garbagedisposal = device("Garbage Disposal",dbCursor)
        self.garbagedisposal.actuators.append(actuator("Garbage Disposal Actuator", "Garbage Disposal",dbCursor))

        #-------------------------------------------------------------
        #   LIGHTS
        #-------------------------------------------------------------

        self.lights = device("Kitchen Lights",dbCursor)
        self.lights.actuators.append(actuator("Kitchen Light Actuator","Kitchen Lights",dbCursor))
        self.lights.sensors.append(brightSensor("KLBS","Kitchen Lights", dbCursor))
        self.lights.sensors.append(motionSensor("KLMS","Kitchen Lights", dbCursor))

        #-------------------------------------------------------------
        #   DOORS
        #-------------------------------------------------------------

        #   NO DOORS
        
        #-------------------------------------------------------------
        #   WINDOWS
        #-------------------------------------------------------------

        self.windows = []
        self.windows.append(device("KWindow1",dbCursor))
        self.windows[0].actuators.append(actuator("Kitchen Window 1 Actuator", "Kwindow1",dbCursor))
        self.windows[0].sensors.append(openCloseSensors("KW1OCS","KWindow1",dbCursor))
        self.windows.append(device("KWindow2",dbCursor))
        self.windows[1].actuators.append(actuator("Kitchen Window 2 Actuator", "Kwindow2",dbCursor))
        self.windows[1].sensors.append(openCloseSensors("KW2OCS","KWindow2",dbCursor))
        
        #-------------------------------------------------------------
        #   AC/HEAT
        #-------------------------------------------------------------

        self.air = device("Air",dbCursor)
        self.air.sensors.append(tempSensor("KATS","Air",dbCursor))
        self.air.actuators.append(actuator("Kitchen Air Actuator","Air",dbCursor))
        #-------------------------------------------------------------
        #   CAMERAS
        #-------------------------------------------------------------
        
        self.cameras = []
        self.cameras.append(device("Kitchen Camera 1",dbCursor))
        self.cameras[0].actuators.append(actuator("Kitchen Camera 1 Actuator","Kitchen Camera 1",dbCursor))
        self.cameras[0].sensors.append(motionSensor("KC1MS","Kitchen Camera 1",dbCursor))



    
    #-------------------------------------------------------------
    #   METHODS
    #-------------------------------------------------------------
    #   OVEN
    #-------------------------------------------------------------

    def turnOnOven(self):
        self.oven.actuators[0].turnOn()

    def turnOffOven(self):
        self.oven.actuators[0].turnOff()

    def getOvenTemp(self):
        return self.oven.sensors[0].getTemp()

    def setOvenTemp(self,temp):
        self.oven.sensors[0].setTemp(temp)

    def updateOvenTemp(self):
        lut = self.oven.actuators[0].getLUT()
        now = datetime.datetime.now()
        timeDiff = now - lut
        secondsElapsed = round(timeDiff.total_seconds())
        oldTemp=self.getOvenTemp()
        self.setOvenTemp((secondsElapsed*self.DELTAT))

    def getOvenState(self):
        return self.oven.actuators[0].getState()

    #-------------------------------------------------------------
    #   FRIDGE
    #-------------------------------------------------------------

    def openFridgeDoor(self):
        self.fridge.sensors[1].updateOpen()

    def closeFridgeDoor(self):
        self.fridge.sensors[1].updateClosed()

    def getFridgeDoorState(self):
        return self.fridge.sensors[1].getState()
    
    #-------------------------------------------------------------
    #   STOVE
    #-------------------------------------------------------------

    def turnOnStoveBurner(self, burnerNum):
        self.stove.actuators[burnerNum].turnOn()

    def turnOffStoveBurner(self, burnerNum):
        self.stove.actuators[burnerNum].turnOff()

    

    #-------------------------------------------------------------
    #   SINK
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   MICROWAVE
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DISH WASHER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   COFFEE MAKER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   TOASTER
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   GARBAGE DISPOSAL
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   LIGHTS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   DOORS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   WINDOWS
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   AC/HEAT
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    #   CAMERAS
    #-------------------------------------------------------------

        

# def main():
#     # Open database connection
#     db = pymysql.connect("localhost","jp","Database","digital_home_database" )

#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
    
#     cursor.execute("DELETE FROM TempSensors")
#     cursor.execute("DELETE FROM OpenCloseSensors")
#     cursor.execute("DELETE FROM MotionSensors")
#     cursor.execute("DELETE FROM LiquidFlowSensors")
#     cursor.execute("DELETE FROM BrightnessSensor")
#     cursor.execute("DELETE FROM Actuators")
#     cursor.execute("DELETE FROM Devices")

#     # oven = device("Oven",cursor)

#     # tempS = tempSensor("TS1","Oven",cursor)

#     # oven.sensors.append(tempS)

#     # kitchen = room("kitchen",cursor)

#     # kitchen.devices.append(oven)
#     # print(kitchen.devices[0].getName())
#     kitchen1 = kitchen("Kitchen", cursor)
#     print(kitchen1.oven.actuators[0].getState())
#     kitchen1.turnOnOven()
#     print(kitchen1.oven.actuators[0].getState())
#     kitchen1.turnOffOven()
#     print(kitchen1.oven.actuators[0].getState())
#     print("FRIDGE")
#     print(kitchen1.getFridgeDoorState())
#     kitchen1.openFridgeDoor()
#     print(kitchen1.getFridgeDoorState())
#     kitchen1.closeFridgeDoor()
#     print(kitchen1.getFridgeDoorState())



#     db.commit()
#     db.close()
# main()