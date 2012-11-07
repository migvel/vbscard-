
import bge
import math
from bge import texture
from bge import logic
cont = logic.getCurrentController()
obj = cont.owner


logic.globalDict["campos"] = [70,0,3.85]
logic.globalDict["camang"] = 0

logic.globalDict["act"] = "zoomin1"
logic.globalDict["cont"] = 0

obj.position = logic.globalDict["campos"]
obj.visible = False


def viewtravel():
    if(logic.globalDict["act"] == "zoomin1"):
        if logic.globalDict["campos"][0] > 2:
            logic.globalDict["campos"][0] = logic.globalDict["campos"][0] - 0.1
            obj.position = logic.globalDict["campos"]
        else:
            logic.globalDict["act"] = "pause1"
        
    elif(logic.globalDict["act"] == "pause1"):
        if logic.globalDict["cont"] < 100:
            logic.globalDict["cont"] = logic.globalDict["cont"] + 1
        else:
            logic.globalDict["act"] = "rotate1"
            logic.globalDict["camang"] = 0            

    elif(logic.globalDict["act"] == "rotate1"):
        if(logic.globalDict["camang"] < 2*3.1416):
            logic.globalDict["camang"] =  logic.globalDict["camang"] + 0.01
            obj.orientation = [0,0,logic.globalDict["camang"]]
        else:
            logic.globalDict["act"] = "pause2"
            logic.globalDict["cont"] = 0
            #set camera to next view.


    elif(logic.globalDict["act"] == "pause2"):
        if logic.globalDict["cont"] < 100:
            logic.globalDict["cont"] = logic.globalDict["cont"] + 1
        else:
            logic.globalDict["act"] = "firstperson"
            obj.position = [30,0,3.34]
            obj.orientation = [0,0,3.14]
            logic.globalDict["campos"][0] = 30



    elif(logic.globalDict["act"] == "firstperson"):
        if logic.globalDict["campos"][0] < 200:
            logic.globalDict["campos"][2] = logic.globalDict["campos"][2] + math.sin(logic.globalDict["campos"][0])*0.05
            logic.globalDict["campos"][0] = logic.globalDict["campos"][0] + 0.1            
            obj.position = logic.globalDict["campos"]

        else:
            logic.globalDict["act"] = "zoomin1"
            logic.globalDict["campos"] = [70,0,3.85]
            logic.globalDict["act"] = "zoomin1"
            obj.position = logic.globalDict["campos"]
            obj.orientation = [0,0,0]
            
        


