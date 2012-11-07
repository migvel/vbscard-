

import bge
import math
from bge import texture
from bge import logic
cont = logic.getCurrentController()
obj = cont.owner


#inital values
#logic.globalDict["xpos"] = 70
#logic.globalDict["ypos"] = 0
#logic.globalDict["zpos"] = 3.85

#sets the original position angle.
#it's done for the cube camera reference


logic.globalDict["mechpos"] = [6.42,0,3.3]

def move():
    if(logic.globalDict["act"] == "2ndperson"):
        if(logic.globalDict["mechpos"][0] < 50):
            logic.globalDict["mechpos"][0] = logic.globalDict["mechpos"][0] + 0.1  +  abs(math.sin(logic.globalDict["mechpos"][0])*0.1)    
            logic.globalDict["mechpos"][2] = logic.globalDict["mechpos"][2] + math.sin(logic.globalDict["mechpos"][0])*0.01
            obj.position = logic.globalDict["mechpos"]

       
       
