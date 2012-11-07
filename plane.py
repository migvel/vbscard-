import bge
import math
from bge import texture
from bge import logic
cont = logic.getCurrentController()
obj = cont.owner


logic.globalDict["planepos"] = [7.97531,0,3.968]

def move():
    if(logic.globalDict["act"] == "2ndperson"):
        if(logic.globalDict["planepos"][0] < 50):
            logic.globalDict["planepos"][0] = logic.globalDict["planepos"][0] + 0.1 +  abs(math.sin(logic.globalDict["planepos"][0])*0.1)
            logic.globalDict["planepos"][2] = logic.globalDict["mechpos"][2] + (3.97-3.34)  + math.sin(logic.globalDict["planepos"][0])*0.01
            obj.position = logic.globalDict["planepos"]

