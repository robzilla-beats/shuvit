#scale = .3
#action layers
#0-14 rolling
#grablay = 400
#fliplay = 500
#grindlay = 700
os = 'Windows'
from sys import platform
if platform != "win32":
 os = 'Linux'
def onWindows():
 return os == 'Windows'
from mathutils import Vector

import bge
import GameLogic
import ctypes
import math
#import bpy

#build global dict (move this to separate script that runs once)
scene = bge.logic.getCurrentScene()
objList = scene.objects
try:
    GameLogic.DictObjects
    init=1
except:
    init=0
if init:
    cont.GameLogic.getCurrentController()
    own = cont.getOwner()
    name = own.getName()
    if not GameLogic.DictObjects.has_key(name):
        GameLogic.DictObjects[name]=cont
    own.init=0
reduction = 400000
axisTh = 0.03 




############
##vibration#
############
## Define necessary structures
#class XINPUT_VIBRATION(ctypes.Structure):
#    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort), ("wRightMotorSpeed", ctypes.c_ushort)]
#xinput = ctypes.windll.xinput1_3 # Load Xinput.dll
## Set up function argument types and return type
#XInputSetState = xinput.XInputSetState
#XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
#XInputSetState.restype = ctypes.c_uint
## Now we're ready to call it. Set left motor to 100%, right motor to 50%
## for controller 0
##vibration = XINPUT_VIBRATION(65535, 32768)
##XInputSetState(0, ctypes.byref(vibration))
## You can also create a helper function like this:
#def set_vibration(controller, left_motor, right_motor):
#    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535))
#    XInputSetState(controller, ctypes.byref(vibration))  
## ... and use it like so
##set_vibration(0, 0.2, 0.2)
################
##end vibration#
################

#initialize quadrant variables
q1on = 0
q2on = 0
q3on = 0
q4on = 0
q5on = 0
q6on = 0
q7on = 0
q8on = 0
lq1on = 0
lq2on = 0
lq3on = 0
lq4on = 0
lq5on = 0
lq6on = 0
lq7on = 0
lq8on = 0

#number of frames / length of the location timers
countdown = 20


cont = GameLogic.getCurrentController() 
obj = bge.logic.getCurrentScene().objects
char = bge.constraints.getCharacter
own = cont.owner
dict = bge.logic.globalDict #Get the global dictionary
#dict['trick_string'] = ''

#last frame stuff
lGRAB_ON = own["lGRAB_ON"]
lastgrab = own["lastGrab"]
lastpump = own["lastPump"]
lf_ground = own["lF_ground"]
lastopos = own["last_Opos"]
lastnopos = own["last_nOpos"]
LAST_STANCE = own["last_stance"]
LAST_GROUND = own["last_ground"]
lastStop = own["lastStop"]
LAST_LEFT = own["LAST_LEFT"]
last_trick_string = dict.get('last_trick_sting')
lasta = own["lasta"]
lastx = own["lastx"]
lastaf = own["lastaf"]
lastxf = own["lastxf"]
lgf = own['last_grind_frame']
frame = own['framenum']
frames_since_grinding = frame - lgf
own['last_footplant'] = own['footplant_on']
lastaBut_ground = own['lastaBut_ground'] 
lastxBut_ground = own['lastxBut_ground'] 
aBut_ground = own['aBut_ground']
xBut_ground = own['xBut_ground']
own['last_manual_v2'] = own['manual_v2']


#current frame stuff
GRAB_ON = own["GRAB_ON"]
pumpon = own["Pump"]
vib_countdown = own["vib_Countdown"]
grindold = own['grindOld']
#grindHit = own["LAST_GRIND"]
LAST_GRIND = own["LAST_GRIND"]
#grindTouch = cont.sensors['grindCol']
grindTouch = cont.sensors['grindCol_bottom']
touched = grindTouch.triggered
leftgrabon = own["Leftgrabon"]
rightgrabon = own["Rightgrabon"]
linvel = own.getLinearVelocity
zvel = own.worldLinearVelocity.z
own["Zvel"] = zvel
r_ground = cont.sensors["r_Ground"]
trigger = r_ground.triggered
STANCE = own["stance"]
motion = cont.actuators['MotionPump']
linVelocity = own.getLinearVelocity(True)
countdown = own['countdown']
jump_timer = own['jump_timer']
pos = own.localPosition
rot = own.getAxisVect( [0.0, 0.0, 1.0])
gray = cont.sensors["gRay"]
#airconst = cont.actuators["airConst"]
pop = cont.actuators["pop"]
grindHit = own["grindHit"]
grindCement = cont.actuators["grind_cement"]
grindRail = cont.actuators["grind_rail"]
grindSound = own["grindSound"]
skater = scene.objects["Char4"]
deck = scene.objects["deck"]
trucks = scene.objects["trucks"]
wheel1 = scene.objects["rollen.000"]
wheel2 = scene.objects["rollen.001"]
wheel3 = scene.objects["rollen.002"]
wheel4 = scene.objects["rollen.003"]
turnsens = .04
turnsens2 = .06 #air_turn_boost
grindDar = own["grindDar_hit"]
grindEmpty = scene.objects["grindEmpty"]
grindDar2 = grindEmpty.sensors["grindDar2"]
#invertCol = cont.sensors["invertCol"]
cam = scene.objects["Camera.003"]
freecam = scene.objects["freecam"]
followcam = scene.objects["followcam"]
coping_on = own["coping"]
invert_on = own['invert_on']
grab_type = own['grab_type']
c_ground = cont.sensors['c_ground']
#
control_bottom = scene.objects['control_bottom']
invertTouch = control_bottom.sensors['grindCol_bottom']
wallride = own["wallride"]
wallride_col = cont.sensors['wallride']
wallrideL = cont.sensors['wallrideL']
wallrideR = cont.sensors['wallrideR']
wallrideconstL = cont.actuators['wallrideconstL']
wallrideconstR = cont.actuators['wallrideconstR']
if r_ground.triggered: own['wallride_off'] = 0
own['pop_sound'] = 0
own['land_sound'] = 0
#own['fall'] = 0 

#joystick location timers
q1oncd = own["Q1oncd"]
q2oncd = own["Q2oncd"]
q3oncd = own["Q3oncd"]
q4oncd = own["Q4oncd"]
q5oncd = own["Q5oncd"]
q6oncd = own["Q6oncd"]
q7oncd = own["Q7oncd"]
q8oncd = own["Q8oncd"]
q1oncdl = own["Q1oncdl"]
q2oncdl = own["Q2oncdl"]
q3oncdl = own["Q3oncdl"]
q4oncdl = own["Q4oncdl"]
q5oncdl = own["Q5oncdl"]
q6oncdl = own["Q6oncdl"]
q7oncdl = own["Q7oncdl"]
q8oncdl = own["Q8oncdl"]


#setable
grablay = 600 #this plus 1
fliplay = 470
MAX_VEL = 6.7
SPEEDUP = .055
SPEEDPUMP = .09 #.075
SPEEDPUMPFAST = .13 #.09
PUMP_SPEED_SENS = .4
PUMP_SENS = .98
ACCEL = 10
CRUISE = 9
COUNTDOWN = 20 #pump and speed stuff
JUMPHEIGHT = 800 #775#750
JUMPSTRENGTH = 0
own['flip_manual_stance'] = 0
CAVEMAN_SPEED = .75
LAND_LAYER = 100
LAND_END = 20

#Sensor logic bricks connected to the python Controller  
aXis = cont.sensors["sControla"]
bUtt = cont.sensors["sControlb"]

onW = onWindows()

# windows stuff
lar_lts = 0
uad_lts = 1
lar_rts = 2 if onW else 2
uad_rts = 3 if onW else 3
lt = 4 if onW else 4
rt = 5 if onW else 5

# These are the numerical values associated with the buttons on the Xbox Controller 
# Called with - SensorName.getButtonStatus(buttonnumber) - 
# A joystick sensor logic brick (with the 'Button' Event Type; 'All Events' selected; and 'Tap' enabled) must be connected to the Python Controller logic brick to call these buttons 

a_but = 0 if onW else 0
b_but = 1 if onW else 1
x_but = 2 if onW else 2
y_but = 3 if onW else 3
l_bump = 9 if onW else 9
r_bump = 10 if onW else 10
bk_but = 4 if onW else 4
st_but = 6 if onW else 6
xb_but = 5 if onW else 5
lts_pr = 7 if onW else 7
rts_pr = 8 if onW else 8
l_dp = 13 if onW else 13
r_dp = 14 if onW else 14
u_dp = 11 if onW else 11
d_dp = 12 if onW else 12

lLR = aXis.axisValues[lar_lts] / reduction
lUD = aXis.axisValues[uad_lts] / reduction
rLR = aXis.axisValues[lar_rts] / reduction
rUD = aXis.axisValues[uad_rts] / reduction
lTrig = aXis.axisValues[lt] / reduction
rTrig = aXis.axisValues[rt] / reduction
aBut = bUtt.getButtonStatus(a_but)
bBut = bUtt.getButtonStatus(b_but)
xBut = bUtt.getButtonStatus(x_but)
yBut = bUtt.getButtonStatus(y_but)
lBump = bUtt.getButtonStatus(l_bump)
rBump = bUtt.getButtonStatus(r_bump)
bkBut = bUtt.getButtonStatus(bk_but)
stBut = bUtt.getButtonStatus(st_but)
xbBut = bUtt.getButtonStatus(xb_but)
ltsBut = bUtt.getButtonStatus(lts_pr)
rtsBut = bUtt.getButtonStatus(rts_pr)
ldPad = bUtt.getButtonStatus(l_dp)
rdPad = bUtt.getButtonStatus(r_dp)
udPad = bUtt.getButtonStatus(u_dp)
ddPad = bUtt.getButtonStatus(d_dp)

## -End- ##
list = bUtt.getButtonActiveList()
#print(list)

#no input
def cutOff():
    
 if (abs(lLR) < axisTh 
     and abs(lUD) < axisTh 
     and abs(rLR) < axisTh 
     and abs(rUD) < axisTh
     and aBut == False):
         
  return True

#fliptricks after manuals
if (frame - own['last_manual_frame']) < 25:
    flip_start_lay = 8
    flipspeed = .4
    own['flipspeed'] = .4
    own['flip_start_lay'] = 8
    #print("chopping flip start")
else:
    flip_start_lay = 1 
    own['flip_start_lay'] = 1
    flipspeed = .6   
    own['flipspeed'] = .6
def printplaying():
    splaying_layers = "S: "
    playing_layers = "D: "
    tplaying_layers = "T: "
    for x in range(9900):
        if skater.isPlayingAction(x):
        #if trucks.isPlayingAction(x):
        #if skater.isPlayingAction(x):                        
            splaying_layers += str(x)
            splaying_layers += " "        
        if deck.isPlayingAction(x):
        #if trucks.isPlayingAction(x):
        #if skater.isPlayingAction(x):                        
            playing_layers += str(x)
            playing_layers += " "
        if trucks.isPlayingAction(x):
        #if trucks.isPlayingAction(x):
        #if skater.isPlayingAction(x):                        
            tplaying_layers += str(x)
            tplaying_layers += " "            
    print(splaying_layers, playing_layers, tplaying_layers)   

if aBut == True and lasta == False and r_ground.triggered:
    aBut_ground = True
    own['aBut_ground'] = True
#else:
if aBut == False:
    aBut_ground = False    
    own['aBut_ground'] = False
if xBut == True and lastx == False and r_ground.triggered:
    xBut_ground = True
    own['xBut_ground'] = True
#else:
if xBut == False:
    xBut_ground = False    
    own['xBut_ground'] = False    
    
def killact(layer):
    if skater.isPlayingAction(layer):
        skater.stopAction(layer)
    if deck.isPlayingAction(layer):    
        deck.stopAction(layer)
    if trucks.isPlayingAction(layer):    
        trucks.stopAction(layer)

def killall():
    for x in range(9000):
        skater.stopAction(x)
        deck.stopAction(x)
        trucks.stopAction(x)
               
def grind_stance():
    #own["last_grind_stance"] = own["grind_stance"]
#    if grindHit == 1 and LAST_GRIND == 1 and (own['grindCountdown'] < 15 or own['grindCountdown'] >19):
#        own["last_grind_stance"] = own["grind_stance"]        
        #own["grind_stance"] = STANCE 
    pass    
grind_stance()  

def reset_rtimers():
    own["Q1oncd"] = 0
    own["Q2oncd"] = 0
    own["Q3oncd"] = 0
    own["Q4oncd"] = 0
    own["Q5oncd"] = 0
    own["Q6oncd"] = 0
    own["Q7oncd"] = 0
    own["Q8oncd"] = 0
    q1oncd = 0
    q2oncd = 0
    q3oncd = 0
    q4oncd = 0
    q5oncd = 0
    q6oncd = 0
    q7oncd = 0
    q8oncd = 0    

def check_fall():
    playing_frame = 20
    if skater.isPlayingAction(fliplay):
        playing_frame = skater.getActionFrame(fliplay)
    if r_ground.triggered == True and skater.isPlayingAction(fliplay) and own['jump_timer'] < 40 and playing_frame < 14 and playing_frame > 3:
        own['fall'] = 1
        print("fall: ", playing_frame, own['jump_timer'])
check_fall()
def check_landing():
    lf_ground = own["lF_ground"]
    #zvel = own.getLinearVelocity
    #print(zvel)
    STANCE = own["stance"]
    #if lf_ground == False and r_ground.triggered == True and grindDar == 0:
    playing_action_frame = skater.getActionFrame(LAND_LAYER)
    #if playing_action_frame < (LAND_END):    
        #own["lastPump"] = False
        #own["Pump"] = False
    if lf_ground == False and r_ground.triggered == True:
        #resetjumpstance()
        #print(r_ground.hitObject)
        own['jump_from_trans'] = 0
        nearestObject = None
        minDist = None
        detectedObjects = grindDar2.hitObjectList
        #if grindHit == False and gray.triggered == False and touched == False:

#        if grindDar2.positive:
#            for obj in detectedObjects:
#                dist = own.getDistanceTo(obj)
#                if (minDist is None or dist < minDist):
#                    nearestObject = obj
#                    minDist = dist                    
#        if nearestObject != None and 'rail' in scene.objects[nearestObject]:
#            cont.activate(own.actuators["landonrail"])
#            print("landonrail***************")
        #play landing sound
        if grindDar == 0:
            #print("you are not grinding", grindHit)
            lastheight = own["air_height"]
            pos = own.worldPosition.z
            dist = lastheight - pos
            dist = dist * 2
            #print(dist, "-------------dist")
            
            if dist > 1:
                dist = 1
            own.actuators["land"].volume = dist 
            #cont.deactivate(own.actuators["land"])
            sact = own.actuators["land"]
            sact.stopSound()   
            cont.activate(own.actuators["land"])
            own['land_sound'] = 1
        if grindDar == 1:
            pass
            #cont.activate(own.actuators["landonrail"])    
        #vibrate
        #set_vibration(0, 0.3, 0.3)
        own["vib_Countdown"] = 14
        cont.activate(own.actuators["Vibration"])
        #print("vibrate")
        #killall() 
        #if own["reg_nmanual"] == 0 and own["fak_nmanual"] == 0 and own["reg_manual"] == 0 and own["fak_manual"] == 0:
        if own['manual_v2'] == 0 and grindDar == 0:           
            if STANCE == 0:
                own['requestAction'] = 'reg_land'
                #skater.playAction("reg_land", 1,20, layer=LAND_LAYER, blendin=5, priority=7, layer_weight=0, play_mode=0, speed=.5)
            elif STANCE == 1:
                own['requestAction'] = 'fak_land'                
                #skater.playAction("fak_land", 1,20, layer=LAND_LAYER, blendin=5, priority=7, layer_weight=0, play_mode=0, speed=.5)
        killact(2)
        killact(3)
        killact(4)
        killact(5)    
    lf_ground = r_ground.triggered
    own["lF_ground"] = lf_ground
    vib_countdown = own["vib_Countdown"]
    if vib_countdown == 0:
        pass
        #set_vibration(0, 0, 0)
    elif vib_countdown > 0:
        vib_countdown = vib_countdown - 1
        own["vib_Countdown"] = vib_countdown
    if vib_countdown == 1:
        stopAnims()
        stance()
    # if touched == False and lf_ground == True:    
    #     if own['jump_stance'] != 3:
    #         own['jump_stance'] = 3    
        

#air anim
if r_ground.triggered == False:
    if STANCE == 0:
        own['requestAction'] = 'reg_air'
    if STANCE == 1:
        own['requestAction'] = 'fak_air'
else:
    if STANCE == 0:
        own['requestAction'] = 'reg_roll'
    if STANCE == 1:
        own['requestAction'] = 'fak_roll'

#check manual_v2
if (rUD > .04 and rUD < .07) or (rUD < -.04 and rUD > -.07):
#if (rUD > .04 and rUD < .07):
    #print("zoned")    
    timer = own['manual_v2_timer']
    timer = timer + 1
    if timer > 20:
        own['manual_v2'] = 1
    own['manual_v2_timer'] = timer    
if rUD < .04 and rUD > -.04:
    own['manual_v2_timer'] = 0
    own['manual_v2'] = 0 
    own['manual_v2_type'] = None
if own['manual_v2'] == 1:    
    if own['last_manual_v2'] == 0:
        #print("don't flip")
        if STANCE == 0:
            if rUD > .04 and rUD < .07:
                #print("reg manual")
                own['manual_v2_type'] = 'reg manual'
                own['requestAction'] = 'reg_manual'    
                
            if rUD < -.04 and rUD > -.07:
                #print("reg nose manual")
                own['manual_v2_type'] = 'reg nose manual'
                own['requestAction'] = 'reg_nose_manual' 
                
        if STANCE == 1:
            if rUD > .04 and rUD < .07:
                #print("fak manual")
                own['manual_v2_type'] = 'fak manual'
                own['requestAction'] = 'fak_manual'     
                
            if rUD < -.04 and rUD > -.07:
                #print("fak nose manual")
                own['manual_v2_type'] = 'fak nose manual'
                own['requestAction'] = 'fak_nose_manual' 
                            
    else:
        #print("flip stance")
        if STANCE == 0:
            if own['manual_v2_type'] == 'fak manual':
                own['manual_v2_type'] = 'reg nose manual'
            if own['manual_v2_type'] == 'fak nose manual':
                own['manual_v2_type'] = 'reg manual'
        if STANCE == 1:
            if own['manual_v2_type'] == 'reg manual':
                own['manual_v2_type'] = 'fak nose manual'
            if own['manual_v2_type'] == 'reg nose manual':
                own['manual_v2_type'] = 'fak manual'                                
#print(own['manual_v2'], own['manual_v2_type'])    
#check manual
####
#reg
if rUD > .04 and rUD < .07 and STANCE == 0 and rLR < .035 and rLR > -.035:
    timer = own["reg_manual_timer"]
    timer = timer + 1
    own["reg_manual_timer"] = timer
    if timer > 20 and rUD < .04:
        own["reg_manual"] = 0
        #print("reg_man off")
if rUD <= .04 and (STANCE == 1 or STANCE == 0) and rUD >= -.04:
    own["reg_manual_timer"] = 0
    own["reg_manual"] = 0 
    #print("reg_man off2")   
#####
if own["reg_manual_timer"] > 10 and own["fak_manual"] == 0 and own['reg_nmanual'] == 0:
#if own["reg_manual_timer"] > 10 and own["fak_manual"] == 0:
    #if own['fak_nmanual'] == 0:
    own["reg_manual"] = 1
######
if own["reg_manual_timer"] == 0:
    own["reg_manual"] = 0 
if own['last_reg_manual'] == 1 and own['reg_manual'] == 0:
    killall()   
#print(own["reg_manual"])    
      
####   
#fak
if rUD > .04 and rUD < .07 and STANCE == 1 and rLR < .035 and rLR > -.035:
    timer = own["fak_manual_timer"]
    timer = timer + 1
    own["fak_manual_timer"] = timer
    if timer > 20:
        own["fak_manual"] = 0
if rUD <= .04 and (STANCE == 1 or STANCE == 0) and rUD >= -.04:
    own["fak_manual_timer"] = 0
    own["fak_manual"] = 0
if own["fak_manual_timer"] > 10 and own["reg_manual"] == 0:
    own["fak_manual"] = 1
if own["fak_manual_timer"] == 0:
    own["fak_manual"] = 0 
if own['last_fak_manual'] == 1 and own['fak_manual'] == 0:
    killall()   
#print(own["reg_manual"], own["fak_manual"])    
 
#####
#reg nmanual
if rUD < -.04 and rUD > -.07 and STANCE == 0 and rLR < .035 and rLR > -.035:
    timer = own["reg_nmanual_timer"]
    timer = timer + 1
    own["reg_nmanual_timer"] = timer
    if timer > 20:
        own["reg_nmanual"] = 0
if rUD >= -.04 and (STANCE == 1 or STANCE == 0) and rUD <= .04:
    own["reg_nmanual_timer"] = 0
    own["reg_nmanual"] = 0

if own["reg_nmanual_timer"] > 10 and own["fak_nmanual"] == 0 and own['reg_manual'] == 0 and own['fak_manual'] == 0:  
    if own['last_fak_manual'] == False and own['last_reg_manual'] == False and own['last_fak_manual'] == False:
        own["reg_nmanual"] = 1
        #print("baaad", own['reg_manual'], own['last_reg_manual'])

if own["reg_nmanual_timer"] == 0:
    own["reg_nmanual"] = 0 
if own['last_reg_nmanual'] == 1 and own['reg_nmanual'] == 0:
    killall()   
 
#####
#fak nmanual
#print (rUD)
if rUD < -.04 and rUD > -.07 and STANCE == 1 and rLR < .035 and rLR > -.035:
    timer = own["fak_nmanual_timer"]
    timer = timer + 1
    own["fak_nmanual_timer"] = timer
    if timer > 20:
        own["fak_nmanual"] = 0
if rUD >= -.04 and (STANCE == 1 or STANCE == 0) and rUD <= .04:
    own["fak_nmanual_timer"] = 0
    own["fak_nmanual"] = 0
    #print('@@@@@@@@@fak_man_off_1')
if own["fak_nmanual_timer"] > 10 and own["reg_nmanual"] == 0 and own['fak_manual'] == 0 and own ['reg_manual'] == 0:
    own["fak_nmanual"] = 1
if own["fak_nmanual_timer"] == 0 and own['reg_manual'] == 0:
    #if own['flip_manual_stance'] == 0:
    own["fak_nmanual"] = 0 
if own['last_fak_nmanual'] == 1 and own['fak_nmanual'] == 0:
    killall()   


#print("rm ", own["reg_manual"], "rnm ", own["reg_nmanual"], "fm ", own["fak_manual"], "fnm ", own["fak_nmanual"])


def reg_stance_left_off():
    killact(10)  
    killact(32)
    LAST_LEFT = own["LAST_LEFT"]
    if LAST_LEFT == 1 and rUD < .06:
        skater.playAction("nreg_left", 30,40, layer=33, blendin=10, layer_weight=0, play_mode=0, speed=2)
        #deck.playAction("a_reg_left", 30,40, layer=33, play_mode=0, speed=2)
        #deck.playAction("a_reg_right", 30,40, layer=501, play_mode=0, speed=.5)
    own["LAST_LEFT"] = 0   

def reg_stance_right_off():
    killact(11) 
    killact(34)
    LAST_RIGHT = own["LAST_RIGHT"]
    #if LAST_RIGHT == 1 and rUD < .06:
        #skater.playAction("nreg_right", 30,40, layer=35, blendin=10, layer_weight=0, play_mode=0, speed=2)
        #deck.playAction("a_reg_left", 30,40, layer=33, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        #deck.playAction("a_reg_right", 30,40, layer=501, play_mode=0, speed=.5)
    own["LAST_RIGHT"] = 0  
    
def reg_stance_on():
    #revert_timer
    playing = deck.isPlayingAction(40)
    if own["revert_timer"] < 1 and own['manual_v2'] == 0 and playing == 0:
        own['requestAction'] = 'reg_roll'
#        skater.playAction("nreg", 1,60, layer=2, blendin=4, layer_weight=0, play_mode=1, speed=.5)
#        deck.playAction("a_reg", 1,40, layer=2, blendin=0, blend_mode=0, play_mode=1, speed=.5)
#        trucks.playAction("a_reg", 1,40, layer=2, blendin=2, layer_weight=0, play_mode=1, speed=.5)
def reg_stance_off():
    killact(2)   
    
def reg_manual_on():
    own['requestAction'] = 'reg_manual'
#    skater.playAction("reg_manual", 10,70, layer=222, blendin=0, layer_weight=.1, play_mode=1, speed=.5)                
#    deck.playAction("a_reg_manual", 10,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    trucks.playAction("a_reg_manual", 10,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    if own["last_reg_manual"] == 0:
#        reg_stance_left_off()
#        reg_stance_right_off()
#        skater.playAction("reg_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)                
#        deck.playAction("a_reg_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)
#        trucks.playAction("a_reg_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)        
    if own["reg_manual_timer"] == 41:
        killact(3000)
        killact(3001)
        killact(3002)    
def reg_manual_off():
    killact(222)
    killact(223)
    killact(224)  
    killact(3000)
    killact(3001)
    killact(3002)
    killact(10)  
    killact(32)
    killact(11)  
    killact(34) 
    
def fak_manual_on():
    #killall()
    own['requestAction'] = 'fak_manual'
#    skater.playAction("fak_manual", 10,70, layer=222, blendin=0, layer_weight=.1, play_mode=1, speed=.5)                
#    deck.playAction("a_fak_manual", 10,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    trucks.playAction("a_fak_manual", 10,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    if own["last_fak_manual"] == 0:
#        fak_stance_left_off()
#        fak_stance_right_off()
#        skater.playAction("fak_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)                
#        deck.playAction("a_fak_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)
#        trucks.playAction("a_fak_manual", 1,10, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)        
    if own["fak_manual_timer"] == 41:
        killact(3000)
        killact(3001)
        killact(3002)    
def fak_manual_off():
    killact(222)
    killact(223)
    killact(224)  
    killact(3000)
    killact(3001)
    killact(3002)
    killact(10)  
    killact(32)
    killact(11)  
    killact(34)  
#######                     
#######
#######
#######
def reg_nmanual_on():
    own['requestAction'] = 'reg_nmanual'
#    skater.playAction("reg_nmanual", 12,70, layer=222, blendin=0, layer_weight=.1, play_mode=1, speed=.5)                
#    deck.playAction("a_fak_manual", 12,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    trucks.playAction("a_fak_manual", 12,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    if own["last_reg_nmanual"] == 0:
#        reg_stance_left_off()
#        reg_stance_right_off()
#        skater.playAction("reg_nmanual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)                
#        deck.playAction("a_fak_manual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)
#        trucks.playAction("a_fak_manual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)        
    if own["reg_nmanual_timer"] == 41:
        killact(3000)
        killact(3001)
        killact(3002)    
def reg_nmanual_off():
    killact(222)
    killact(223)
    killact(224)  
    killact(3000)
    killact(3001)
    killact(3002)
    killact(10)  
    killact(32)
    killact(11)  
    killact(34) 
    
def fak_nmanual_on():
    #killall()
    own['requestAction'] = 'fak_nmanual'
#    skater.playAction("fak_nmanual", 12,70, layer=222, blendin=0, layer_weight=.1, play_mode=1, speed=.5)                
#    deck.playAction("a_reg_manual", 12,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    trucks.playAction("a_reg_manual", 12,70, layer=222, blendin=0, layer_weight=.9, play_mode=1, speed=.5)
#    if own["last_fak_nmanual"] == 0:
#        fak_stance_left_off()
#        fak_stance_right_off()
#        skater.playAction("fak_nmanual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)                
#        deck.playAction("a_reg_manual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)
#        trucks.playAction("a_reg_manual", 1,11, layer=3000, blendin=2, layer_weight=.8, play_mode=0, speed=.5)        
    if own["fak_nmanual_timer"] == 41:
        killact(3000)
        killact(3001)
        killact(3002)    
def fak_nmanual_off():
    killact(222)
    killact(223)
    killact(224)  
    killact(3000)
    killact(3001)
    killact(3002)
    killact(10)  
    killact(32)
    killact(11)  
    killact(34)      
    
###########
    
def reg_stanceinc_on():
    skater.playAction("nreg", 1,60, layer=3, blendin=2, layer_weight=0, play_mode=1, speed=.5)        
    deck.playAction("a_reg", 1,40, layer=3, blendin=0, blend_mode=0, play_mode=1, speed=.5)
    trucks.playAction("a_reg", 1,40, layer=3, blendin=2, layer_weight=0, play_mode=1, speed=.5)
def reg_stanceinc_off():
    killact(3)   
    
                
def reg_stance_left_on():
    #if own["reg_manual"] == 0 and own["fak_manual"] == 0 and own["reg_nmanual"] == 0 and own["fak_nmanual"] == 0 :
    if own['manual_v2'] == 0 and own["revert_timer"] < 1:
        own['requestAction'] = 'reg_turnLeft'    
#        skater.playAction("nreg_left", 10,30, layer=10, blendin=10, layer_weight=0, play_mode=1, speed=.5) 
#        deck.playAction("a_reg_left", 10,30, layer=10, blendin=2, layer_weight=0, play_mode=1, speed=.5)
        LAST_LEFT = own["LAST_LEFT"]
        #layer 100 is frame 20
        playing_action_frame = skater.getActionFrame(LAND_LAYER)
        #print(playing_action_frame, "PAF")
        if LAST_LEFT == 0 or (playing_action_frame > (LAND_END - 2) and playing_action_frame < (LAND_END - 1)):
            LAST_LEFT = 1
#            skater.playAction("nreg_left", 1,10, layer=32, blendin=10, layer_weight=0, play_mode=0, speed=.5)
#            deck.playAction("a_reg_left", 1,10, layer=32, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        own["LAST_LEFT"] = 1 
                        
         
def reg_stance_right_on():
    if own['manual_v2'] == 0 and own["revert_timer"] < 1:
        own['requestAction'] = 'reg_turnRight' 
#        skater.playAction("nreg_right", 10,30, layer=11, blendin=10, layer_weight=0, play_mode=1, speed=.5)                
#        deck.playAction("a_reg_right", 10,30, layer=11, blendin=2, layer_weight=0, play_mode=1, speed=.5)
        LAST_RIGHT = own["LAST_RIGHT"]
        playing_action_frame = skater.getActionFrame(LAND_LAYER)
        if LAST_RIGHT == 0 or (playing_action_frame > (LAND_END - 2) and playing_action_frame < (LAND_END - 1)):
            LAST_RIGHT = 1
#            skater.playAction("nreg_right", 1,10, layer=34, blendin=10, layer_weight=0, play_mode=0, speed=.5)
#            deck.playAction("a_reg_right", 1,10, layer=34, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        own["LAST_RIGHT"] = 1 
              
   
def fak_stance_on():
    playing = deck.isPlayingAction(40)
    if own['manual_v2'] == 0 and own["revert_timer"] < 1 and playing == 0:
        own['requestAction'] = 'fak_roll'
        #skater.playAction("nfak", 1,60, layer=3, blendin=4, priority=9, layer_weight=0, play_mode=1, speed=.5)                
        #deck.playAction("a_reg", 1,40, layer=3, blendin=2, priority=9, layer_weight=0, play_mode=1, speed=.5)
        #trucks.playAction("a_reg", 1,40, layer=3, blendin=2, priority=9, layer_weight=0, play_mode=1, speed=.5)    
def fak_stance_off():
    killact(3)
    
def fak_stance_left_on():
    if own['manual_v2'] == 0 and own["revert_timer"] < 1:
        own['requestAction'] = 'fak_turnLeft'     
        #skater.playAction("nfak_left", 10,30, layer=12, blendin=10, layer_weight=0, play_mode=1, speed=.5) 
        #deck.playAction("a_reg_right", 10,30, layer=12, blendin=2, layer_weight=0, play_mode=1, speed=.5)
        LAST_LEFT_FAK = own["LAST_LEFT_FAK"]
        playing_action_frame = skater.getActionFrame(LAND_LAYER)
        if LAST_LEFT_FAK == 0 or (playing_action_frame > (LAND_END - 2) and playing_action_frame < (LAND_END - 1)):
            LAST_LEFT_FAK = 1
            #skater.playAction("nfak_left", 1,10, layer=36, blendin=10, layer_weight=0, play_mode=0, speed=.5)
            #deck.playAction("a_reg_right", 1,10, layer=36, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        own["LAST_LEFT_FAK"] = 1                      
def fak_stance_left_off():
    killact(12)  
    killact(36)
    LAST_LEFT_FAK = own["LAST_LEFT_FAK"]
    #if LAST_LEFT_FAK == 1 and rUD < .06:
        #skater.playAction("nfak_left", 30,40, layer=33, blendin=10, layer_weight=0, play_mode=0, speed=2)
        #deck.playAction("a_reg_left", 30,40, layer=33, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        #deck.playAction("a_reg_right", 30,40, layer=501, play_mode=0, speed=.5)
    own["LAST_LEFT_FAK"] = 0
    
def fak_stance_right_on():
    if own['manual_v2'] == 0 and own["revert_timer"] < 1:
        own['requestAction'] = 'fak_turnRight' 
        #skater.playAction("nfak_right", 10,30, layer=13, blendin=10, layer_weight=0, play_mode=1, speed=.5)                
        #deck.playAction("a_reg_left", 10,30, layer=13, blendin=2, layer_weight=0, play_mode=1, speed=.5)
        LAST_RIGHT_FAK = own["LAST_RIGHT_FAK"]
        #playing_action_frame = skater.getActionFrame(LAND_LAYER)  
        #if LAST_RIGHT_FAK == 0 or (playing_action_frame > (LAND_END - 2) and playing_action_frame < (LAND_END - 1)):
            #LAST_RIGHT_FAK = 1
            #skater.playAction("nfak_right", 1,10, layer=37, blendin=10, layer_weight=0, play_mode=0, speed=.5)
            #deck.playAction("a_reg_left", 1,10, layer=37, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        own["LAST_RIGHT_FAK"] = 1        
def fak_stance_right_off():
    killact(13) 
    killact(37)
    LAST_RIGHT_FAK = own["LAST_RIGHT_FAK"]
    #if LAST_RIGHT_FAK == 1 and rUD < .06:
        #skater.playAction("nfak_right", 30,40, layer=33, blendin=10, layer_weight=0, play_mode=0, speed=2)
        #deck.playAction("a_reg_left", 30,40, layer=33, blendin=10, layer_weight=0, priority=7, play_mode=0, speed=.5)
        #deck.playAction("a_reg_right", 30,40, layer=501, play_mode=0, speed=.5)
    own["LAST_RIGHT_FAK"] = 0    
    
def reg_air_on():
    playing = deck.isPlayingAction(fliplay)
    if playing == False:
        own['requestAction'] = 'reg_air'        
        #skater.playAction("reg_air", 1,60, layer=4, blendin=2, priority=6, layer_weight=0, play_mode=1, speed=.5)    

def reg_air_off():
    killact(4)    
def fak_air_on():
    flipping = skater.isPlayingAction(fliplay)
    if flipping == False:
        own['requestAction'] = 'fak_air' 
        #skater.playAction("fak_air", 1,60, layer=5, blendin=2, priority=9, layer_weight=0, play_mode=1, speed=.5)      
  
def fak_air_off():
    killact(5)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
def stance():
#    turnsens = .04
#    turnblend = 10    
    rotation = .96
    turnsens = 0.06
    if rot.z < .9: inc = 1
    else: inc = 0
    flipping = skater.isPlayingAction(500)
    #print(flipping)
    #ground
    if r_ground.triggered == True and grindHit == False and flipping == False and own["wallride"] == None and own['revert_timer'] < 2:
        if STANCE == 0:
            reg_manual = own['reg_manual']
            fak_manual = own["fak_manual"]
            reg_nmanual = own['reg_nmanual']
            fak_nmanual = own["fak_nmanual"]             
            if LAST_STANCE != STANCE or LAST_GROUND != r_ground.triggered:
                fak_stance_off()
                reg_air_off()
                fak_air_off()
            if reg_manual == 0 and fak_manual == 0:  
                last_manual = own['last_reg_manual']
                if last_manual == 1:
                    reg_manual_off()                   
                    fak_manual_off()
                reg_stance_on()
#            if own['last_manual'] == 1:
#                if STANCE == 0:
#                    if fak_manual == 1:
#                        fak_manual = 0
#                        reg_nmanual = 1
#                        own['reg_nmanual'] = 1
#                        print("changing manual")
                                            
            #if reg_manual == 1 and fak_manual == 0 and reg_nmanual == 0 and fak_nmanual == 0:
            #if reg_manual == 1 and fak_manual == 0 and reg_nmanual == 0:
            if own['manual_v2_type'] == 'reg manual':    
                reg_manual_on()                   
            #elif reg_manual == 0 and fak_manual == 0 and reg_nmanual == 1 and fak_nmanual == 0:
            elif own['manual_v2_type'] == 'reg nose manual':    
                reg_nmanual_on()
            #elif reg_manual == 0 and fak_manual == 1 and reg_nmanual == 0 and fak_nmanual == 0: 
            elif own['manual_v2_type'] == 'fak manual':
                #reg_nmanual_on()
                fak_manual_on()
            #elif reg_manual == 0 and fak_manual == 0 and reg_nmanual == 0 and fak_nmanual == 1: 
            elif own['manual_v2_type'] == 'fak nose manual':
                #reg_manual_on()
                fak_nmanual_on()
        if STANCE == 1:
            reg_manual = own['reg_manual']
            fak_manual = own["fak_manual"]
            reg_nmanual = own['reg_nmanual']
            fak_nmanual = own["fak_nmanual"]
            if LAST_STANCE != STANCE or LAST_GROUND != r_ground.triggered:    
                #fak_manual_off()
                #reg_manual_off()
                #print("turn man off")
                reg_stance_off()
                reg_air_off()
                fak_air_off 
            if fak_manual == 0:                    
                last_manual = own['last_fak_manual']
                if last_manual == 1:
                    fak_manual_off()
                    reg_manual_off()
                fak_stance_on()                    
            #if reg_manual == 0 and fak_manual == 1 and reg_nmanual == 0 and fak_nmanual == 0:
            if own['manual_v2_type'] == 'fak manual':
                fak_manual_on()
            #elif reg_manual == 0 and fak_manual == 0 and reg_nmanual == 0 and fak_nmanual == 1:
            elif own['manual_v2_type'] == 'fak nose manual':
                fak_nmanual_on()
            #elif reg_manual == 1 and fak_manual == 0 and reg_nmanual == 0 and fak_nmanual == 0: 
            elif own['manual_v2_type'] == 'reg manual':
                #fak_nmanual_on() 
                reg_manual_on()
            #elif reg_manual == 0 and fak_manual == 0 and reg_nmanual == 1 and fak_nmanual == 0: 
            elif own['manual_v2_type'] == 'reg nose manual':
                #fak_manual_on() 
                reg_nmanual_on()                     
            #fak_stance_on()
        if own["Pump"] == False:
            
            if lLR < -turnsens and STANCE == 0:            
                reg_stance_left_on()
            if lLR > -turnsens or LAST_GRIND != grindHit:
                reg_stance_left_off()    
            if lLR > turnsens and STANCE == 0:
                reg_stance_right_on()
            if lLR < turnsens or LAST_GRIND != grindHit:
                reg_stance_right_off()   
            if lLR < -turnsens and STANCE == 1:            
                fak_stance_left_on()
            if lLR > -turnsens or LAST_GRIND != grindHit:
                fak_stance_left_off()    
            if lLR > turnsens and STANCE == 1:
                fak_stance_right_on()
            if lLR < turnsens or LAST_GRIND != grindHit:
                fak_stance_right_off()                       
    #air
    playing = deck.isPlayingAction(fliplay)
    #playing = False
    if r_ground.triggered == False and playing == False and flipping == False:
        if STANCE == 0:
            #if LAST_STANCE != STANCE or r_ground.triggered:
            if LAST_STANCE != STANCE or LAST_GROUND != r_ground.triggered:                
                fak_air_off()
                reg_stance_off()
                fak_stance_off()
                reg_stance_left_off() 
                reg_stance_right_off()
                fak_stance_left_off()  
                fak_stance_right_off() 
#                reg_manual_off()
#                fak_manual_off()
            reg_air_on()
        if STANCE == 1:
            if LAST_STANCE != STANCE or LAST_GROUND != r_ground.triggered:
                reg_air_off()  
                reg_stance_off()
                fak_stance_off()  
                reg_stance_left_off()
                reg_stance_right_off()
                fak_stance_left_off()  
                fak_stance_right_off()  
#                reg_manual_off()
#                fak_manual_off()                        
            fak_air_on()
    if grindHit == True:
        reg_stance_off()
        fak_stance_off()        
                       
###################
#trick definitions#
###################
def jump():
    #print("jump funct")
    jump_timer = own['jump_timer']
    
    reg_manual_off()
    fak_manual_off()
    reg_nmanual_off()
    fak_nmanual_off()    
    #grindold
    #fak_manual_off()
    #print(JUMPSTRENGTH)
    cont.deactivate(wallrideconstL)
    cont.deactivate(wallrideconstR)    
    if JUMPSTRENGTH != 0:
        height = JUMPSTRENGTH * JUMPHEIGHT
    else:
        height = JUMPHEIGHT    
    #if jump_timer == 0:
    if jump_timer < 50:    
        jump_timer = 60
        own['jump_timer'] = jump_timer
            
    if zvel < 7 and jump_timer == 60:
        cont.activate(own.actuators["pop"])
        own['pop_sound'] = 1
        print("jump")
        #
        posx = own.worldPosition[0]
        posy = own.worldPosition[1]
        posz = own.worldPosition[2]
        jumppos = Vector((posx, posy, posz))
        own['jumpPos'] = jumppos  
        force = [ 0.0, 0.0, height]
        # use local axis
        local = False
        # apply force
        try:
            if 'trans' in r_ground.hitObject:
                print('jump from trans')
                own['jump_from_trans'] = 1
                own['trans_jump_obj'] = r_ground.hitObject
        except:
            print('trans jump broke')
        if grindHit == False:
            own.applyForce(force, local)
            force2 = [0.0, 0, 150]
            own.applyForce(force2, True)
            #print("apply jump force1")
        if grindHit == True:
            linvelloc = own.getLinearVelocity(True)
            own.applyForce(force, True)
            force2 = [0.0, 0, 150]
            own.applyForce(force2, True) 
            linvelloc2 = own.getLinearVelocity(True)
            force = (linvelloc.x, linvelloc.y, linvelloc2.z)
            own.setLinearVelocity(force, True) 
            #print("apply jump force2 grindHit")          
                
        own['jump_stance'] = STANCE
        if STANCE == True:
            own["jump_stance"] = 1
        if STANCE == False:
            own["jump_stance"] = 0        
        #own["jump_stance"] = own["stance"]
        if grindHit == True:
            own['grind_jump'] = 1
            if lLR > turnsens or lLR < -turnsens or lUD > turnsens or lUD < -turnsens:
                own['grindjumpturn'] = True
                #print("turn on grindjumpturn")
    num = 1            
    if num ==1:                
        rString = "R"        
        lString = "L"
        cont.deactivate(wallrideconstL)
        cont.deactivate(wallrideconstR)
        #print("deactivating constraints")
        if own["wallride"] == "R":
            force = [0,170,0]
            own.applyForce(force, True)
            print("****walljumpforce R")
            cont.activate(own.actuators["pop2"])
            jump_timer = 60
            own['jump_timer'] = jump_timer            
        if own["wallride"] == "L":
            force = [0,-170,0] #325
            own.applyForce(force, True)                    
            print("****walljumpforce L")
            cont.activate(own.actuators["pop2"])
            jump_timer = 60
            own['jump_timer'] = jump_timer
            
            own["Q1oncd"] = 0
        own["Q2oncd"] = 0
        own["Q3oncd"] = 0
        own["Q4oncd"] = 0
        own["Q5oncd"] = 0
        own["Q6oncd"] = 0
        own["Q7oncd"] = 0
        own["Q8oncd"] = 0         
#        if rot.z < .4:
#            force = [-1, linVelocity.y, linVelocity.z]
#            own.setLinearVelocity(force, local)
    if own['jump_timer'] == 60:
        own['jump_timer'] = 59

def jump_Timer():
    jump_timer = own['jump_timer']
    if jump_timer == 1:
        pass
    if jump_timer > 0:
        jump_timer = jump_timer - 1
        own['jump_timer'] = jump_timer 
    if own['grindjumpturn'] == True:
        jump_timer = 30
        own['jump_timer'] = jump_timer           
        

def pump():
    velocity = own['velocity']
    #regular
    local = True
    downforce = -.1
    if linVelocity.x < MAX_VEL and linVelocity.x >= -0 and STANCE == 1 and grindHit == False:
        countdown = COUNTDOWN
        yvel = linVelocity.x + SPEEDPUMP
        yvel2 = linVelocity.x + SPEEDPUMPFAST
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity.z + downforce]
        force2 = [(yvel2), 0, linVelocity.z + downforce]
        if rot.z < PUMP_SENS and rot.z > PUMP_SPEED_SENS:
            own.setLinearVelocity(force, local)
        if rot.z < PUMP_SENS and rot.z <= PUMP_SPEED_SENS:
            own.setLinearVelocity(force2, local)
        own['requestAction'] = 'fak_pump'
        #skater.playAction("nfak_pump.001", 1,60, layer=20, priority=8, blendin=10, play_mode=1, speed=.5)
        #skater.playAction("nopos", 1,40, layer=0, priority=7, blendin=10, play_mode=3, speed=.5)    
        if lastpump == False:        
            #skater.playAction("nfak_pump_in", 1,20, layer=350, priority=8, blendin=10, play_mode=0, speed=1)
            #cont.activate(fak_pumpin)
            pass
    #switch
    if linVelocity.x > -MAX_VEL and linVelocity.x <= 0 and STANCE == 0 and grindHit == False:
        countdown = COUNTDOWN
        yvel = linVelocity.x - SPEEDPUMP
        yvel2 = linVelocity.x - SPEEDPUMPFAST
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity.z + downforce]
        force2 = [(yvel2), 0, linVelocity.z + downforce]
        if rot.z < PUMP_SENS and rot.z > PUMP_SPEED_SENS:
            own.setLinearVelocity(force, local)
        if rot.z < PUMP_SENS and rot.z <= PUMP_SPEED_SENS:
            own.setLinearVelocity(force2, local)
        own['requestAction'] = 'reg_pump'    
        #skater.playAction("nreg_pump", 1,60, layer=21, priority=8, blendin=10, play_mode=1, speed=.5)
        
        if lastpump == False:
            #skater.playAction("nreg_pump_in", 1,20, layer=350, priority=8, blendin=10, play_mode=0, speed=1)
            #cont.activate(reg_pumpin)
            pass
    #force = [ 0, 0, -200]
    #own.applyForce(force, 0) # apply force    
    own["Pump"] = True
    own["lastPump"] = True
            
def roll():
    if r_ground.triggered == 1:  
        pass      
def stop():
    #if r_ground.triggered == 1 and STANCE == False and linVelocity.x < -.1:
    if r_ground.triggered == 1 and STANCE == False:        
        skater.playAction("reg_stop", 1,30, layer=18, priority=59, blendin=10, play_mode=1, speed=.5)
        yvel = linVelocity.x * .985
        force = [(yvel), 0, linVelocity.z]
        own.setLinearVelocity(force, True)
        if lastStop == False:
            skater.playAction("reg_stopin", 1,15, layer=61, priority=3, blendin=10, play_mode=0, speed=.5)
    #elif r_ground.triggered == 1 and STANCE == True and linVelocity.x > .1:
    elif r_ground.triggered == 1 and STANCE == True:
        skater.playAction("fak_stop", 1,30, layer=19, priority=7, blendin=10, play_mode=1, speed=.5)
        yvel = linVelocity.x * .985
        force = [(yvel), 0, linVelocity.z]
        own.setLinearVelocity(force, True)
        if lastStop == False:
            skater.playAction("fak_stopin", 1,15, layer=62, priority=3, blendin=10, play_mode=0, speed=.5)
    own["lastStop"] = True
#    if linVelocity.x < .1:
#        force = [0, 0, linVelocity.z]
#        own.setLinearVelocity(force, True)
    if linVelocity.x < .05 and linVelocity.x > -.05 and own["lastStop"] == True:
        own["lastStop"] == False   
        skater.stopAction(7)
        skater.stopAction(1) 
        if STANCE == True:
            skater.playAction("fak_stopin", 15,1, layer=63, priority=3, blendin=10, play_mode=0, speed=.5)
        elif STANCE == False:
            skater.playAction("reg_stopin", 15,1, layer=64, priority=3, blendin=10, play_mode=0, speed=.5)    

def oposin():
    if skater.isPlayingAction(30) or skater.isPlayingAction(31):
        landing = 1
    else:
        landing = 0     
    if (r_ground.triggered == 1) and STANCE == False and landing == 0 and own['manual'] == 0:
        if grindold == 0:
            own['requestAction'] = 'reg_opos'
        #if lastopos == False:
            #skater.playAction("noposin", 1,20, layer=65, priority=3, blendin=10, play_mode=0, speed=.5)
        #else:
            #skater.playAction("nopos", 1,40, layer=67, priority=7, blendin=10, play_mode=1, speed=.5)    
    elif (r_ground.triggered == 1) and STANCE == True and own['manual'] == 0:
        if grindold == 0:
            own['requestAction'] = 'fak_opos'
        #skater.playAction("fak_opos", 1,40, layer=68, priority=7, blendin=10, play_mode=1, speed=.5)
        #if lastopos == False:
            #skater.playAction("fak_oposin", 1,20, layer=66, priority=3, blendin=10, play_mode=0, speed=.5)
    else:
        killact(65)
        killact(66)
        killact(67)
        killact(68)          
    own["last_Opos"] = True
    
def noposin():
    if skater.isPlayingAction(30) or skater.isPlayingAction(31):
        landing = 1
    else:
        landing = 0    
    if (r_ground.triggered == 1) and STANCE == False and landing == 0 and own['manual'] == 0:
        #pass
        if grindold == 0:
            own['requestAction'] = 'reg_nopos'
#        skater.playAction("nnopos", 1,40, layer=73, priority=8, blendin=10, play_mode=1, speed=.5)
#        if lastnopos == False:
#            skater.playAction("nnoposin", 1,20, layer=71, priority=4, blendin=10, play_mode=0, speed=.5)
    elif (r_ground.triggered == 1) and STANCE == True and own['manual'] == 0:
        if grindold == 0:
            own['requestAction'] = 'fak_nopos'
#        if lastnopos == False:
#            skater.playAction("fak_noposin", 1,20, layer=72, priority=4, blendin=10, play_mode=0, speed=.5)
#        else:
#            skater.playAction("fak_nopos", 1,40, layer=74, priority=8, blendin=10, play_mode=1, speed=.5)                
    else:        
        killact(71)
        killact(72)
        killact(73)
        killact(74)         
    own["last_nOpos"] = True    
            
def aollie():
    print("ollie")
    dict['trick_string'] = 'Ollie'
    r_ground = cont.sensors["r_Ground"]
    trigger = r_ground.triggered
    STANCE = own["stance"]
    wallride = own["wallride"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_ollie'
        jump()  
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_ollie'
        jump()

def nollie():
    print("nollie")
    dict['trick_string'] = 'Nollie'
    r_ground = cont.sensors["r_Ground"]
    trigger = r_ground.triggered
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own['requestAction'] = 'fak_nollie'
        own["wallride_off"] = 1
        jump()  
    elif (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie'
        jump()  
  

def kickflip():
    print("kickflip")
    dict['trick_string'] = 'Kickflip'
    STANCE = own["stance"]
    print(flip_start_lay)
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_kickflip'       
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_kickflip'       
        jump()
        if own["wallride"] !=1: jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_kickflip'
        if own["wallride"] != None: 
            jump()  
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_kickflip'
        if own["wallride"] != None: 
            jump()
            
def varial_kickflip():
    print("varial kickflip")
    dict['trick_string'] = 'Varial Kickflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_varial_kickflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_varial_kickflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()              
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
            
def nollie_varial_kickflip():
    print("nollie varial kickflip")
    dict['trick_string'] = 'Nollie Varial Kickflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_varial_kickflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_varial_kickflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()              
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
            
def nollie_varial_heelflip():
    print("nollie varial heelflip")
    dict['trick_string'] = 'Nollie Varial Heelflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_varial_heelflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_varial_heelflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()              
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()            
                        
def varial_heelflip():
    print("varial heelflip")
    dict['trick_string'] = 'Varial Heelflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_varial_heelflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_varial_heelflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()              
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()            
            
def nollie_kickflip():
    print("kickflip")
    STANCE = own["stance"]
    dict['trick_string'] = 'Nollie Kickflip'
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_kickflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_kickflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None:
            print("wall out trick") 
            #jump()  
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None:
            print("wall out trick") 
            #jump()
    
def heelflip():
    print("heelflip")
    dict['trick_string'] = 'Heelflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_heelflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_heelflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None:
            print("wall out trick")
            #jump()
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None:
            print("wall out trick") 
            #jump()
def nollie_heelflip():
    print("heelflip")
    dict['trick_string'] = 'Nollie Heelflip'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_heelflip'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or (grindHit == True and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_heelflip'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()        
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       

def shovit():
    print("shovit")
    dict['trick_string'] = 'Shovit'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_shovit'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_shovit'
        jump()
    if r_ground.triggered == 0 and STANCE == False:     
        if own["wallride"] != None: 
            jump()  
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
def shovit360():
    print("360shovit")
    dict['trick_string'] = '360 Shovit'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_shovit360'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_shovit360'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()        
def fsshovit360():
    print("360shovit")
    dict['trick_string'] = '360 Shovit'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_fsshovit360'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_fsshovit360'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
def nollie_shovit():
    print("shovit")
    dict['trick_string'] = 'Nollie Shovit'
    STANCE = own["stance"]
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_shovit'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_shovit'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()        

def fsshovit():
    dict['trick_string'] = 'Frontside Shovit'
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_fsshovit'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or ((grindHit == True or wallride != None) and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_fsshovit'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()        
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
        
def nollie_fsshovit():
    dict['trick_string'] = 'Nollie Frontside Shovit'
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_fsshovit'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or (grindHit == True and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_fsshovit'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()
 
#nollie_shovit360()
def nollie_shovit360():
    dict['trick_string'] = 'Nollie Frontside Shovit 360'
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_shovit360'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or (grindHit == True and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_shovit360'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump() 


#nollie_fsshovit360()
def nollie_fsshovit360():
    dict['trick_string'] = 'Nollie Frontside Shovit'
    if (r_ground.triggered == 1 and STANCE == False) or ((grindHit == True or wallride != None) and STANCE == False):
        own["wallride_off"] = 1
        own['requestAction'] = 'reg_nollie_fsshovit'
        jump()
    elif (r_ground.triggered == 1 and STANCE == True) or (grindHit == True and STANCE == True):
        own["wallride_off"] = 1
        own['requestAction'] = 'fak_nollie_fsshovit'
        jump()
    if r_ground.triggered == 0 and STANCE == False:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()       
    elif r_ground.triggered == 0 and STANCE == True:
        own["wallride_off"] = 1
        if own["wallride"] != None: 
            jump()             
    
def frontside_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    dict['trick_string'] = 'Mute Grab'
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:         
        own['requestAction'] = 'frontside_grab'
        #skater.playAction("reg_fg", 10,30, layer=400, priority=5, play_mode=1, speed=.5)
        grablay2 = grablay + 1

        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(400)
        killact(401)
            
def backside_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    
    
    if GRAB_ON == True and r_ground.triggered == 0 and aBut == True:
        
        skater.playAction("reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
        deck.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
        trucks.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)          
    elif GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:
        own['requestAction'] = 'backside_grab'        
        #skater.playAction("reg_bsg2", 10,30, layer=402, priority=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(402)              
        
def fakfrontside_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]

    if GRAB_ON == True and r_ground.triggered == 0 and aBut == True:    
        skater.playAction("fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
        deck.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
        trucks.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)     
    
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:           
        #cont.activate(fak_frontsidegrab)
        own['requestAction'] = 'fak_frontside_grab' 
        #skater.playAction("fak_fg", 10,30, layer=403, priority=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
        #print("frontside_grab_on")
    elif r_ground.triggered == 1:        
        killact(403)
    
def fakbackside_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:         
        #cont.activate(fak_backsidegrab)
        own['requestAction'] = 'fak_backside_grab' 
        #skater.playAction("fak_bg", 10,30, layer=404, priority=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(404)
        
#nose/tail grabs        
def frontside_nose_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:
        own['requestAction'] = 'frontside_nose_grab' 
        #cont.activate(fak_backsidegrab)
        #skater.playAction("frontside_nose_grab", 10,30, layer=400, priority=5,  blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(400)
    print("frontside nosegrab on")
def frontside_tail_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0: 
        own['requestAction'] = 'frontside_tail_grab' 
        #cont.activate(fak_backsidegrab)
        #skater.playAction("frontside_tail_grab", 10,30, layer=409, priority=5,  blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(400)    
    print("frontside tailgrab on")  
def backside_nose_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    #airwalk
    #if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0 and (aBut == True):
    if GRAB_ON == True and r_ground.triggered == 0 and (aBut == True):    
        print("airwalk")
        skater.playAction("reg_airwalk", 10,30, layer=405, priority=5, blendin=5, play_mode=1, speed=.5)
        deck.playAction("a_reg_airwalk", 10,30, layer=405, priority=5, blendin=5, play_mode=1, speed=.5)
        trucks.playAction("a_reg_airwalk", 10,30, layer=405, priority=5, blendin=5, play_mode=1, speed=.5)
    
    #norm
    elif GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:   
        #cont.activate(fak_backsidegrab)
        own['requestAction'] = 'backside_nose_grab' 
        #skater.playAction("backside_nose_grab", 10,30, layer=405, priority=5, blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(405)    
    print("backside nosegrab on")
def backside_tail_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0: 
        own['requestAction'] = 'backside_tail_grab' 
        #cont.activate(fak_backsidegrab)
        #skater.playAction("backside_tail_grab", 10,30, layer=411, priority=5,  blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(411)    
    print("backside tailgrab on")
#switch    
def fak_frontside_nose_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:  
        own['requestAction'] = 'fak_frontside_nose_grab' 
        #cont.activate(fak_backsidegrab)
        #skater.playAction("fak_frontside_nose_grab", 10,30, layer=406, priority=5, blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(406)      
    print("fak frontside nosegrab on")
def fak_frontside_tail_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:           
        #cont.activate(fak_backsidegrab)
        own['requestAction'] = 'fak_frontside_tail_grab' 
        #skater.playAction("fak_frontside_tail_grab", 10,30, layer=412, priority=5,  blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(412)    
    print("fak frontside tailgrab on")  
def fak_backside_nose_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:           
        #cont.activate(fak_backsidegrab)
        own['requestAction'] = 'fak_backside_nose_grab' 
        #skater.playAction("fak_backside_nose_grab", 10,30, layer=408, priority=5, blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(408)         
    print("fak backside nosegrab on")
def fak_backside_tail_grab_on():
    GRAB_PLAYED = own["GRAB_PLAYED"]
    GRAB_ON = own["GRAB_ON"]
    if GRAB_ON == True and GRAB_PLAYED == False and r_ground.triggered == 0:           
        #cont.activate(fak_backsidegrab)
        own['requestAction'] = 'fak_backside_tail_grab' 
        #skater.playAction("fak_backside_tail_grab", 10,30, layer=410, priority=5,  blendin=5, play_mode=1, speed=.5)
        GRAB_PLAYED = True
        own["GRAB_PLAYED)"] = GRAB_PLAYED
    elif r_ground.triggered == 1:
        killact(410)    
    print("fak backside tailgrab on")         
#--------------------
        
def SWAG():
    if r_ground.triggered == 1:
        SWAG = own["swag"]
        SWAG = own.getLinearVelocity(True)
        SWAG = SWAG[1]
        own["swag"] = SWAG
        #print(SWAG)
        if STANCE == True:
            if SWAG > 1 and SWAG < 2:
                rotation = [ 0.0, 0, (SWAG / 200)]
                own.applyRotation( rotation, True)        
            elif SWAG > 2:
                rotation = [ 0.0, 0, (SWAG / 50)]
                own.applyRotation( rotation, True)
            elif SWAG < -1 and SWAG > -2:
                rotation = [ 0.0, 0, (SWAG / 200)]
                own.applyRotation( rotation, True)
            elif SWAG < -2:
                rotation = [ 0.0, 0, (SWAG / 50)]
                own.applyRotation( rotation, True)
        if STANCE == False:
            if SWAG > 1 and SWAG < 2:
                rotation = [ 0.0, 0, (-SWAG / 200)]
                own.applyRotation( rotation, True)        
            elif SWAG > 2:
                rotation = [ 0.0, 0, (-SWAG / 50)]
                own.applyRotation( rotation, True)
            elif SWAG < -1 and SWAG > -2:
                rotation = [ 0.0, 0, (-SWAG / 200)]
                own.applyRotation( rotation, True)
            elif SWAG < -2:
                rotation = [ 0.0, 0, (-SWAG / 50)]
                own.applyRotation( rotation, True) 
                
def air():
    if r_ground.triggered == False and own['airup'] == 0:
         
        distance = own.getDistanceTo(gray.hitPosition)
        #print(frame - lgf, "frames since grind")
        since_grind_buf = 3
        if gray.hitObject != None and grindDar2.triggered == False and (frame - lgf) > since_grind_buf:
        #if gray.hitObject != None and grindDar2.triggered == False:
            if distance < .5:  
                own.alignAxisToVect(gray.hitNormal, 2, .1)
            elif distance >= .5 and distance < 1.75:  
                own.alignAxisToVect(gray.hitNormal, 2, .05)
            elif distance >= 1.75:  
                own.alignAxisToVect([0.0,0.0,1.0], 2, .03)
#            own.alignAxisToVect(gray.hitNormal, 2, .01)
        if grindDar2.triggered and (frame - lgf) > since_grind_buf:
            #print("grindar2")  
            #own.alignAxisToVect(gray.hitNormal, 2, .075)
            if distance < .5:  
                own.alignAxisToVect(gray.hitNormal, 2, .1)
            elif distance >= .5 and distance < 1.75:  
                own.alignAxisToVect(gray.hitNormal, 2, .03)
            elif distance >= 1.75:  
                own.alignAxisToVect([0.0,0.0,1.0], 2, .03)            
    elif r_ground.triggered == True:
        pass
def stopAnims():
    pass       
    
def isplaying():
#    for x in range(9000):
#        l1 = deck.isPlayingAction(x)
#        if l1 == True:
#            print(x)
    pass

def nextframe():
    framenumber = own["framenum"]
    framenumber = framenumber + 1
    if framenumber == 900000:
        framenumber = 0
    own["framenum"] = framenumber
    #print(framenumber)
    
def push():
    local = True
    #print("push")
    linVelocity15 = own.linearVelocity
    if linVelocity15.x < MAX_VEL and linVelocity15.x >= -0 and r_ground.triggered == True and own['hippy'] == 0 and own['last_hippy'] == 0 and own['last_footplant'] == False:
        countdown = COUNTDOWN
        yvel = linVelocity15.x + SPEEDUP
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity15.z]
        #killall()
        own.setLinearVelocity(force, local)
        own['requestAction'] = 'fak_push_goof'
        #skater.playAction("fak_push_goof", 1,35, layer=100, blendin=2, play_mode=0, speed=.5)
    #switch
    if linVelocity15.x > -MAX_VEL and linVelocity15.x < 0 and r_ground.triggered == True and own['hippy'] == 0 and own['last_hippy'] == 0:
        countdown = COUNTDOWN
        yvel = linVelocity15.x - SPEEDUP
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity15.z]
        #killall()
        own.setLinearVelocity(force, local)
        own['requestAction'] = 'reg_push'
        #skater.playAction("reg_push", 1,35, layer=101, blendin=2, play_mode=0, speed=.5)
def push_goof():
    linVelocity15 = own.linearVelocity
    local = True
    #print("push goof")
    if linVelocity15.x < MAX_VEL and linVelocity15.x >= -0 and r_ground.triggered == True and own['hippy'] == 0 and own['last_hippy'] == 0:
        countdown = COUNTDOWN
        yvel = linVelocity15.x + SPEEDUP
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity15.z]
        #killall()
        own.setLinearVelocity(force, local)
        own['requestAction'] = 'fak_push'
        #skater.playAction("fak_push", 1,35, layer=100, blendin=2, play_mode=0, speed=.5)
    #switch
    if linVelocity15.x > -MAX_VEL and linVelocity15.x < 0 and r_ground.triggered == True and own['hippy'] == 0 and own['last_hippy'] == 0:
        countdown = COUNTDOWN
        yvel = linVelocity15.x - SPEEDUP
        own['countdown'] = countdown
        force = [(yvel), 0, linVelocity15.z]
        #killall()
        own.setLinearVelocity(force, local)
        own['requestAction'] = 'reg_push_goof'
        #skater.playAction("reg_push_goof", 1,35, layer=101, blendin=2, play_mode=0, speed=.5)        
def brfoot():
    lay = grablay + 40
    killact(5)
    #killall()
    if STANCE == 0:
        skater.playAction("brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("1: Correct")
    if STANCE == 1:
        skater.playAction("fak_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED) 
        #print("2: Correct")       
    jump()    
def frfoot():
    lay = grablay + 40
    killact(5)
    #killall()
    if STANCE == 0:
        skater.playAction("frfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("frfoot")
    if STANCE == 1:
        skater.playAction("fakbfrfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("!fak_frfoot.001")        
    jump()          
    #lastpush
def blfoot():
    lay = grablay + 40
    killact(5)
    #killall()
    if STANCE == 0:
        skater.playAction("blfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("blfoot")
    if STANCE == 1:
        skater.playAction("fakfrfoot.001", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("correct fakfrfoot.001")
    jump() 
def flfoot():
    lay = grablay + 40
    killact(5)
    #killall()
    if STANCE == 0:
        skater.playAction("flfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        #print("3: Correct")
    if STANCE == 1:
        skater.playAction("fak_flfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        deck.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED)
        trucks.playAction("a_brfoot", 1, 30, layer=lay, blendin=2, play_mode=0, speed=CAVEMAN_SPEED) 
        #print("4: wrong - fak_flfoot")       
    jump()         
def rollsound():
    #onground
    if r_ground.triggered == 1 and grindDar == 0 and own['invert_on'] == 0:
        num1 = .05
        num2 = .25
        if linVelocity.x <= -num1 and linVelocity.x >= num1:
            own.actuators["sroll"].volume = .0001
            cont.deactivate(own.actuators["sroll"])
            own.actuators["sroll"].stopSound()
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .02
            own.actuators["sroll"].pitch = .65
        num1 = .25
        num2 = .5
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .03
            own.actuators["sroll"].pitch = .7             
        num1 = .5
        num2 = .75
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .04
            own.actuators["sroll"].pitch = .75   
        num1 = .75
        num2 = 1
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .05
            own.actuators["sroll"].pitch = .8 
        num1 = 1
        num2 = 1.5
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .06
            own.actuators["sroll"].pitch = .85             
        num1 = 1.5
        num2 = 2
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .07
            own.actuators["sroll"].pitch = .9  
        num1 = 2
        num2 = 3
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .08
            own.actuators["sroll"].pitch = .95   
        num1 = 3
        num2 = 4
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .09
            own.actuators["sroll"].pitch = 1
        num1 = 4
        num2 = 5
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .11
            own.actuators["sroll"].pitch = 1.05                                                                 
        num1 = 5
        num2 = 6
        if (linVelocity.x > num1 and linVelocity.x < num2) or (linVelocity.x < -num1 and linVelocity.x > -num2):   
            own.actuators["sroll"].volume = .1
            own.actuators["sroll"].pitch = 1.1 
        #play sound
        #own.actuators["sroll"].volume = .1
        own.actuators['sroll'].mode = 2
        cont.activate(own.actuators["sroll"]) 
    if grindDar == 1 or own['invert_on'] == 1:  
        own.actuators["sroll"].volume = .0001  
        cont.deactivate(own.actuators["sroll"])     
        own.actuators["sroll"].stopSound() 
    #in air        
    if r_ground.triggered == False:
        own.actuators["sroll"].volume = .0001
        cont.deactivate(own.actuators["sroll"])     
        own.actuators["sroll"].stopSound() 
        
    act = cont.actuators["sroll"]
    own['sroll_vol'] = act.volume
    own['sroll_pitch'] = act.pitch    
        
def wheelroll():
    #own.actuators["sroll"].volume = .1
    #still
    if linVelocity.x <= -0.05 and linVelocity.x >= 0.05:
        wheel1.stopAction(2)
        wheel2.stopAction(2)
        wheel3.stopAction(2)
        wheel4.stopAction(2)
        #cont.deactivate(own.actuators["sroll"])
        #own.actuators["sroll"].stopSound() 
    #regular
    if linVelocity.x > 0.05 and linVelocity.x < .5:
        wheel2.playAction("roll1.001", 1,20, layer=2, play_mode=0, speed=.25)
        wheel3.playAction("roll2.001", 1,20, layer=2, play_mode=0, speed=.25)
        wheel4.playAction("roll3.001", 1,20, layer=2, play_mode=0, speed=.25)
        wheel1.playAction("roll4.001", 1,20, layer=2, play_mode=0, speed=.25)
    if linVelocity.x > 0.5 and linVelocity.x < 1:
        wheel2.playAction("roll1.001", 1,20, layer=2, play_mode=1, speed=1)
        wheel3.playAction("roll2.001", 1,20, layer=2, play_mode=1, speed=1)
        wheel4.playAction("roll3.001", 1,20, layer=2, play_mode=1, speed=1)
        wheel1.playAction("roll4.001", 1,20, layer=2, play_mode=1, speed=1)
    if linVelocity.x > 1 and linVelocity.x < 4:
        wheel2.playAction("roll1.001", 1,20, layer=2, play_mode=1, speed=1.5)
        wheel3.playAction("roll2.001", 1,20, layer=2, play_mode=1, speed=1.5)
        wheel4.playAction("roll3.001", 1,20, layer=2, play_mode=1, speed=1.5)
        wheel1.playAction("roll4.001", 1,20, layer=2, play_mode=1, speed=1.5)
    if linVelocity.x > 4:
        wheel2.playAction("roll1.001", 1,20, layer=2, play_mode=1, speed=2)
        wheel3.playAction("roll2.001", 1,20, layer=2, play_mode=1, speed=2)
        wheel4.playAction("roll3.001", 1,20, layer=2, play_mode=1, speed=2)
        wheel1.playAction("roll4.001", 1,20, layer=2, play_mode=1, speed=2)
    #switch
    if linVelocity.x < -0.05 and linVelocity.x > -.5:
        wheel2.playAction("roll1.001", 20,1, layer=2, play_mode=0, speed=.25)
        wheel3.playAction("roll2.001", 20,1, layer=2, play_mode=0, speed=.25)
        wheel4.playAction("roll3.001", 20,1, layer=2, play_mode=0, speed=.25)
        wheel1.playAction("roll4.001", 20,1, layer=2, play_mode=0, speed=.25)
    if linVelocity.x < -0.5 and linVelocity.x > -1:
        wheel2.playAction("roll1.001", 20,1, layer=2, play_mode=1, speed=1)
        wheel3.playAction("roll2.001", 20,1, layer=2, play_mode=1, speed=1)
        wheel4.playAction("roll3.001", 20,1, layer=2, play_mode=1, speed=1)
        wheel1.playAction("roll4.001", 20,1, layer=2, play_mode=1, speed=1)
    if linVelocity.x < -1 and linVelocity > -4:
        wheel2.playAction("roll1.001", 20,1, layer=2, play_mode=1, speed=1.5)
        wheel3.playAction("roll2.001", 20,1, layer=2, play_mode=1, speed=1.5)
        wheel4.playAction("roll3.001", 20,1, layer=2, play_mode=1, speed=1.5)
        wheel1.playAction("roll4.001", 20,1, layer=2, play_mode=1, speed=1.5)       
    if linVelocity.x < -4:
        wheel2.playAction("roll1.001", 20,1, layer=2, play_mode=1, speed=2)
        wheel3.playAction("roll2.001", 20,1, layer=2, play_mode=1, speed=2)
        wheel4.playAction("roll3.001", 20,1, layer=2, play_mode=1, speed=2)
        wheel1.playAction("roll4.001", 20,1, layer=2, play_mode=1, speed=2) 

def transspeed():
    num1 = .1
    num2 = .4
    speed = 20
#    if rot.z > num1 and rot.z < num2 and r_ground.triggered == True:
#        if STANCE == 1:
#            force = [speed, 0, 0]
#        else:
#            force = [-speed, 0, 0]
#        own.applyForce(force, True)
#    num1 = .4
#    num2 = .6
#    speed = 40
#    if rot.z > num1 and rot.z < num2 and r_ground.triggered == True:
#        if STANCE == 1:            
#            force = [speed, 0, 0]
#        else:
#            force = [-speed, 0, 0]            
#        own.applyForce(force, True)
#    num1 = .6
#    num2 = .8
#    speed = 20
#    if rot.z > num1 and rot.z < num2 and r_ground.triggered == True:
#        if STANCE == 1:
#            force = [speed, 0, 0]
#        else:
#            force = [-speed, 0, 0]
#        own.applyForce(force, True)               
    
def turn():   
    rotamt = .02
    linVelocity2 = own.getLinearVelocity(True)
    speed = .002
    #force = [speed, 0, 0]
    #print(lLR)
    manual = 0
    #if (own['fak_nmanual'] == 1 or own['reg_nmanual'] == 1 or own['fak_manual'] == 1 or own['reg_manual'] == 1): 
    if own['manual_v2'] == 1:     
        manual = 1       
        if abs(linVelocity.x) < 2:
            speed = .005
            
    jumpstance = own['jump_stance']
    if lLR > turnsens or lLR < -turnsens:
        own["turn"] = 1
    else:
        own["turn"] = 0
    if lUD > turnsens or lUD < -turnsens:
        own["turnud"] = 1
    else:
        own["turnud"] = 0        
#light  
#if manual and grindhit = true  
    if lLR > turnsens and lLR < (turnsens * 1.3) and (grindHit == False or (manual == 1 and grindHit == True)):       
        rotation = [ 0.0, 0.0, (-rotamt)]        
        local = False # use world axis
        own.applyRotation( rotation, local)
    
        if r_ground.triggered == True:
            #print("light turn")
            if STANCE == 0:   
                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
            if STANCE == 1:   
                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1)           
    if lLR < -turnsens and lLR > (turnsens * -1.3) and (grindHit == False or (manual == 1 and grindHit == True)):       
        rotation = [ 0.0, 0.0, rotamt]        
        local = False # use world axis
        own.applyRotation( rotation, local) 
        
        if r_ground.triggered == True:
            #print("light turn")
            if STANCE == 0:   
                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
            if STANCE == 1:   
                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1)        
#medium
    if lLR > (turnsens * 1.3) and (grindHit == False or (manual == 1 and grindHit == True)):
        #turn left
        if rot.z < .4:
            rotation = [ 0.0, 0.0, (-rotamt * 5)] 
        if rot.z < .6 and rot.z > .4:    
            rotation = [ 0.0, 0.0, (-rotamt * 2)]        
        else:
            rotation = [ 0.0, 0.0, (-rotamt * 1.6)]        
        local = True # use world axis
        own.applyRotation( rotation, local)
        if r_ground.triggered == True:
            #print("med turn")
            if STANCE == 0:   
                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
            if STANCE == 1:   
                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1)  
    if lLR < (-turnsens * 1.3) and (grindHit == False or (manual == 1 and grindHit == True)):
        #turn right
        if rot.z < .4:
            rotation = [ 0.0, 0.0, (rotamt * 5)]
        if rot.z < .6 and rot.z > .4:    
            rotation = [ 0.0, 0.0, (rotamt * 2)]             
        else:            
            rotation = [ 0.0, 0.0, (rotamt * 1.6)]        
        local = True # use world axis
        own.applyRotation( rotation, local) 
        if r_ground.triggered == True:
            #print("med turn")
            if STANCE == 0:   
                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
            if STANCE == 1:   
                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1)        
    #if lLR > (turnsens * 1.3 and grindHit == False):
        #skater.playAction("nreg_right", 1,20, layer=23, priority=8, blendin=10, play_mode=0, speed=.5)     
#air
    if r_ground.triggered == False and lLR > turnsens and (grindHit == False or (manual == 1 and grindHit == True)) and own["wallride"] == None:
        rotamt = .07
        if STANCE == 0:
            own.applyRotation([0,0,-rotamt], 1)
        if STANCE == 1:
            own.applyRotation([0,0,-rotamt], 1) 
    if r_ground.triggered == False and lLR < -turnsens and (grindHit == False or (manual == 1 and grindHit == True)) and own["wallride"] == None:
        rotamt = .07
        if STANCE == 0:
            own.applyRotation([0,0,rotamt], 1)
        if STANCE == 1:
            own.applyRotation([0,0,rotamt], 1)                      
##### rewrite attempt     
#    rotamt = .03
#    linVelocity2 = own.getLinearVelocity(True)
#    speed = .002
#    turninc = .007 #.0025
#    turnmult = .99
#    turnmax = .043 #.043
#    rlLR = 0
#    rlLR = round(lLR, 2)
#    rlLR2 = rlLR 
#    rlLR = rlLR * 20.5
#    turninc = turninc * abs(rlLR)
#    rlLR2 = rlLR2 * 12.5
#    turnmax = turnmax * abs(rlLR2)
#    if abs(rlLR2) <= .6:
#        turnmax = turnmax *.7
#        turninc = turninc * .7
#    manual = 0
#    if (own['fak_nmanual'] == 1 or own['reg_nmanual'] == 1 or own['fak_manual'] == 1 or own['reg_manual'] == 1): 
#        manual = 1       
#        if abs(linVelocity.x) < 2:
#            speed = .005
#    jumpstance = own['jump_stance']
#    if lLR > turnsens or lLR < -turnsens:
#        own["turn"] = 1
#    else:
#        own["turn"] = 0
#    if lUD > turnsens or lUD < -turnsens:
#        own["turnud"] = 1
#    else:
#        own["turnud"] = 0 
#    newz = rot.z *2    
#    newz = (abs(newz) -2) +1  
#    newz = abs(newz)
#    newz = newz - 1
#    newz = abs(newz) +1
#    newz = round(newz,4)
#    if newz > 2: newz == 2  
#    turninc = (turninc * newz) * newz
#    turnmax = turnmax * newz          
#    if lLR > -turnsens and lLR < 0:
#        own["leftturn"] = 0
#        own['leftturnamt'] = turninc
#    if lLR < -turnsens and (grindHit == False or (manual == 1 and grindHit == True)):
#        turn = own["leftturn"]
#        leftturnamt = own['leftturnamt']
#        if turn < turnmax:
#            turn = turn + leftturnamt
#        leftturnamt = leftturnamt * turnmult   
#        rotation = [ 0.0, 0.0, (turn)]        
#        local = False # use world axis
#        own.applyRotation( rotation, local)
#        own["leftturn"] = turn 
#        own['leftturnamt'] = leftturnamt
#        if r_ground.triggered == True and abs(linVelocity2.x) < 5:
#            if STANCE == 0:   
#                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
#            if STANCE == 1:   
#                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1) 
#    #right            
#    if lLR < turnsens and lLR > 0:
#        own["rightturn"] = 0
#        own['rightturnamt'] = turninc
#    if lLR > turnsens and (grindHit == False or (manual == 1 and grindHit == True)):
#        turn = own["rightturn"]
#        rightturnamt = own['rightturnamt']
#        if turn < turnmax:
#            turn = turn + rightturnamt
#        rightturnamt = rightturnamt * turnmult 
#        rotation = [ 0.0, 0.0, (-turn)]        
#        local = False # use world axis
#        own.applyRotation( rotation, local)
#        own["rightturn"] = turn 
#        own['rightturnamt'] = rightturnamt         
#        if r_ground.triggered == True and abs(linVelocity2.x) < 5:
#            if STANCE == 0:   
#                own.setLinearVelocity([linVelocity2.x - speed, linVelocity2.y, linVelocity2.z], 1)
#            if STANCE == 1:   
#                own.setLinearVelocity([linVelocity2.x + speed, linVelocity2.y, linVelocity2.z], 1)            #air
#    if r_ground.triggered == False and lLR > turnsens and (grindHit == False or (manual == 1 and grindHit == True)):
#        rotamt = .07
#        if STANCE == 0:
#            own.applyRotation([0,0,-rotamt], 1)
#        if STANCE == 1:
#            own.applyRotation([0,0,-rotamt], 1) 
#    if r_ground.triggered == False and lLR < -turnsens and (grindHit == False or (manual == 1 and grindHit == True)):
#        rotamt = .07
#        if STANCE == 0:
#            own.applyRotation([0,0,rotamt], 1)
#        if STANCE == 1:
#            own.applyRotation([0,0,rotamt], 1)                      
###########
def grindsound():
    dropin = own['dropinTimer']
    lif = own['last_invert_frame'] 
    #if frame - lif < 3 and invert_on == 0:
    if grindSound != None and grindHit == True and own['nogrindsound'] == 0:    
    #if grindHit == True and dropin == 0 and own['invert_on'] == 0 and own["LAST_GRIND"] == True and own["nogrindsound"] == 0 and (frame - lif > 13):
        if abs(linVelocity.x) > abs(linVelocity.y):
            vel = linVelocity.x
        elif abs(linVelocity.x) < abs(linVelocity.y):
            vel = linVelocity.y    
        else:
            vel = 0    
        if grindSound == "rail":
            cont.deactivate(own.actuators['grind_cement'])
            num1 = .000
            num2 = .05
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .0001
                own.actuators["grind_rail"].pitch = .6
            num1 = .05
            num2 = .25
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .05
                own.actuators["grind_rail"].pitch = .7 
            
            num1 = .25
            num2 = .5
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .1
                own.actuators["grind_rail"].pitch = .75 
            num1 = .5
            num2 = .75
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .14
                own.actuators["grind_rail"].pitch = .8 
            num1 = .75
            num2 = 1
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .17
                own.actuators["grind_rail"].pitch = .85 
            num1 = 1
            num2 = 1.25
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .18
                own.actuators["grind_rail"].pitch = .9      
            num1 = 1.25
            num2 = 2
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .19
                own.actuators["grind_rail"].pitch = .95                                            
            num1 = 2
            num2 = 40
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_rail"].volume = .19
                own.actuators["grind_rail"].pitch = 1 
                
                    
            cont.activate(own.actuators['grind_rail'])           
        if grindSound == "concrete":
        #play sound
            cont.deactivate(own.actuators['grind_rail'])
            num1 = .000
            num2 = .05
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .01
                own.actuators["grind_cement"].pitch = .6
            num1 = .05
            num2 = .25
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .05
                own.actuators["grind_cement"].pitch = .7 
            
            num1 = .25
            num2 = .5
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .1
                own.actuators["grind_cement"].pitch = .75 
            num1 = .5
            num2 = .75
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .14
                own.actuators["grind_cement"].pitch = .8 
            num1 = .75
            num2 = 1
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .17
                own.actuators["grind_cement"].pitch = .85 
            num1 = 1
            num2 = 1.25
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .18
                own.actuators["grind_cement"].pitch = .9      
            num1 = 1.25
            num2 = 2
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .19
                own.actuators["grind_cement"].pitch = .95                                            
            num1 = 2
            num2 = 40
            if (vel > num1 and vel < num2) or (vel < -num1 and vel > -num2):   
                own.actuators["grind_cement"].volume = .19
                own.actuators["grind_cement"].pitch = 1 
            cont.activate(own.actuators['grind_cement'])
    else:
        cont.deactivate(own.actuators['grind_cement'])    
        cont.deactivate(own.actuators['grind_rail'])    
def record_grindsound():
    dropin = own['dropinTimer']
    lif = own['last_invert_frame']     
    if grindHit == True and dropin == 0 and own['invert_on'] == 0 and own["LAST_GRIND"] == True and own["nogrindsound"] == 0 and (frame - lif > 13):
        if grindSound == "concrete":
            act = own.actuators["grind_cement"]
            own['grindcement_vol'] = act.volume
            own['grindcement_pitch'] = act.pitch 
        elif grindSound == "rail":       
            act = own.actuators["grind_rail"]
            own['grindrail_vol'] = act.volume
            own['grindrail_pitch'] = act.pitch
    if own["LAST_GRIND"] == False:    
        own['grindcement_vol'] = 0
        own['grindcement_pitch'] = 0
        own['grindrail_vol'] = 0
        own['grindrail_pitch'] = 0    
    
def grind():
    grindsound()
    STANCE = own["stance"]
    jumpstance = own["jump_stance"]
    lif = frame - own['last_invert_frame']
    if grindHit == True and own['invert_on'] == 0 and own['footplant_on'] == False and own['manual'] == 0 and lif > 40 and own['dropinTimer'] < 30:  
        #skater.stopAction(0)
        #deck.stopAction(0)
        #trucks.stopAction(0)
        gblend = 1    
        #add grindstance?
        #printplaying()
        if LAST_GRIND == 0:
            gt = own['grindType']
            #print(gt)
            #grind in
        tempstance = 3
        #print("jumpstance: ", jumpstance, "stance: ", STANCE)
        if jumpstance != 3:
            tempstance = jumpstance
        else:
            tempstance = STANCE  
        #print("tempstance: ", tempstance) 
        grindpos = own['grindpos']
        if grindpos == "reg_5050" and own['grindType'] == "empty":
            own['grindType'] = grindpos
        if own['grindType'] == "empty" and grindpos == 'reg_board':
            if jumpstance == 1:
                own['grindType'] = "fak_bsboard"
                own["stance"] = True
                STANCE = True
            elif jumpstance == 0:    
                own['grindType'] = "reg_bsboard"
                own["stance"] = False
                STANCE = False
            elif jumpstance == 3:
                if STANCE == True:
                    own['grindType'] = "fak_bsboard"
                else:
                    own['grindType'] = "reg_bsboard"        
        #if STANCE == True and LAST_GRIND == False:
        if STANCE == True:    
            #print("jumpstance =1")
            if own['grindType'] == "reg_bsboard":
                own['grind_stance'] = 0
                own['requestAction'] = 'reg_bsboard'
                #skater.playAction("reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)  
                #deck.playAction("a_reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("play fak reg_bsboard")  
            elif own['grindType'] == "fak_bsboard":
                own['grind_stance'] = 1
                own['requestAction'] = 'fak_bsboard'
                #skater.playAction("fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)  
                #deck.playAction("a_fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("play fak fak_bsboard") 
            elif own['grindType'] == "reg_fsboard":
                own['grind_stance'] = 0
                own['requestAction'] = 'reg_fsboard'
                #skater.playAction("reg_FS_Board", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_FS_Board", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_FS_Board", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("reg_FS_Board")

            elif own['grindType'] == "reg_tailg":
                own['requestAction'] = 'reg_tailg'
                #skater.playAction("reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
            elif own['grindType'] == "reg_tailgR":
                own['requestAction'] = 'reg_tailgr'
                #skater.playAction("reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                 
            elif own['grindType'] == "reg_tailgL":
                own['requestAction'] = 'reg_tailgl'
                #skater.playAction("reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                     
            elif own['grindType'] == "reg_noseg":
                own['requestAction'] = 'reg_noseg'                
#                skater.playAction("reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
#                deck.playAction("a_reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
#                trucks.playAction("a_reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "reg_nosegR":
                #print("playing reg_nosegR")
                own['requestAction'] = 'reg_nosegr'                
                #skater.playAction("reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
            elif own['grindType'] == "reg_nosegL":
                #print("playing reg_nosegL")
                own['requestAction'] = 'reg_nosegl'                
                #skater.playAction("reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                                
            elif own['grindType'] == "fak_noseg":
                own['requestAction'] = 'fak_noseg'                
                #skater.playAction("fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_nosegR": 
                own['requestAction'] = 'fak_nosegr'               
                #skater.playAction("fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_nosegL":
                own['requestAction'] = 'reg_nosegl'                
                #skater.playAction("fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                                
                #print("fak_noseg")
            elif own['grindType'] == "fak_tailg":
                own['requestAction'] = 'fak_tailg' 
                #skater.playAction("fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_tailgR": 
                own['requestAction'] = 'fak_tailgr'
                #skater.playAction("fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_tailgL":
                own['requestAction'] = 'fak_tailgl' 
                #skater.playAction("fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)        
            
            elif own['grindType'] == "reg_tailslide":
                own['requestAction'] = 'reg_tailslide'
                own['grind_stance'] = 0                
                #skater.playAction("fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE                                  
            elif own['grindType'] == "fak_tailslide":
                own['requestAction'] = 'fak_tailslide'
                own['grind_stance'] = 1
                #skater.playAction("reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE 
            elif own['grindType'] == "reg_noseslide":
                own['requestAction'] = 'reg_noseslide'
                own['grind_stance'] = 0
                #skater.playAction("fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE  
            elif own['grindType'] == "fak_noseslide":
                own['requestAction'] = 'fak_noseslide'  
                own['grind_stance'] = 1              
                #skater.playAction("reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE                                                             
            elif own['grindType'] == "nose_stall":
                own['requestAction'] = 'nose_stall'
                skater.playAction("fak_nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)            
                deck.playAction("a_fak_nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                trucks.playAction("a_fak_nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)  
                #print("fak_nose_stall")
            elif own['grindType'] == "tail_stall":
                own['requestAction'] = 'tail_stall'
                skater.playAction("fak_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)            
                deck.playAction("a_fak_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                trucks.playAction("a_fak_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
                #print("fak_tail_stall")                   
            else:
                if STANCE == 0:
                    own['requestAction'] = 'reg_5050'
                    #skater.playAction("reg_5050", 1,30, layer=700, blendin=gblend, priority=8, layer_weight=0, play_mode=1, speed=.5) 
                    #deck.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
                    #trucks.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
                if STANCE == 1:
                    own['requestAction'] = 'fak_5050'
                    #skater.playAction("fak_5050", 1,30, layer=700, blendin=gblend, priority=8, layer_weight=0, play_mode=1, speed=.5) 
                    #deck.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
                    #trucks.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)                        
                #print("fak_5050")
            
        #elif STANCE == False and LAST_GRIND == False:
        elif STANCE == False:
            #print("jumpstance =0")
            if own['grindType'] == "reg_bsboard":
                own['grind_stance'] = 0
                own['requestAction'] = 'reg_bsboard'
                #skater.playAction("reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)    
                #deck.playAction("a_reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("play reg reg_bsboard")
            elif own['grindType'] == "fak_bsboard":
                own['grind_stance'] = 1
                own['requestAction'] = 'fak_bsboard'
                #skater.playAction("fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)  
                #deck.playAction("a_fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_BS_Board2", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("play reg fak_bsboard")     
            elif own['grindType'] == "reg_tailg":
                own['grind_stance'] = 0
                own['requestAction'] = 'reg_tailg'
                #skater.playAction("reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                # if STANCE == True and LAST_GRIND == 0: STANCE = False
                # elif STANCE == False and LAST_GRIND == 0: STANCE = True
                # own['stance'] = STANCE    
            elif own['grindType'] == "reg_tailgR":
                own['requestAction'] = 'reg_tailgr'
                #skater.playAction("reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                 
            elif own['grindType'] == "reg_tailgL":
                own['requestAction'] = 'reg_tailgl'
                #skater.playAction("reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                            
            elif own['grindType'] == "reg_noseg":
                own['requestAction'] = 'reg_noseg'
#                skater.playAction("reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
#                deck.playAction("a_reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
#                trucks.playAction("a_reg_noseg.001", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("0 reg_noseg")
            elif own['grindType'] == "reg_nosegR":
                #print("playing reg_nosegR")   
                own['requestAction'] = 'reg_nosegr'             
                #skater.playAction("reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "reg_nosegL":
                #print("playing reg_nosegL")   
                own['requestAction'] = 'reg_nosegl'             
                #skater.playAction("reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                                
            elif own['grindType'] == "fak_noseg":
                own['requestAction'] = 'fak_noseg'
                #skater.playAction("fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_noseg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)        
                #print("0 fak_noseg")
            elif own['grindType'] == "fak_nosegR": 
                own['requestAction'] = 'fak_nosegr'               
                #skater.playAction("fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_nosegR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_nosegL":
                own['requestAction'] = 'fak_nosegl'                
                #skater.playAction("fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_nosegL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                
            elif own['grindType'] == "fak_tailg":
                own['requestAction'] = 'fak_tailg'
                own['requestAction'] = 'fak_tailg'
                own['grind_stance'] = 1
                #skater.playAction("fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailg", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_tailgR": 
                own['requestAction'] = 'fak_tailgr'
                #skater.playAction("fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailgR", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
            elif own['grindType'] == "fak_tailgL":
                own['requestAction'] = 'fak_tailgl' 
                #skater.playAction("fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tailgL", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)                       
            elif own['grindType'] == "reg_tailslide":
                own['grind_stance'] = 0           
                own['requestAction'] = 'reg_tailslide'     
                #skater.playAction("fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE                                  
            elif own['grindType'] == "fak_tailslide":
                own['grind_stance'] = 1
                own['requestAction'] = 'fak_tailslide'
                #skater.playAction("reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_noses", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE 
            elif own['grindType'] == "reg_noseslide":
                own['grind_stance'] = 0
                own['requestAction'] = 'reg_noseslide'
                #skater.playAction("fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_fak_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE  
            elif own['grindType'] == "fak_noseslide":  
                own['grind_stance'] = 1              
                own['requestAction'] = 'fak_noseslide'
                #skater.playAction("reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #deck.playAction("a_reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #trucks.playAction("a_reg_tails", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
                #if STANCE == True and LAST_GRIND == 0: STANCE = False
                #elif STANCE == False and LAST_GRIND == 0: STANCE = True
                #own['stance'] = STANCE
                 
                #if STANCE == True: STANCE = False
                #if STANCE == False: STANCE = True
                #print("change stance")
                #STANCE = own["stance"]                 
            elif own['grindType'] == "nose_stall":
                skater.playAction("nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
                deck.playAction("a_nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                trucks.playAction("a_nose_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5) 
                #print("nose_stall") 
            elif own['grindType'] == "tail_stall":
                skater.playAction("reg_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                deck.playAction("a_reg_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                trucks.playAction("a_reg_tail_stall", 1,30, layer=700, blendin=gblend, play_mode=1, speed=.5)
                #print("reg_tail_stall")                                 
            else:
#                print("@playing last resort")                          
                if STANCE == 0:
                    own['requestAction'] = 'reg_5050'
#                    skater.playAction("reg_5050", 1,30, layer=700, blendin=gblend, priority=8, layer_weight=0, play_mode=1, speed=.5) 
#                    deck.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
#                    trucks.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
                if STANCE == 1:
                    own['requestAction'] = 'fak_5050'
#                    skater.playAction("fak_5050", 1,30, layer=700, blendin=gblend, priority=8, layer_weight=0, play_mode=1, speed=.5) 
#                    deck.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)
#                    trucks.playAction("a_reg", 1,40, layer=700, blendin=gblend, priority=9, layer_weight=0, play_mode=1, speed=.5)   
            
    else:
        if own['grindCountdown'] < 16:
            grindtype("empty")
            killact(700)  
            killact(705)
            killact(706)
            killact(707)
            killact(708)
#    if LAST_GRIND ==1 and grindHit ==0:
#        #print("++++out", own['grindType'])
#        if own['grindType'] == "reg_tailslide":
#            own['grind_stance'] = 0                
#            #skater.playAction("fak_noses", 30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_fak_noses", 30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_fak_noses", 30,40, layer=200, play_mode=1, speed=.5)

####
#        elif own['grindType'] == "fak_tailslide":
#            own['grind_stance'] = 1
#            #skater.playAction("reg_noses", 30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_reg_noses", 30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_reg_noses", 30,40, layer=200, play_mode=1, speed=.5)
#####


#        elif own['grindType'] == "reg_noseslide":
#            own['grind_stance'] = 0
#            #skater.playAction("fak_tails", 30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_fak_tails", 30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_fak_tails", 30,40, layer=200, play_mode=1, speed=.5)                
#        elif own['grindType'] == "fak_noseslide":  
#            own['grind_stance'] = 1              
#            #skater.playAction("reg_tails", 30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_reg_tails", 30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_reg_tails", 30,40, layer=200, play_mode=1, speed=.5)  
####******
#        elif own['grindType'] == "reg_tailg":
#            #skater.playAction("reg_tailg.001",30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_reg_tailg.001",30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_reg_tailg.001",30,40, layer=200, play_mode=1, speed=.5) 
#        elif own['grindType'] == "reg_tailgR":
#            skater.playAction("reg_tailgR",30,40, layer=200, play_mode=1, speed=.5)
#            #deck.playAction("a_reg_tailgR",30,40, layer=200, play_mode=1, speed=.5)
#            #trucks.playAction("a_reg_tailgR",30,40, layer=200, play_mode=1, speed=.5) 
#        elif own['grindType'] == "reg_tailgL":
#            skater.playAction("reg_tailgL",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_reg_tailgL",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_reg_tailgL",30,40, layer=200, play_mode=1, speed=.5) 

#        elif own['grindType'] == "reg_noseg":                
#            skater.playAction("reg_noseg.001",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_reg_noseg.001",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_reg_noseg.001",30,40, layer=200, play_mode=1, speed=.5)
#        elif own['grindType'] == "reg_nosegR":                
#            skater.playAction("reg_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_reg_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_reg_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#        elif own['grindType'] == "reg_nosegL":                
#            skater.playAction("reg_nosegL",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_reg_nosegL",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_reg_nosegL",30,40, layer=200, play_mode=1, speed=.5)                        
#        elif own['grindType'] == "fak_noseg":                
#            skater.playAction("fak_noseg",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_noseg",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_noseg",30,40, layer=200, play_mode=1, speed=.5)
#            #print("fak_noseg")
#        elif own['grindType'] == "fak_nosegR":                
#            skater.playAction("fak_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_nosegR",30,40, layer=200, play_mode=1, speed=.5)
#        elif own['grindType'] == "fak_nosegL":                
#            skater.playAction("fak_nosegL",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_nosegL",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_nosegL",30,40, layer=200, play_mode=1, speed=.5)                        
#        elif own['grindType'] == "fak_tailg": 
#            skater.playAction("fak_tailg",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_tailg",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_tailg",30,40, layer=200, play_mode=1, speed=.5)
#        elif own['grindType'] == "fak_tailgR": 
#            skater.playAction("fak_tailgR",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_tailgR",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_tailgR",30,40, layer=200, play_mode=1, speed=.5)
#        elif own['grindType'] == "fak_tailgL": 
#            skater.playAction("fak_tailgL",30,40, layer=200, play_mode=1, speed=.5)
#            deck.playAction("a_fak_tailgL",30,40, layer=200, play_mode=1, speed=.5)
#            trucks.playAction("a_fak_tailgL",30,40, layer=200, play_mode=1, speed=.5)         
                            
                         
                  
def rotmult():
    if r_ground.triggered:
        #print(linVelocity)
        num = ((rot.z * -1) +1)
        num = num * 100
        #print(num)

def airup():
    if r_ground.triggered == False:
        pos = own.worldPosition
        pos = own.worldPosition.z
        last_pos = own['last_posz']
        #print(last_pos - pos)
        if last_pos - pos > 0:
            own['airup'] = 0
        if last_pos - pos < 0:    
            own['airup'] = 1
        if pos > own['last_posz']:
            own["air_height"] = pos  
        own['last_posz'] = pos
        
def onramp():
    if r_ground.positive:
        if 'ramp' in r_ground.hitObject:
            own['onramp'] = 1
        else:
            own['onramp'] = 0   
    else:
        own['onramp'] = 0        
#    if r_ground.positive:
#        own['rgroundhit'] = 1        
#    else:
#        own['rgroundhit'] = 0
def grindtype(gtype):
    own['grindType'] = gtype
    
def transmult():
#    linvel = own.getLinearVelocity(True)
    lastrotz = own["rotz"]
#    lastlinvelx = own["linvelx"]
##up
#    #reg
#    if rot.z < lastrotz and linvel.x > lastlinvelx and rot.z < .9 and rot.z > .3 and linvel.x > 0:
#        force = [ 40, 0, 0]
#        own.applyForce(force, 1) # apply force 
#    #fak
#    if rot.z < lastrotz and linvel.x > lastlinvelx and rot.z < .9 and rot.z > .3 and linvel.x < 0:
#        force = [ -40, 0, 0]
#        own.applyForce(force, 1) # apply force 
##down            
#    #reg
#    if rot.z > lastrotz and linvel.x > lastlinvelx and rot.z < .9 and rot.z > .3 and linvel.x > 0:
#        force = [ 40, 0, 0]
#        own.applyForce(force, 1) # apply force 
#    #fak
#    if rot.z > lastrotz and linvel.x > lastlinvelx and rot.z < .9 and rot.z > .3 and linvel.x < 0:
#        force = [ -40, 0, 0]
#        own.applyForce(force, 1) # apply force     
    linvel = own.getLinearVelocity(True)
    newx = (linvel.x + (linvel.x * .039))
    if linvel.x < 7 and linvel.x > -7 and rot.z > lastrotz and r_ground.triggered == 1 and rot.z > .3 and rot.z < .93:
        own.setLinearVelocity([newx, linvel.y, linvel.z], True)    
        #print("what the fuck")
        
def speedmult():
    vel = own.getLinearVelocity(True)
    xyz = own.worldOrientation.to_euler()
    roty = math.degrees(xyz[1])     
    roty = abs(roty) 
    roty = roty * .0005
    #print("Roty: ", roty)
    
    if abs(vel.x) > 1:
        #mult = .0007
        mult = .0015 + roty
    else:
        mult = .000       
    mult2 = .018
    mult3 = .007
    

    
    lastrotz = own["rotz"]
    #print(lastrotz)     
    x = vel.x * mult
    x2 = x + vel.x
    x3 = vel.x * mult2
    x4 = x3 + vel.x
    x5 = vel.x * mult3
    x6 = x5 + vel.x
    if r_ground.triggered and vel.x < 4 and vel.x > -4:
        own.setLinearVelocity([x2, vel.y, vel.z], True)
        #pass
#    if STANCE == True:
#        if lastrotz > .9 and r_ground.triggered == True and vel.x > .05 and vel.x < 4:
#            own.setLinearVelocity([x6, vel.y, vel.z], True)  
#        if lastrotz < .9 and r_ground.triggered == True:
#            own.setLinearVelocity([x2, vel.y, vel.z], True)   
#        if lastrotz < .85 and lastrotz > .7 and r_ground.triggered == True:          
#            own.setLinearVelocity([x4, vel.y, vel.z], True)   

def coping():
    if invertTouch.positive:
        own["coping"] = 1
    else:
        own["coping"] = 0    


def onboard():
    if own['walk'] == 1:
        cont.deactivate(cam.actuators['replayCam'])
        cont.activate(cam.actuators['Camera'])
        killall()
        #set_vibration(0, 0.0, 0.0) 
        walklay = 40
        fliplay3 = 2060  
        ob_speed = .5
        #add dropin anim
             
        if STANCE == 0:
            skater.stopAction(fliplay)
            deck.stopAction(fliplay)
            trucks.stopAction(fliplay)
            killall() 
            if own['dropinCol'] == True:
                print("dropinanim")
                own['requestAction'] = reg_dropin
                #skater.playAction("nreg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                #deck.playAction("a_reg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                #trucks.playAction("a_reg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
            else:
                own['requestAction'] = 'reg_onboard'    
                #skater.playAction("reg_noffboard", 9,0, layer=40, priority=0, play_mode=0, speed=ob_speed)
                #deck.playAction("a_reg_noffboard", 9,0, layer=40, priority=0, play_mode=0, speed=ob_speed)
                #trucks.playAction("a_reg_noffboard", 9,0, layer=40, priority=0, play_mode=0, speed=ob_speed)
            force = (linVelocity.x -1, linVelocity.y, linVelocity.z)
            own.setLinearVelocity(force, True)
            own['dropinTimer'] = 60
            #print("get on board")
        if STANCE == 1:
            skater.stopAction(fliplay)
            deck.stopAction(fliplay)
            trucks.stopAction(fliplay)
            killall() 
            if own['dropinTimer'] > 30:
                print("dropinanim2")
                own['requestAction'] = fak_dropin
                #skater.playAction("nfak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                #deck.playAction("a_fak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                #trucks.playAction("a_fak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=.75)
            else: 
                own['requestAction'] = 'fak_onboard'
                #skater.playAction("nfak_offboard", 30,1, layer=40, priority=0, play_mode=0, speed=1.5)
                #deck.playAction("a_fak_offboard", 30,1, layer=40, priority=0, play_mode=0, speed=1.5)
                #trucks.playAction("a_fak_offboard", 30,1, layer=40, priority=0, play_mode=0, speed=1.5)
            force = (linVelocity.x +1, linVelocity.y, linVelocity.z)
            own.setLinearVelocity(force, True)
            own['dropinTimer'] = 60
            #print("get on board")            
    else:
        num = own['dropinTimer']
        if num > 0:
            num = num - 1
        own['dropinTimer'] = num            
    #if own['dropinTimer'] == 1:
        #killact(6011) 
        #killact(6000)    
        #killact(6001)   
        #killact(2)  
        
def offboard():
        wheel1.stopAction(2)
        wheel2.stopAction(2)
        wheel3.stopAction(2)
        wheel4.stopAction(2)    
        cont.deactivate(own.actuators["sroll"])
        sact = own.actuators["sroll"]
        sact.volume = .0001   
        own.actuators["sroll"].stopSound()
        own['offboard_vel'] = own.linearVelocity
        own['walk_timer'] = 0               
    
def resetjumpstance():
    if LAST_GRIND == True and grindHit == False:
        own["lF_ground_frame"] = own['framenum']
        lfg = own["lF_ground_frame"]
        #print(lfg, "----- this?")  
        if own['jump_stance'] != 3:
            own['jump_stance'] = 3
    # if r_ground.positive and grindDar == 0:
    #     lfg = own["lF_ground_frame"]
    #     fn = own["framenum"]
    #     time = fn - lfg
    #     #pass
    #     print(LAST_GRIND)
    #     if time > 60:
    #         own["jump_stance"] = 3
    #     #print("resetting jumpstance")
    
def grass():
    try:
        if 'grass' in r_ground.hitObject:
            #print("grass")
            linVel = own.getLinearVelocity(True)
            linvelx = linVel.x * .98
            own.setLinearVelocity((linvelx, linVel.y, linVel.z), 1)
    except:
        pass    
def grindoutair():
#    if own['grind_jump'] == True: 
#        if own['grindjumpturn'] != True:
#           own['grindjumpturn'] = True 
    skippy = 0
    linVel = own.getLinearVelocity(True)
    if own['LAST_GRIND'] == True and grindHit == True:
        own['lg_stance'] = STANCE
    #else:
        #own['lg_stance'] = 0
    lg_stance = own['lg_stance']
    own.actuators["grindoutair"].useLocalLinV = True        
    if own['grindjumpturn'] == True and own['grindCountdown'] > 12 and skippy == 0:           
        grindoutspeed = .1  
        grindoutspeed2 = 5.4  
        if lLR > turnsens:
            #followcam.actuators["up"].dLoc = [ 0, 0, -camspeed2]
            if own['last_grindpos'] == 'reg_5050':
                if STANCE == 0:
                    own.actuators["grindoutair"].linV = [0, grindoutspeed, 0]                    
                else:
                    own.actuators["grindoutair"].linV = [0, -grindoutspeed, 0] 
                cont.activate(own.actuators["grindoutair"]) 
                #print("50grindoutair")   

        if lLR < -turnsens:
            if own['last_grindpos'] == 'reg_5050':
                if STANCE == 0:
                    own.actuators["grindoutair"].linV = [0, -grindoutspeed, 0]
                else: 
                    own.actuators["grindoutair"].linV = [0, grindoutspeed, 0] 
                cont.activate(own.actuators["grindoutair"])
                #print("50grindoutair")
        if lUD > turnsens:
            js = own['lg_stance']
            linvelx = own.getLinearVelocity(True)                
            if own['last_grindpos'] == 'reg_board':
                if js == 1:
                   own.actuators["grindoutair"].linV = [-grindoutspeed, 0, 0]
                   cont.activate(own.actuators["grindoutair"])
                   #print("1grindoutair*", round(linvelx.x, 2), js)
                else:
                    own.actuators["grindoutair"].linV = [grindoutspeed, 0, 0] 
                    cont.activate(own.actuators["grindoutair"]) 
                    #print("2grindoutair*", round(linvelx.x, 2), js)   
                #cont.activate(own.actuators["grindoutair"])                
        if lUD < -turnsens:  
            js = own['lg_stance']      
            if own['last_grindpos'] == 'reg_board':    
                if js == 0:
                    own.actuators["grindoutair"].linV = [-grindoutspeed, 0, 0]
                    cont.activate(own.actuators["grindoutair"])
                    #print("3grindoutair broke", js)
                else:
                    own.actuators["grindoutair"].linV = [grindoutspeed, 0, 0]
                    cont.activate(own.actuators["grindoutair"])
                    #print("equal")
                    #print("4grindoutair broke", js)  
                
    if LAST_GRIND == False and r_ground.triggered and own['grindjumpturn'] == True and own['grindCountdown'] < 1:
        own['grindjumpturn'] = False
        #pass
    if r_ground.triggered:
        own['grind_jump'] = False 
        #own['grindjumpturn'] = False   
        #pass
    
    if own['grindjumpturn'] == False or own['grindCountdown'] < 19:
        #pass
        cont.deactivate(own.actuators["grindoutair"])
        #print("deactivate#################################")
#    if own['grindjumpturn'] == True and r_ground.triggered:
#        own['grindjumpturn'] = False
                      

def set_last_grindpos():
    if own['grindpos'] != None:
        own['last_grindpos'] = own['grindpos']
def air_pos():
    grindpos = own['grindpos']
    GRAB_ON = own["GRAB_ON"]
    wr = own["wallride"]
    if rUD > .040 and r_ground.triggered == False and GRAB_ON == False and wr == None and jump_timer < 50:
        killact(2)
        killact(4)
#        if trucks.isPlayingAction(500) == False:
#            if STANCE == 0:
        if STANCE == 0:
            own['requestAction'] = 'reg_air_tail'    
#                skater.playAction("reg_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
#                deck.playAction("a_reg_manual", 10,70, layer=50, priority=8,  play_mode=1, speed=.5)
#                trucks.playAction("a_reg_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
        else:
            own['requestAction'] = 'fak_air_tail' 
#                skater.playAction("fak_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
#                deck.playAction("a_fak_manual", 10,70, layer=50, priority=8,  play_mode=1, speed=.5)
#                trucks.playAction("a_fak_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
    elif rUD < -.040 and r_ground.triggered == False and GRAB_ON == False and wr == None and jump_timer < 50:
        killact(2)
        killact(4)
#        if trucks.isPlayingAction(500) == False:
        if STANCE == 0:
            own['requestAction'] = 'reg_air_nose' 
#                skater.playAction("reg_nmanual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
#                deck.playAction("a_fak_manual", 10,70, layer=50, priority=8,  play_mode=1, speed=.5)
#                trucks.playAction("a_fak_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
        else:
            own['requestAction'] = 'fak_air_nose' 
#                skater.playAction("fak_nmanual", 10,70, layer=50, priority=8, play_mode=1, speed=.5) 
#                deck.playAction("a_reg_manual", 10,70, layer=50, priority=8,  play_mode=1, speed=.5)
#                trucks.playAction("a_reg_manual", 10,70, layer=50, priority=8, play_mode=1, speed=.5)                                     
    else:
        killact(50)
        #killact(50)
        #killact(50)

def air_turn_boost():
    pass

def revert():
    own["Q3oncdl"] = 0
    own["Q4oncdl"] = 0
    own["Q5oncdl"] = 0
    own["Q6oncdl"] = 0
    own["Q7oncdl"] = 0
    local = True
    rot = [ 0.0, 0.0, 3.14]
    own.applyRotation(rot,local)
    #killall()
    #if own['reg_manual'] == 1 or own['reg_nmanual'] == 1:
    #if own['reg_manual'] == 1:
    if own['manual_v2_type'] == 'reg manual': 
        own['requestAction'] = 'reg_manual_revert_ccw'   
#        skater.playAction("reg_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
#        deck.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
#        trucks.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg")
    #elif own['reg_nmanual'] == 1:
    elif own['manual_v2_type'] == 'reg nose manual':    
        skater.playAction("fak_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg nose manual revert")             
    #elif own['fak_manual'] == 1 or own['fak_nmanual'] == 1:
    elif own['manual_v2_type'] == 'fak manual':    
        skater.playAction("fak_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak manual revert")
    elif own['manual_v2_type'] == 'fak nose manual':    
        skater.playAction("reg_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak")           
    else:
        own['requestAction'] = 'revert1'            
#        skater.playAction("revert1", 1,10, layer=400, priority=8, play_mode=0, speed=.5)
#        deck.playAction("a_revert1", 1,10, layer=400, priority=1, play_mode=0, speed=.5)
#        trucks.playAction("a_revert1", 1,10, layer=400, priority=0, play_mode=0, speed=.5)
    own['revert_timer'] = 20 
    cont.activate(own.actuators["revertSound"])      
    #revert_on_timer 20
    #force = [0,0,0]
    #own.setLinearVelocity(force, True)    
def revert2():
    own["Q3oncdl"] = 0
    own["Q4oncdl"] = 0
    own["Q5oncdl"] = 0
    own["Q6oncdl"] = 0
    own["Q7oncdl"] = 0 
    local = True
    rot = [ 0.0, 0.0, -3.14]
    own.applyRotation(rot,local)
    #killall()
    if own['manual_v2_type'] == 'reg manual':    
        skater.playAction("reg_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg")
    #elif own['reg_nmanual'] == 1:
    elif own['manual_v2_type'] == 'reg nose manual':    
        skater.playAction("fak_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg nose manual revert")             
    #elif own['fak_manual'] == 1 or own['fak_nmanual'] == 1:
    elif own['manual_v2_type'] == 'fak manual':    
        skater.playAction("fak_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak manual revert")
    elif own['manual_v2_type'] == 'fak nose manual':    
        skater.playAction("reg_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak")   
    else:     
        own['requestAction'] = 'revert2'       
#        skater.playAction("revert2", 1,10, layer=400, priority=8, play_mode=0, speed=.5)
#        deck.playAction("a_revert2", 1,10, layer=400, priority=1, play_mode=0, speed=.5)
#        trucks.playAction("a_revert2", 1,10, layer=400, priority=0, play_mode=0, speed=.5)
    own['revert_timer'] = 20 
    cont.activate(own.actuators["revertSound"])         
def revert3():
    own["Q7oncdl"] = 0
    own["Q8oncdl"] = 0
    own["Q1oncdl"] = 0
    own["Q2oncdl"] = 0
    own["Q3oncdl"] = 0
    local = True
    rot = [ 0.0, 0.0, 3.14]
    own.applyRotation(rot,local) 
    print("real revert 3")  
    #killall()
    if own['manual_v2_type'] == 'reg manual':    
        skater.playAction("reg_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg")
    #elif own['reg_nmanual'] == 1:
    elif own['manual_v2_type'] == 'reg nose manual':    
        skater.playAction("fak_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg nose manual revert")             
    #elif own['fak_manual'] == 1 or own['fak_nmanual'] == 1:
    elif own['manual_v2_type'] == 'fak manual':    
        skater.playAction("fak_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak manual revert")
    elif own['manual_v2_type'] == 'fak nose manual':    
        skater.playAction("reg_manual_revert_ccw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_ccw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak")   
    else:       
        own['requestAction'] = 'revert3' 
#        skater.playAction("revert1", 1,10, layer=400, priority=8, play_mode=0, speed=.5)
#        deck.playAction("a_revert1", 1,10, layer=400, priority=1, play_mode=0, speed=.5)
#        trucks.playAction("a_revert1", 1,10, layer=400, priority=0, play_mode=0, speed=.5)
    own['revert_timer'] = 20 
    cont.activate(own.actuators["revertSound"])      
def revert4():
    own["Q7oncdl"] = 0
    own["Q8oncdl"] = 0
    own["Q1oncdl"] = 0
    own["Q2oncdl"] = 0
    own["Q3oncdl"] = 0
    local = True
    rot = [ 0.0, 0.0, 3.14]
    own.applyRotation(rot,local)  
    #killall()
    if own['manual_v2_type'] == 'reg manual':    
        skater.playAction("reg_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg")
    #elif own['reg_nmanual'] == 1:
    elif own['manual_v2_type'] == 'reg nose manual':    
        skater.playAction("fak_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("reg nose manual revert")             
    #elif own['fak_manual'] == 1 or own['fak_nmanual'] == 1:
    elif own['manual_v2_type'] == 'fak manual':    
        skater.playAction("fak_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_fak_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak manual revert")
    elif own['manual_v2_type'] == 'fak nose manual':    
        skater.playAction("reg_manual_revert_cw", 70,10, layer=400, priority=8, play_mode=0, speed=4)
        deck.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=1, play_mode=0, speed=4)
        trucks.playAction("a_reg_manual_revert_cw", 70,10, layer=400, priority=0, play_mode=0, speed=4)
        print("fak") 
    else:
        own['requestAction'] = 'revert4'
        print("normal revert")        
#        skater.playAction("revert2", 1,10, layer=400, priority=8, play_mode=0, speed=.5)
#        deck.playAction("a_revert2", 1,10, layer=400, priority=1, play_mode=0, speed=.5)
#        trucks.playAction("a_revert2", 1,10, layer=400, priority=0, play_mode=0, speed=.5)
    own['revert_timer'] = 20 
    cont.activate(own.actuators["revertSound"])       

def powerslide():
    own['powerslide_counter'] = own['powerslide_counter'] + 1
    since_walk = own['framenum'] - own['last_walk_frame']
    since_grind = own['framenum'] - own['last_grind_frame']
    if own['powerslide_counter'] > 15 and since_walk > 100 and since_grind > 40:
        own['powerslide_on'] = 1
        if STANCE == 0:
            own['powerslide'] = "reg2"
            #skater.playAction("nreg_powerslide", 20,80, layer=400, priority=8, play_mode=1, speed=.5)
            #deck.playAction("a_reg_powerslide", 20,80, layer=400, priority=1, play_mode=1, speed=.5)
            #trucks.playAction("a_reg_powerslide", 20,80, layer=400, priority=0, play_mode=1, speed=.5)        
        if STANCE == 1:
            own['powerslide'] = "fak1" 
            #skater.playAction("nfak_powerslide", 20,80, layer=400, priority=8, play_mode=1, speed=.5)
            #deck.playAction("a_fak_powerslide_d", 20,80, layer=400, priority=1, play_mode=1, speed=.5)
            #trucks.playAction("a_fak_powerslide_t", 20,80, layer=400, priority=0, play_mode=1, speed=.5)             
        linVelocity4 = own.getLinearVelocity(True)    
        if own['powerslide_counter'] > 15 and own['powerslide_counter'] < 18:         
            newx = linVelocity4.x * .9 
        else:
            newx = linVelocity4.x * .98        
        force = [newx, linVelocity4.y, linVelocity4.z]
        own.setLinearVelocity(force, True)
def powerslide2():
    own['powerslide_counter'] = own['powerslide_counter'] + 1
    since_walk = own['framenum'] - own['last_walk_frame']
    since_grind = own['framenum'] - own['last_grind_frame']
    if own['powerslide_counter'] > 15 and since_walk > 100 and since_grind > 100:
        own['powerslide_on'] = 1
        if STANCE == 0:
            own['powerslide'] = "reg1"
            #skater.playAction("nreg_powerslide2", 20,80, layer=400, priority=8, play_mode=1, speed=.5)
            #deck.playAction("a_reg_powerslide2_d", 20,80, layer=400, priority=1, play_mode=1, speed=.5)
            #trucks.playAction("a_reg_powerslide2_t", 20,80, layer=400, priority=0, play_mode=1, speed=.5)        
        if STANCE == 1:
            own['powerslide'] = "fak2" 
            #skater.playAction("nfak_powerslide2", 20,80, layer=400, priority=8, play_mode=1, speed=.5)
            #deck.playAction("a_fak_powerslide2_d", 20,80, layer=400, priority=1, play_mode=1, speed=.5)
            #trucks.playAction("a_fak_powerslide2_t", 20,80, layer=400, priority=0, play_mode=1, speed=.5)             
        linVelocity4 = own.getLinearVelocity(True)    
        if own['powerslide_counter'] > 15 and own['powerslide_counter'] < 18:         
            newx = linVelocity4.x * .9 
        else:
            newx = linVelocity4.x * .98        
        force = [newx, linVelocity4.y, linVelocity4.z]
        own.setLinearVelocity(force, True)        
def powerslide_state():

####powerslide on#####  
    if own['powerslide_on'] == 1:   
        if own['powerslide'] == "reg2":                               
            own['requestAction'] = 'reg_fs_powerslide'
        if own['powerslide'] == "fak1":                               
            own['requestAction'] = 'fak_fs_powerslide'
        if own['powerslide'] == "reg1":                               
            own['requestAction'] = 'reg_powerslide'
        if own['powerslide'] == "fak2":                               
            own['requestAction'] = 'fak_powerslide'                                    
    #if own['powerslide_on'] == 1 and own['last_powerslide_on'] == 0:
        #print("power_on")
        #if own['powerslide'] == "reg2":
            
#            skater.playAction("nreg_powerslide", 0,20, layer=401, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_reg_powerslide", 0,20, layer=401, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_reg_powerslide", 0,20, layer=401, priority=0, play_mode=0, speed=1.5) 
#        if own['powerslide'] == "fak1":
#            own['requestAction'] = 'fak_powerslide'
#            skater.playAction("nfak_powerslide", 0,20, layer=401, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_fak_powerslide_d", 0,20, layer=401, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_fak_powerslide_t", 0,20, layer=401, priority=0, play_mode=0, speed=1.5)
            
#        if own['powerslide'] == "reg1":
#            #own['requestAction'] = 'reg_fs_powerslide'
#            skater.playAction("nreg_powerslide2", 0,20, layer=401, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_reg_powerslide2_d", 0,20, layer=401, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_reg_powerslide2_t", 0,20, layer=401, priority=0, play_mode=0, speed=1.5) 
#        if own['powerslide'] == "fak2":
#            #own['requestAction'] = 'fak_fs_powerslide'
#            skater.playAction("nfak_powerslide2", 0,20, layer=401, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_fak_powerslide2_d", 0,20, layer=401, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_fak_powerslide2_t", 0,20, layer=401, priority=0, play_mode=0, speed=1.5)            
            
####powerslide off#####                                 
#    if own['powerslide_on'] == 0 and own['last_powerslide_on'] == 1:
#        killact(400)
#        killact(401)

#        linVelocity4 = own.getLinearVelocity(True)    
#        newx = linVelocity4.x * .9       
#        force = [newx, linVelocity4.y, linVelocity4.z]
#        own.setLinearVelocity(force, True) 
#                
#        if own['powerslide'] == "reg2":   
#            skater.playAction("nreg_powerslide", 20,0, layer=4002, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_reg_powerslide", 20,0, layer=4002, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_reg_powerslide", 20,0, layer=4002, priority=0, play_mode=0, speed=1.5)
#        if own['powerslide'] == "fak1":   
#            skater.playAction("nfak_powerslide", 20,0, layer=4002, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_fak_powerslide_d", 20,0, layer=4002, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_fak_powerslide_t", 20,0, layer=4002, priority=0, play_mode=0, speed=1.5)     
#            
#        if own['powerslide'] == "reg1":   
#            skater.playAction("nreg_powerslide2", 20,0, layer=4002, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_reg_powerslide2_d", 20,0, layer=4002, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_reg_powerslide2_t", 20,0, layer=4002, priority=0, play_mode=0, speed=1.5)
#        if own['powerslide'] == "fak2":   
#            skater.playAction("nfak_powerslide2", 20,0, layer=4002, priority=8, play_mode=0, speed=1.5)
#            deck.playAction("a_fak_powerslide2_d", 20,0, layer=4002, priority=1, play_mode=0, speed=1.5)
#            trucks.playAction("a_fak_powerslide2_t", 20,0, layer=4002, priority=0, play_mode=0, speed=1.5)                                
#        #print("old power") 
def powerslide_sound():
    sact = own.actuators["powerslide_sound"]
    if own['powerslide_on'] == 1:
        sact = own.actuators["powerslide_sound"]
        sact.volume = .2
        new_pitch = (abs(linVelocity.x) / 3)
        #new_pitch = new_pitch * 1.1
        #print("np=", new_pitch)
        if new_pitch < 1.1 and new_pitch > .5: 
            sact.pitch = new_pitch
        elif new_pitch <= .5:
            sact.pitch = .5
        else:
            sact.pitch = 1.1    
        cont.activate(own.actuators["powerslide_sound"])
    else:
        sact.volume = .0
        cont.deactivate(own.actuators["powerslide_sound"])
                               
def check_powerslide():
    try:
        own['last_powerslide_on'] = own['powerslide_on']
    except:
        pass 
    psxvel = abs(linVelocity.x)
    #xvelsens = .1   
    if (lUD > .08 or lUD < -.08) and own['manual_v2'] == False and r_ground.triggered == True and psxvel > .1:
        if lUD > .08:
            powerslide()
        else:
            powerslide2()    
    else:
        own['powerslide_on'] = 0
        own['powerslide_counter'] = 0
        if own['last_powerslide_on'] == 0:    
            own['powerslide'] = None
def killmanuals():
    if own['last_manual_v2'] == 1 and own['manual_v2'] == 0:    
        fak_manual_off()
        reg_manual_off()                
        fak_nmanual_off()
        reg_nmanual_off()                

def killopos():
    if q5oncd < 1 and q1oncd <1:
        killact(65)
        killact(66)
        killact(67)
        killact(68)         
        killact(71)
        killact(72)
        killact(73)
        killact(74)     
                
stopAnims() 
#nextframe()  
air() 
stance()
turn()
#grind()
rotmult()
airup()
onramp()
speedmult()
coping()
onboard()
resetjumpstance()
grass()
grindoutair()
set_last_grindpos()
air_pos()
air_turn_boost()
record_grindsound()
check_powerslide()
powerslide_state()
powerslide_sound()
killmanuals()
killopos()
grind()




##################
###realcontrols###
##################
#       q1
#    q8    q2
# q7          q3
#    q6    q4
#       q5
##################
#lq6
if lUD > .04 and lLR < -0.04 :
    lq6on = 1
    q6oncdl = countdown
    own["Q6oncdl"] = q6oncdl
    #print("lq6on")
elif q6oncdl > 0:
    lq6on = 0
    q6oncdl = q6oncdl - 1
    own["Q6oncdl"] = q6oncdl
#lq8
if lUD < -.04 and lLR < -0.04 :
    lq8on = 1
    q8oncdl = countdown
    own["Q8oncdl"] = q8oncdl
    #print("lq8on")
elif q8oncdl > 0:
    lq8on = 0
    q8oncdl = q8oncdl - 1
    own["Q8oncdl"] = q8oncdl
#lq2
if lUD < -.04 and lLR > 0.04 :
    lq2on = 1
    q2oncdl = countdown
    own["Q2oncdl"] = q2oncdl
    #print("lq2on")
elif q2oncdl > 0:
    lq2on = 0
    q2oncdl = q2oncdl - 1
    own["Q2oncdl"] = q2oncdl
#q4
if lUD > 0.04 and lLR > 0.04 :
    lq4on = 1
    q4oncdl = countdown
    own["Q4oncdl"] = q4oncdl
    #print("lq4on")
elif q4oncdl > 0:
    lq4on = 0
    q4oncdl = q4oncdl - 1
    own["Q4oncdl"] = q4oncdl  
#q5
if lUD > .070 and lq4on == 0 and lq6on == 0:
    lq5on = 1
    q5oncdl = countdown
    own["Q5oncdl"] = q5oncdl
    #print("lq5on")
elif q5oncdl > 0:
    lq5on = 0
    q5oncdl = q5oncdl - 1
    own["Q5oncdl"] = q5oncdl   
#q1    
if lUD < -0.070 and lq8on !=1 and lq2on != 1:
    lq1on = 1
    q1oncdl = countdown
    own["Q1oncdl"] = q1oncdl
    #print("lq1on")              
elif q1oncdl > 0:
    lq1on = 0
    q1oncdl = q1oncdl - 1
    own["Q1oncdl"] = q1oncdl   
#q7
if lLR < -0.070 and lq8on != 1 and lq6on != 1:
    lq7on = 1
    q7oncdl = countdown
    own["Q7oncdl"] = q7oncdl
    #print("lq7on")       
elif q7oncdl > 0:
    lq7on = 0
    q7oncdl = q7oncdl - 1
    own["Q7oncdl"] = q7oncdl  
#q3    
if lLR > 0.070 and lq2on !=1 and lq4on != 1:
    lq3on = 1
    q3oncdl = countdown
    own["Q3oncdl"] = q3oncdl
    #print("lq3on") 
elif q3oncdl > 0:
    lq3on = 0
    q3oncdl = q3oncdl - 1
    own["Q3oncdl"] = q3oncdl       
#34567
own['set_revert_timer'] = 0
if q3oncdl < q4oncdl < q5oncdl < q6oncdl < q7oncdl:
    if r_ground.triggered == True:
        print("REVERT!!!")
        revert()
        own['set_revert_timer'] = 1
if q3oncdl > q4oncdl > q5oncdl > q6oncdl > q7oncdl:
    if r_ground.triggered == True:
        print("REVERT2!!!")
        revert2()
        own['set_revert_timer'] = 1
if q7oncdl < q8oncdl < q1oncdl < q2oncdl < q3oncdl:
    if r_ground.triggered == True:
        print("REVERT3!!!")
        revert3()
        own['set_revert_timer'] = 1
if q7oncdl > q8oncdl > q1oncdl > q2oncdl > q3oncdl:
    if r_ground.triggered == True:
        print("REVERT4!!!")
        revert4()
        own['set_revert_timer'] = 1           
################
#q6
if rUD > .04 and rLR < -0.04 :
    q6on = 1
    q6oncd = countdown
    own["Q6oncd"] = q6oncd
    #print("q6on")
elif q6oncd > 0:
    q6on = 0
    q6oncd = q6oncd - 1
    own["Q6oncd"] = q6oncd
    
#q8
if rUD < -.04 and rLR < -0.04 :
    q8on = 1
    q8oncd = countdown
    own["Q8oncd"] = q8oncd
    #print("q8on")
elif q8oncd > 0:
    q8on = 0
    q8oncd = q8oncd - 1
    own["Q8oncd"] = q8oncd
#q2
if rUD < -.04 and rLR > 0.04 :
    q2on = 1
    q2oncd = countdown
    own["Q2oncd"] = q2oncd
    #print("q2on")
elif q2oncd > 0:
    q2on = 0
    q2oncd = q2oncd - 1
    own["Q2oncd"] = q2oncd
    
#q4
if rUD > 0.04 and rLR > 0.04 :
    q4on = 1
    q4oncd = countdown
    own["Q4oncd"] = q4oncd
    #print("q4on")
elif q4oncd > 0:
    q4on = 0
    q4oncd = q4oncd - 1
    own["Q4oncd"] = q4oncd
#q5
if rUD > .070:
    if q4on == 0 and q6on == 0:
        #print("q5on")
        q5on = 1
        q5oncd = countdown
        own["Q5oncd"] = q5oncd
    oposin()   
if rUD > .02:    
    grindpos = own['grindpos']   
    jumpstance = own["jump_stance"]
    if LAST_GRIND == False:    
        if grindpos == "reg_stall":
            grindtype("nose_stall") #change
        elif grindpos == "fak_stall":
            grindtype("nose_stall")
        elif grindpos == "reg_5050":  
            if jumpstance != 3:
                if jumpstance == 0:
                    if rLR > .02:
                        grindtype("reg_tailgR")
                    elif rLR < -.02:
                        grindtype("reg_tailgL")
                    else:                        
                        grindtype("reg_tailg")
                if jumpstance == 1:
                    if rLR > .02:
                        grindtype("fak_tailgR")
                    elif rLR < -.02:
                        grindtype("fak_tailgL")
                    else:                        
                        grindtype("fak_tailg")
            else:
                if STANCE == 0:
                    if rLR > .03:
                        grindtype("reg_tailgR")
                    elif rLR < -.02:
                        grindtype("reg_tailgL")
                    else:        
                        grindtype("reg_tailg")
                if STANCE == 1:
                    grindtype("fak_tailg")                                 
        elif grindpos == "reg_board":
            if jumpstance != 3:
                if jumpstance == 0:
                    grindtype("reg_tailslide")
                if jumpstance == 1:
                    grindtype("fak_tailslide") 
                STANCE = jumpstance
                own['stance'] = STANCE       
            else:        
                if STANCE == 0:
                    grindtype("reg_tailslide")
                if STANCE == 1:
                    grindtype("fak_tailslide")    
        else:
            if jumpstance == 0:
                grindtype("reg_tailg")
            if jumpstance == 1:
                grindtype("fak_tailg")   
          
        
elif q5oncd > 0:
    q5on = 0
    q5oncd = q5oncd - 1
    own["Q5oncd"] = q5oncd
    killact(65)
    killact(66)
    killact(67)
    killact(68) 
    flipping = skater.isPlayingAction(fliplay)    
#    if own["last_Opos"] == True and flipping == False:
#        if STANCE == False:
#            skater.playAction("noposin", 20,1, layer=69, priority=3, blendin=10, play_mode=0, speed=.5)
#        elif STANCE == True:
#            skater.playAction("fak_oposin", 20,1, layer=70, priority=3, blendin=10, play_mode=0, speed=.5)
        #skater.stopAction(7)
        #skater.stopAction(0)       
    own["last_Opos"] = False
#q1    
if rUD < -0.070:
    if q2on == 0 and q8on == 0:
        #print("q1on")
        q1on = 1
        q1oncd = countdown
        own["Q1oncd"] = q1oncd
    noposin()
if rUD < -0.020:    
    grindpos = own['grindpos']
    jumpstance = own["jump_stance"]
    if LAST_GRIND == False:       
        if grindpos == "reg_5050":
            #print("nose something")
            if jumpstance != 3:  
                if jumpstance == 0:
                    if rLR > .02:
                        grindtype("reg_nosegR")
                    elif rLR < -.02:
                        grindtype("reg_nosegL")    
                    else:
                        #print("gtype reg_nosegR")    
                        grindtype("reg_noseg")
                if jumpstance == 1:
                    if rLR > .02:
                        grindtype("fak_nosegR")
                    elif rLR < -.02:
                        grindtype("fak_nosegL")
                    else:
                        grindtype("fak_noseg")   
            else:
                if STANCE == 0:
                    if rLR > .02:
                        grindtype("reg_nosegR")
                    elif rLR < -.02:
                        grindtype("reg_nosegL")    
                    else:                    
                        grindtype("reg_noseg")
                if STANCE == 1:
                    if rLR > .02:
                        grindtype("fak_nosegR")
                    elif rLR < -.02:
                        grindtype("fak_nosegL")  
                    else:    
                        grindtype("fak_noseg")        
        elif grindpos == "reg_board":
            #print("nose something")
            if jumpstance != 3:
                if jumpstance == 0:
                    grindtype("reg_noseslide")    
                if jumpstance == 1:
                    grindtype("fak_noseslide") 
                STANCE = jumpstance    
                own['stance'] = STANCE    
            else:
                if STANCE == 0:
                    grindtype("reg_noseslide")
                if STANCE == 1:
                    grindtype("fak_noseslide")               
   
elif q1oncd > 0:
    q1on = 0
    q1oncd = q1oncd - 1
    own["Q1oncd"] = q1oncd
    killact(73)
    killact(74)
    killact(71)
    killact(72)
    flipping = skater.isPlayingAction(fliplay)       
#    if own["last_nOpos"] == True and flipping == False:

#        if STANCE == 0 and r_ground.triggered:
#            skater.playAction("nnoposin", 20,1, layer=75, priority=3, blendin=10, play_mode=0, speed=.5)
#        elif STANCE == 1 and r_ground.triggered:
#            skater.playAction("fak_noposin", 20,1, layer=76, priority=3, blendin=10, play_mode=0, speed=.5)
    own["last_nOpos"] = False   
       
#q7
if rLR < -0.070:
    if q8on == 0 and q6on == 0:
        q7on = 1
        q7oncd = countdown
        own["Q7oncd"] = q7oncd
        #print("q7on")
       
elif q7oncd > 0:
    q7on = 0
    q7oncd = q7oncd - 1
    own["Q7oncd"] = q7oncd
#q3    
if rLR > 0.070:
    if q4on == 0 and q2on == 0:
        q3on = 1
        q3oncd = countdown
        own["Q3oncd"] = q3oncd
        #print("q3on")
elif q3oncd > 0:
    q3on = 0
    q3oncd = q3oncd - 1
    own["Q3oncd"] = q3oncd

#trick calls



# 360 flip
# 3 > 4 > 5 > 8

# laser flip
# 7 > 6 > 5 > 2  

#nollie 360 shovit
if q7oncd > 0 and q8oncd > 0 and q1oncd > 0 and q2oncd > 0 and q3oncd > 0 and q7oncd <= q8oncd <= q1oncd <= q2oncd <= q3oncd:
    print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
    print ("Nollie 360 shovit")
    dict['trick_string'] = 'Nollie 360 Shovit'
    nollie_shovit360()
    q7oncd = 0
    q8oncd = 0
    q1oncd = 0
    q2oncd = 0
    q3oncd = 0
    own["Q7oncd"] = q7oncd
    own["Q8oncd"] = q8oncd
    own["Q1oncd"] = q1oncd
    own["Q2oncd"] = q2oncd
    own["Q3oncd"] = q3oncd

#nollie fs 360 shovit
if q7oncd > 0 and q8oncd > 0 and q1oncd > 0 and q2oncd > 0 and q3oncd > 0 and q3oncd <= q2oncd <= q1oncd <= q8oncd <= q7oncd:
    #print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
    print ("Nollie Front Side 360 shovit")
    dict['trick_string'] = 'Nollie FS 360 Shovit'
    nollie_fsshovit360()
    q7oncd = 0
    q8oncd = 0
    q1oncd = 0
    q2oncd = 0
    q3oncd = 0
    own["Q7oncd"] = q7oncd
    own["Q8oncd"] = q8oncd
    own["Q1oncd"] = q1oncd
    own["Q2oncd"] = q2oncd
    own["Q3oncd"] = q3oncd    

# varial heelflip
# 7 < 6 < 2
if q7oncd > 0 and q6oncd > 0 and q2oncd > 0 and q7oncd < q6oncd < q2oncd:
    dict['trick_string'] = 'Varial Heelflip'
    varial_heelflip()
    reset_rtimers()
    
# varial kickflip 
# 3 < 4 < 8
if q3oncd > 0 and q4oncd > 0 and q8oncd > 0 and q3oncd < q4oncd < q8oncd:
    dict['trick_string'] = 'Varial Kickflip'
    varial_kickflip()
    reset_rtimers()

# nollie varial kickflip
# 3 < 2 < 6
if q3oncd > 0 and q2oncd > 0 and q6oncd > 0 and q3oncd <= q2oncd <= q6oncd:
    dict['trick_string'] = 'Nollie Varial Kickflip'
    print('Nollie Varial Kickflip')
    nollie_varial_kickflip()
    reset_rtimers()   
    
# nollie varial heelflip
# 7 < 8 < 4
if q7oncd > 0 and q8oncd > 0 and q4oncd > 0 and q7oncd <= q8oncd <= q4oncd:
    dict['trick_string'] = 'Nollie Varial Heelflip'
    print('Nollie Varial Heelflip')
    nollie_varial_heelflip()
    reset_rtimers()   




#360 shovit
if q3oncd > 0 and q4oncd > 0 and q5oncd > 0 and q6oncd > 0 and q7oncd > 0 and q7oncd >= q6oncd >= q5oncd >= q4oncd >= q3oncd:
#    print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
    #print ("______-------360 shovit")
    dict['trick_string'] = '360 Shovit'
    shovit360()
    q3oncd = 0
    q4oncd = 0
    q5oncd = 0
    q6oncd = 0
    q7oncd = 0
    own["Q3oncd"] = q3oncd
    own["Q4oncd"] = q4oncd
    own["Q5oncd"] = q5oncd
    own["Q6oncd"] = q6oncd
    own["Q7oncd"] = q7oncd
#360 fs shovit    
if q3oncd > 0 and q4oncd > 0 and q5oncd > 0 and q6oncd >= 0 and q7oncd > 0 and q7oncd <= q6oncd <= q5oncd <= q4oncd <= q3oncd:
#    print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
    #print ("______-------360 shovit")
    dict['trick_string'] = '360 Frontside Shovit'
    fsshovit360()
    q3oncd = 0
    q4oncd = 0
    q5oncd = 0
    q6oncd = 0
    q7oncd = 0
    own["Q3oncd"] = q3oncd
    own["Q4oncd"] = q4oncd
    own["Q5oncd"] = q5oncd
    own["Q6oncd"] = q6oncd
    own["Q7oncd"] = q7oncd    

#ollie
if q5oncd > 0 and q1oncd > 0 and q5oncd < q1oncd:
    JUMPSTRENGTH = q1oncd - q5oncd
    #4,7
    if JUMPSTRENGTH <= 4:
       JUMPSTRENGTH = 1.1
    if JUMPSTRENGTH > 4 and JUMPSTRENGTH < 7:
       JUMPSTRENGTH = 1        
    if JUMPSTRENGTH >= 7:
       JUMPSTRENGTH = .9               
    aollie()
    
    q1oncd = 0
    q5oncd = 0
    own["Q1oncd"] = q1oncd
    own["Q5oncd"] = q5oncd
    
#nollie
if q5oncd > 0 and q1oncd > 0 and q5oncd > q1oncd:
    JUMPSTRENGTH = q5oncd - q1oncd
    #4,7
    if JUMPSTRENGTH <= 4:
       JUMPSTRENGTH = 1.1
    if JUMPSTRENGTH > 4 and JUMPSTRENGTH < 7:
       JUMPSTRENGTH = 1        
    if JUMPSTRENGTH >= 7:
       JUMPSTRENGTH = .9
    nollie()
    q1oncd = 0
    q5oncd = 0
    own["Q1oncd"] = q1oncd
    own["Q5oncd"] = q5oncd
    print("nollie")

#kickflip
if q5oncd > 0 and q8oncd > 0 and q5oncd < q8oncd and q3oncd < 1:
    kickflip()
    q8oncd = 0
    q5oncd = 0
    own["Q8oncd"] = q8oncd
    own["Q5oncd"] = q5oncd
    
#nollie kickflip
if q1oncd > 0 and q6oncd > 0 and q1oncd < q6oncd:
    nollie_kickflip()
    q6oncd = 0
    q1oncd = 0
    own["Q6oncd"] = q6oncd
    own["Q1oncd"] = q1oncd    

#heelflip
if q5oncd > 0 and q2oncd > 0 and q5oncd < q2oncd:
    heelflip()
    q2oncd = 0
    q5oncd = 0
    own["Q2oncd"] = q2oncd
    own["Q5oncd"] = q5oncd
    
#nollie_heelflip
if q1oncd > 0 and q4oncd > 0 and q1oncd < q4oncd:
    nollie_heelflip()
    q1oncd = 0
    q4oncd = 0
    own["Q1oncd"] = q1oncd
    own["Q4oncd"] = q4oncd    


#shovit
if q4oncd > 0 and q5oncd > 0 and q6oncd > 0 and q4oncd <= q5oncd <= q6oncd and q3oncd < 1:
   shovit()
   q4oncd = 0
   q5oncd = 0
   q6oncd = 0
   own["Q4oncd"] = q4oncd
   own["Q5oncd"] = q5oncd
   own["Q6oncd"] = q6oncd
    
#nollie_shovit
if q2oncd > 0 and q1oncd > 0 and q8oncd > 0 and q2oncd <= q1oncd <= q8oncd and q3oncd == 0:
    nollie_shovit()
    print('nollie shuvit')
    #nollie_fsshovit()
    q2oncd = 0
    q1oncd = 0
    q8oncd = 0
    own["Q2oncd"] = q2oncd
    own["Q1oncd"] = q1oncd
    own["Q8oncd"] = q8oncd    
    
#fsshovit
if q4oncd > 0 and q5oncd > 0 and q6oncd > 0 and q6oncd <= q5oncd <= q4oncd and q7oncd < 1:
#    print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
#    print ("^%*^%*^%*^%fsshovit")
    fsshovit()
    q4oncd = 0
    q5oncd = 0
    q6oncd = 0
    own["Q4oncd"] = q4oncd
    own["Q5oncd"] = q5oncd
    own["Q6oncd"] = q6oncd
    
#nollie_fsshovit
if q8oncd > 0 and q1oncd > 0 and q2oncd > 0 and q8oncd <= q1oncd <= q2oncd and q7oncd == 0:
#    print("q4oncd: ", q4oncd, " q5oncd: ", q5oncd, " q6oncd: ", q6oncd)
    print ("nollie fsshovit")
    nollie_fsshovit()
    #nollie_shovit()
    q8oncd = 0
    q1oncd = 0
    q2oncd = 0
    own["Q8oncd"] = q4oncd
    own["Q1oncd"] = q5oncd
    own["Q2oncd"] = q6oncd 

#360 shovit

# 360 shovit
# 3 > 4 > 5 >6 > 7

# fs 360 shovit
# 7 > 6 > 5 > 4 > 3



     

def hippy_jump():
    STANCE = own["stance"]
    if own['hippy'] == 1 and own['last_hippy'] == 0:
        if STANCE == 0:
            skater.playAction("reg_hippy", 1,10, layer=1101, priority=1, layer_weight=0, play_mode=0, speed=.5)
        if STANCE == 1:
            skater.playAction("fak_hippy", 1,10, layer=1101, priority=1, layer_weight=0, play_mode=0, speed=.5)            
    if own['hippy'] == 1 and own['last_hippy'] == 1:
        if STANCE == 0:
            skater.playAction("reg_hippy", 10,10, layer=1100, priority=0, layer_weight=0, play_mode=1, speed=.5)
        if STANCE == 1:
            skater.playAction("fak_hippy", 10,10, layer=1100, priority=0, layer_weight=0, play_mode=1, speed=.5)
    if own['hippy'] == 0 and own['last_hippy'] == 1:
        killact(1100)
        if rLR > turnsens:
            local = True
            rot = [ 0.0, 0.0, 3.14]
            own.applyRotation(rot,local)
            print("hippy turn")
            if STANCE == 0:
                skater.playAction("reg_hippy_ncw", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5)
                print('%hip1')
            if STANCE == 1:
                skater.playAction("fak_hippy_ncw", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5)                
                print('%hip2')
        elif rLR < -turnsens:
            local = True
            rot = [ 0.0, 0.0, -3.14]
            own.applyRotation(rot,local)
            print("hippy turn neg")            
            if STANCE == 0:
                skater.playAction("fak_hippy_nccw", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5)  
                print('%hip3')
            if STANCE == 1:
                skater.playAction("reg_hippy_nccw", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5) 
                print('%hip4')
##straight        
        else:
            if STANCE == 0:
                skater.playAction("reg_hippy", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5)
            if STANCE == 1:
                skater.playAction("fak_hippy", 10,40, layer=1102, priority=1, layer_weight=0, play_mode=0, speed=.5)                                        

#pushing and hippy jumps

since_a = frame - lastaf
since_x = frame - lastxf
cush = 10
hippy = 0
own['hippy'] = 0
#print(since_a, "a", since_x, "x")

#if xBut == 1 and aBut == 1 and since_a <= cush and since_x <= cush and (lTrig < 0.02 and rTrig < 0.02): 
if xBut == 1 and aBut == 1 and (lTrig < 0.02 and rTrig < 0.02) and r_ground.triggered == True: 
    #F"hippy")
    hippy = 1
    own['hippy'] = 1
    #hippy_jump()
#print(hippy)
hippy_jump()    
if since_a > cush and aBut == 1 and lasta == 1 and (lTrig < 0.02 and rTrig < 0.02) and own['last_hippy'] == 0:
    #print("apush suckka", since_a)
    if xBut == 0 and hippy == 0 and lastaBut_ground == True:
        push()
if since_x > cush and xBut == 1 and lastx == 1 and (lTrig < 0.02 and rTrig < 0.02) and own['last_hippy'] == 0:
    #print("push suckka", since_x)
    if aBut == 0 and hippy == 0 and lastxBut_ground == True:
        push_goof()      
#cavemans 
if LAST_GRIND == False and grindHit == False and r_ground.triggered:    
    if (aBut ==0 and own['lastaBut_ground'] == 1) and lTrig > 0.02:
        brfoot()
    if (aBut ==0 and own['lastaBut_ground'] == 1) and rTrig > 0.02:
        frfoot()
    if (xBut ==0 and own['lastxBut_ground'] == 1) and lTrig > 0.02:
        blfoot()
    if (xBut ==0 and own['lastxBut_ground'] == 1) and rTrig > 0.02:
        flfoot()              
    
#push b button
if (bBut == 0 and own["lastStop"] == True) or (bBut == 1 and own["lastStop"] == False):
        skater.stopAction(7)
        skater.stopAction(1)
        killact(18)
        killact(19)
        
if bBut == 0 and own["lastStop"] == True:
    if STANCE == True:
        skater.playAction("fak_stopin", 15,1, layer=6, priority=3, blendin=10, play_mode=0, speed=.5)    
    elif STANCE == False:
        skater.playAction("reg_stopin", 15,1, layer=7, priority=3, blendin=10, play_mode=0, speed=.5)

if bBut == 1:
    #print("push suckka")
    if linVelocity.x > .05 or linVelocity.x < -.05:
        stop()
    elif linVelocity.x < .05 or linVelocity.x > -.05:
        if own["lastStop"] == True:
            if STANCE == True:
                skater.playAction("fak_stopin", 15,1, layer=8, priority=3, blendin=10, play_mode=0, speed=.5)    
            elif STANCE == False:
                skater.playAction("reg_stopin", 15,1, layer=9, priority=3, blendin=10, play_mode=0, speed=.5)
            own["lastStop"] = False
elif bBut ==0:
        own["lastStop"] = False
##### falls
#space = own.sensors['space']
#if space.triggered:
#    own['fall'] = 1
#else:
#    own['fall'] = 0    

if own['fall'] == 1:
    offboard()
    own['getoffboard'] = True
####

#y button
if own['lasty'] == 1 and yBut ==0:
    offboard()        

if own["GRAB_ON"] == True:
    playing = skater.isPlayingAction(fliplay)
    if playing == 1:
        frame = skater.getActionFrame(fliplay)
        #print("Flipping frame: ", frame)
        if frame > 16:
            skater.stopAction(fliplay)
#frontside grab
flipping = skater.isPlayingAction(fliplay) 
#if rTrig > 0.02 and GRAB_ON == False and r_ground.triggered == 0:
if rTrig > 0.02 and r_ground.triggered == 0 and flipping == False:    
    GRAB_ON = True
    own["GRAB_ON"] = GRAB_ON
    #print(rTrig, GRAB_ON)

    if STANCE == False and rUD >= -.07 and rUD <= .07:
        frontside_grab_on()
    elif STANCE == True and rUD >= -.07 and rUD <= .07:
        fakbackside_grab_on()
    #front_nose    
    if STANCE == True and rUD < -0.070:
        fak_backside_nose_grab_on()
    #front_tail    
    elif STANCE == True and rUD > 0.07:
        fak_backside_tail_grab_on() 
    #    
    if STANCE == False and rUD < -0.070:
        frontside_nose_grab_on()
    #front_tail    
    elif STANCE == False and rUD > 0.07:
        frontside_tail_grab_on()                


#if rTrig <= 0.02 and GRAB_ON == True and lTrig >= -.02:
#    GRAB_ON = False
#    own["GRAB_ON"] = GRAB_ON
#    GRAB_PLAYED = False
#    own["GRAB_PLAYED"] = GRAB_PLAYED
if rTrig <= 0.02 and GRAB_ON == True:
    killact(400)
    killact(401)
    #killact(403)
    killact(404)
    killact(408)
    killact(409)
    killact(410)
    killact(2925)

#backside grab
#if lTrig > 0.02 and GRAB_ON == False and r_ground.triggered == 0:
if lTrig > 0.02 and r_ground.triggered == 0 and flipping == False:    
    GRAB_ON = True
    own["GRAB_ON"] = GRAB_ON
    #print(rTrig)
    if STANCE == False and rUD >= -.07 and rUD <= .07:
        backside_grab_on()
    elif STANCE == True and rUD >= -.07 and rUD <= .07:
        fakfrontside_grab_on()
    #front_nose    
    if STANCE == True and rUD < -0.070:
        fak_frontside_nose_grab_on()
    #front_tail    
    elif STANCE == True and rUD > 0.07:
        fak_frontside_tail_grab_on() 
    #front_nose    
    if STANCE == False and rUD < -0.070:
        backside_nose_grab_on()
    #front_tail    
    elif STANCE == False and rUD > 0.07:
        backside_tail_grab_on()                  
        
#kill grabs        
if lTrig <= 0.02 and GRAB_ON == True and lTrig >= -.02 and rTrig <= .02 and rTrig >= -.2:
    GRAB_ON = False
    own["GRAB_ON"] = GRAB_ON
    GRAB_PLAYED = False
    own["GRAB_PLAYED"] = GRAB_PLAYED
if lTrig <= 0.02 or r_ground.triggered == 1:
    killact(402)
    killact(403)
    killact(405)
    killact(406)
    killact(407)
    killact(411)
    killact(412)
    #killact(404)
#if lTrig <= 0.02 or r_ground.triggered == 1:
#    killact(402)
#    killact(403)
#    #killact(405)
#    #killact(406)
#    killact(407)
#    #killact(404)    

#frontside pump #backside pump
if (rTrig > 0.02 and GRAB_ON == False and r_ground.triggered == 1) or (lTrig > 0.02 and GRAB_ON == False and r_ground.triggered == 1):
    pump()
else:
    if own['lastPump'] == True:
        #skater.stopAction(0) 
        killact(20)
        killact(21)
        killact(22)
        killact(23)
#        if STANCE == 0:
#            skater.playAction("nreg_pump_in", 20,1, layer=24, priority=8, blendin=10, play_mode=0, speed=1)
#        elif STANCE == 1:
#            skater.playAction("nfak_pump_in", 20,1, layer=25, priority=8, blendin=10, play_mode=0, speed=1)
    own["lastPump"] = False 
    own["Pump"] = False 
    #print("stop pumping")
def footplant():    
    #a_reg_fp_rback
    framenum = own['framenum']
    last_ground_frame = own['lF_ground_frame']
    lF_air_frame = own['lF_air_frame']
    frames_since_ground = framenum - lF_air_frame
    frames_since_grind = framenum - own['last_grind_frame']
    #print(frames_since_ground, "fsg")
    if LAST_GRIND == False and grindHit == True and aBut == True and frames_since_ground < 40 and touched:
    #if LAST_GRIND == False and aBut == True and frames_since_ground < 10 and r_ground.triggered == 1:        
    #if grindHit == True and aBut == True and frames_since_ground < 20:    
        own.setLinearVelocity([0,0,0],0)
        killall()
        if STANCE == 0:
            skater.playAction("reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            deck.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            trucks.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            skater.playAction("reg_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)
            deck.playAction("a_reg_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)
            trucks.playAction("a_reg_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)
        if STANCE == 1:
            skater.playAction("fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            deck.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            trucks.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
            skater.playAction("fak_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)
            deck.playAction("a_fak_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)
            trucks.playAction("a_fak_fp_rback", 1,10, layer=2928, priority=8, play_mode=0, speed=1)                            
        own['footplant_on'] = 1
    if grindHit == False:
        own['footplant_on'] = 0 
    if own['footplant_on'] == True and rUD < turnsens and rUD > -turnsens:
        own.setLinearVelocity([0,0,0],0)
    if own['footplant_on'] == 1 and own['last_footplant'] == True:
        if skater.isPlayingAction(2925) == False:
            if STANCE == 0:
                skater.playAction("reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
                deck.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
                trucks.playAction("a_reg_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)                
            if STANCE == 1:
                skater.playAction("fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
                deck.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)
                trucks.playAction("a_fak_fp_rback", 10,10, layer=2925, priority=8, play_mode=1, speed=.5)                        
    if own['last_footplant'] == True and own['footplant_on'] == 0:
        killall()
        if STANCE == 0:
            skater.playAction("reg_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)
            deck.playAction("a_reg_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)
            trucks.playAction("a_reg_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)  
        if STANCE == 1:
            skater.playAction("fak_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)
            deck.playAction("a_fak_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)
            trucks.playAction("a_fak_fp_rback", 10,20, layer=2928, priority=8, play_mode=0, speed=1)            
def invert():    
    if LAST_GRIND == False and grindHit == True and own['grindpos'] == 'reg_board':
        if lBump == 1:
            #print("invert")
        #if coping_on ==1 and lBump == 1:
            print("IIIIIINVVERT")   
            own['invert_on'] = 1
            own.setLinearVelocity([0,0,0],0)
    if own["coping"] == 1 and invert_on == 1:
        killact(25)
        killact(24)
#        if STANCE == False:             
#            skater.playAction("reg_back_invert", 0,0, layer=300, play_mode=0, speed=.5) 
#            deck.playAction("a_reg_back_invert", 0,0, layer=301, play_mode=0, speed=.5)
#            trucks.playAction("a_reg_back_invert", 0,0, layer=302, play_mode=0, speed=.5)  
#        if STANCE == True:             
#            skater.playAction("fak_back_invert", 0,0, layer=300, play_mode=0, speed=.5) 
#            deck.playAction("a_fak_back_invert", 0,0, layer=301, play_mode=0, speed=.5)
#            trucks.playAction("a_fak_back_invert", 0,0, layer=302, play_mode=0, speed=.5)              
        if own['invert_on'] == 1 and own['last_invert'] == False:
            killall()
            cont.activate(own.actuators['invertOn_sound'])
            
            if STANCE == False:
                own['invert_type'] = "reg_back_invert_in"
                skater.playAction("reg_back_invert_in", 10,30, layer=303, play_mode=0, speed=1) 
                deck.playAction("a_reg_back_invert_in", 10,30, layer=303, play_mode=0, speed=1)
                trucks.playAction("a_reg_back_invert_in", 10,30, layer=303, play_mode=0, speed=1) 
            if STANCE == True:
                own['invert_type'] = "fak_fr_invert"
                skater.playAction("fak_fr_invert", 10,30, layer=303, play_mode=0, speed=1) 
                deck.playAction("a_fak_fr_invert", 10,30, layer=303, play_mode=0, speed=1)
                trucks.playAction("a_fak_fr_invert", 10,30, layer=303, play_mode=0, speed=1)                           
    if invert_on == 0 and own['last_invert'] == True:
        #print("kill invert")
        own['last_invert_frame'] = frame
        cont.activate(own.actuators['invertOff_Sound'])
        
        killact(300)
        killact(301)
        killact(302)    
        killact(303)
        killact(304)
        killact(305) 
        killact(700)
        killact(700)
        killact(700)
        killact(290)
        killact(291)
        killact(292)
        if own['invert_type'] == "reg_back_invert_in":
            skater.playAction("reg_back_invert_in", 20,0, layer=306, play_mode=0, speed=1) 
            deck.playAction("a_reg_back_invert_in", 20,0, layer=306, play_mode=0, speed=1)
            trucks.playAction("a_reg_back_invert_in", 20,0, layer=306, play_mode=0, speed=1)
        if own['invert_type'] == "fak_fr_invert":    
            skater.playAction("fak_fr_invert", 20,0, layer=306, play_mode=0, speed=1) 
            deck.playAction("a_fak_fr_invert", 20,0, layer=306, play_mode=0, speed=1)
            trucks.playAction("a_fak_fr_invert", 20,0, layer=306, play_mode=0, speed=1)             
    if invert_on == 1:
        if own['invert_type'] == "reg_back_invert_in":
            skater.playAction("reg_back_invert_in", 30,30, layer=290, play_mode=1, speed=1) 
            deck.playAction("a_reg_back_invert_in", 30,30, layer=290, play_mode=1, speed=1)
            trucks.playAction("a_reg_back_invert_in", 30,30, layer=290, play_mode=1, speed=1)
            
        if own['invert_type'] == "fak_fr_invert":
                skater.playAction("fak_fr_invert", 30,30, layer=290, play_mode=1, speed=1) 
                deck.playAction("a_fak_fr_invert", 30,30, layer=290, play_mode=1, speed=1)
                trucks.playAction("a_fak_fr_invert", 30,30, layer=290, play_mode=1, speed=1)
    lif = own['last_invert_frame'] 
    if frame - lif > 3 and invert_on == 0:
        own['invert_type'] = None
invert() 
footplant()
    
#else:
    #own['invert_on'] = 0 
  
if own['invert_on'] == 0: 
    killact(900)
    #killact(901)
    #killact(902)       
#print("l: ", lBump)
    
def reset_pos():
    #reset
    if ddPad == 1:
        
        spawn_pos = own['spawn_pos']
        spawn_rot = own['spawn_rot']
        try:
            own.worldPosition = (spawn_pos[0], spawn_pos[1], (spawn_pos[2] + .1))
            own.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
        except:    
            own.worldPosition = (0, 0, .1)
            own.worldOrientation = [[1.0, 0.0, 0.0], [ 0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]           
        if own["spawn_stance"] == 1:
            own.setLinearVelocity([.1,0,0], 1)
            #cam.worldPosition = (spawn_pos[0], spawn_pos[1], (spawn_pos[2] + .25))
            #cam.applyMovement([0,-1,0], True)
            #lx = cam.localPosition[1] 
            #lx = lx - 4
            #cam.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
            #cam.localPosition[1] = lx
         
        else: 
            own.setLinearVelocity([-.1,0,0], 1)         
            #cam.worldPosition = (spawn_pos[0], spawn_pos[1], (spawn_pos[2] + .25))
            #cam.applyMovement([0,1,0], True)            
            #lx = cam.localPosition[1]
            #lx = lx - 4
            #cam.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
            #cam.localPosition[1] = lx
    if udPad == 1:
        own['spawn_pos'] = [own.worldPosition[0], own.worldPosition[1], own.worldPosition[2]] 
        own['spawn_rot'] = [[own.worldOrientation[0][0],own.worldOrientation[0][1],own.worldOrientation[0][2]], [own.worldOrientation[1][0],own.worldOrientation[1][1],own.worldOrientation[1][2]], own.worldOrientation[2][2]]
        stance = own["stance"]
        own["spawn_stance"] = stance


   
#start button    
if stBut == True:
    own.actuators["sroll"].volume = .0001
    cont.deactivate(own.actuators["sroll"])
    own.actuators["sroll"].stopSound()

#    print("Start")
#    if own["gamepaused"] == False:
#        cont.activate(own.actuators["pause"])    
#        own["gamepaused"] == True
#    if own["gamepaused"] == True:
#        cont.activate(own.actuators["resume"])
#        own["gamepaused"] == False

     
def ylimit():
    #if r_ground.triggered and touched == False and grindDar == 0:
    lgf = own['last_grind_frame']
    frame = own['framenum']
    frames_since_grinding = frame - lgf
    if r_ground.triggered and touched == False and grindHit == 0 and frames_since_grinding > 20:    
        linVelocity4 = own.getLinearVelocity(True)
        newy = linVelocity4.y * .8 #.4    
        force = [linVelocity4.x, newy, linVelocity4.z]
        own.setLinearVelocity(force, True)   
        #print("limitting y")       
#        own["linVely"] = linVelocity.y 
def getoffboard():
    lasty = own['lasty']
    getoffboard = own['getoffboard']
    if getoffboard == 1 and own['fall'] == False:    
        own['getoffboard'] = 0 
    if yBut == False and lasty == True:
        own['getoffboard'] = 1        

def switchcam():
    pass
#    if ltsBut == False and own['lastlts'] == True and rtsBut == False:
#        if own['camera'] == 1:
#            own['camera'] = 0
#        else:
#            own['camera'] = 1
#    if rtsBut == False and own['lastrts'] == True and ltsBut == False:
#        if own['camera'] == 2:
#            own['camera'] = 0
#        else:
#            own['camera'] = 2 
#followcam 
def move_followcam():
    if own['camera'] == 2:
        #if rtsBut == False and own['lastrts'] == True:
        if own['lastbkBut'] == True and bkBut == False:
            #print("activate move followcam") 
            if own['move_followcam'] == False:
                own['move_followcam'] = True
            else:
                own['move_followcam'] = False                       
        if own['move_followcam'] == True:
            #act = followcam.actuators[
            camspeed1 = .015
            camspeed2 = .055
            camrot1 = .005
            camrot2 = .02
            #up
            if lUD < -0.080:
                followcam.actuators["up"].dLoc = [ 0, 0, -camspeed2]
                cont.activate(followcam.actuators["up"])
                #print("fastup")
            else:
                cont.deactivate(followcam.actuators["up"])    
#            #down    
            if lUD > .080:
                followcam.actuators["down"].dLoc = [ 0, 0, camspeed2]
                cont.activate(followcam.actuators["down"])
            else:
                cont.deactivate(followcam.actuators["down"])                    
#            #left
            if lLR < -0.080:
                followcam.actuators["left"].dLoc = [-camspeed2, 0, 0]                
                cont.activate(followcam.actuators["left"])
            else:
                cont.deactivate(followcam.actuators["left"])                    
#            #right
            if lLR > 0.080:         
                followcam.actuators["right"].dLoc = [camspeed2, 0, 0]                
                cont.activate(followcam.actuators["right"])
            else:
                cont.deactivate(followcam.actuators["right"])  
            #up
            if rUD < -0.080:
                followcam.actuators["rotup"].dLoc = [0, 0, camrot2]
                cont.activate(followcam.actuators["rotup"])
                #print("uppppppppppppppppppppppppppp")
            else:
                cont.deactivate(followcam.actuators["rotup"])    
#            #down    
            if rUD > .080:
                followcam.actuators["rotdown"].dLoc = [0, 0, -camrot2]                
                cont.activate(followcam.actuators["rotdown"])
            else:
                cont.deactivate(followcam.actuators["rotdown"])                    
#            #left
            if rLR < -0.080:
                followcam.actuators["rotleft"].dRot = [0, 0, camrot2]                
                cont.activate(followcam.actuators["rotleft"])
            else:
                cont.deactivate(followcam.actuators["rotleft"])                    
#            #right
            if rLR > 0.080:         
                followcam.actuators["rotright"].dRot = [0, 0, -camrot2]
                cont.activate(followcam.actuators["rotright"])
            else:
                cont.deactivate(followcam.actuators["rotright"]) 

#*********************************************                
                
            if lUD > -0.080 and lUD < -0.030:
                followcam.actuators["up"].dLoc = [ 0, 0, -camspeed1]
                cont.activate(followcam.actuators["up"])
                #print(lUD)
            else:
                cont.deactivate(followcam.actuators["up"])    
#            #down    
            if lUD < .080 and lUD > .03:
                followcam.actuators["down"].dLoc = [ 0, 0, camspeed1]                
                cont.activate(followcam.actuators["down"])
            else:
                cont.deactivate(followcam.actuators["down"])                    
#            #left
            if lLR > -0.080 and lLR < -0.030:
                followcam.actuators["left"].dLoc = [-camspeed1, 0, 0]                
                cont.activate(followcam.actuators["left"])
            else:
                cont.deactivate(followcam.actuators["left"])                    
#            #right
            if lLR < .080 and lLR > .03:       
                followcam.actuators["right"].dLoc = [camspeed1, 0, 0]
                cont.activate(followcam.actuators["right"])
            else:
                cont.deactivate(followcam.actuators["right"])  
            #up
            if rUD > -0.080 and rUD < -0.030:
                followcam.actuators["rotup"].dRot = [camrot1, 0, 0]                
                cont.activate(followcam.actuators["rotup"])
            else:
                cont.deactivate(followcam.actuators["rotup"])    
#            #down    
            if rUD < .080 and rUD > .03:
                followcam.actuators["rotdown"].dRot = [-camrot1, 0, 0]                
                cont.activate(followcam.actuators["rotdown"])
            else:
                cont.deactivate(followcam.actuators["rotdown"])                    
#            #left
            if rLR > -0.080 and rLR < -0.030:
                followcam.actuators["rotleft"].dRot = [0, 0, camrot1]
                cont.activate(followcam.actuators["rotleft"])
            else:
                cont.deactivate(followcam.actuators["rotleft"])                    
#            #right
            if rLR < .080 and rLR > .03:         
                followcam.actuators["rotright"].dRot = [0, 0, -camrot1]
                cont.activate(followcam.actuators["rotright"])
            else:
                cont.deactivate(followcam.actuators["rotright"])                       
def move_flycam():
    if own['camera'] == 1:
        #if rtsBut == False and own['lastrts'] == True:
        if own['lastbkBut'] == True and bkBut == False: 
            if own['move_freecam'] == False:
                own['move_freecam'] = True
            else:
                own['move_freecam'] = False                       
        if own['move_freecam'] == True:
            #act = freecam.actuators[
            camspeed1 = .015
            camspeed2 = .055
            camrot1 = .005
            camrot2 = .02
            #up
            if lUD < -0.080:
                freecam.actuators["up"].dLoc = [ 0, 0, -camspeed2]
                cont.activate(freecam.actuators["up"])
                #print("fastup")
            else:
                cont.deactivate(freecam.actuators["up"])    
#            #down    
            if lUD > .080:
                freecam.actuators["down"].dLoc = [ 0, 0, camspeed2]
                cont.activate(freecam.actuators["down"])
            else:
                cont.deactivate(freecam.actuators["down"])                    
#            #left
            if lLR < -0.080:
                freecam.actuators["left"].dLoc = [-camspeed2, 0, 0]                
                cont.activate(freecam.actuators["left"])
            else:
                cont.deactivate(freecam.actuators["left"])                    
#            #right
            if lLR > 0.080:         
                freecam.actuators["right"].dLoc = [camspeed2, 0, 0]                
                cont.activate(freecam.actuators["right"])
            else:
                cont.deactivate(freecam.actuators["right"])  
            #up
            if rUD < -0.080:
                freecam.actuators["rotup"].dRot = [camrot2, 0, 0]
                cont.activate(freecam.actuators["rotup"])
            else:
                cont.deactivate(freecam.actuators["rotup"])    
#            #down    
            if rUD > .080:
                freecam.actuators["rotdown"].dRot = [-camrot2, 0, 0]                
                cont.activate(freecam.actuators["rotdown"])
            else:
                cont.deactivate(freecam.actuators["rotdown"])                    
#            #left
            if rLR < -0.080:
                freecam.actuators["rotleft"].dRot = [0, 0, camrot2]                
                cont.activate(freecam.actuators["rotleft"])
            else:
                cont.deactivate(freecam.actuators["rotleft"])                    
#            #right
            if rLR > 0.080:         
                freecam.actuators["rotright"].dRot = [0, 0, -camrot2]
                cont.activate(freecam.actuators["rotright"])
            else:
                cont.deactivate(freecam.actuators["rotright"]) 

#*********************************************                
                
            if lUD > -0.080 and lUD < -0.030:
                freecam.actuators["up"].dLoc = [ 0, 0, -camspeed1]
                cont.activate(freecam.actuators["up"])
                #print(lUD)
            else:
                cont.deactivate(freecam.actuators["up"])    
#            #down    
            if lUD < .080 and lUD > .03:
                freecam.actuators["down"].dLoc = [ 0, 0, camspeed1]                
                cont.activate(freecam.actuators["down"])
            else:
                cont.deactivate(freecam.actuators["down"])                    
#            #left
            if lLR > -0.080 and lLR < -0.030:
                freecam.actuators["left"].dLoc = [-camspeed1, 0, 0]                
                cont.activate(freecam.actuators["left"])
            else:
                cont.deactivate(freecam.actuators["left"])                    
#            #right
            if lLR < .080 and lLR > .03:       
                freecam.actuators["right"].dLoc = [camspeed1, 0, 0]
                cont.activate(freecam.actuators["right"])
            else:
                cont.deactivate(freecam.actuators["right"])  
            #up
            if rUD > -0.080 and rUD < -0.030:
                freecam.actuators["rotup"].dRot = [camrot1, 0, 0]                
                cont.activate(freecam.actuators["rotup"])
            else:
                cont.deactivate(freecam.actuators["rotup"])    
#            #down    
            if rUD < .080 and rUD > .03:
                freecam.actuators["rotdown"].dRot = [-camrot1, 0, 0]                
                cont.activate(freecam.actuators["rotdown"])
            else:
                cont.deactivate(freecam.actuators["rotdown"])                    
#            #left
            if rLR > -0.080 and rLR < -0.030:
                freecam.actuators["rotleft"].dRot = [0, 0, camrot1]
                cont.activate(freecam.actuators["rotleft"])
            else:
                cont.deactivate(freecam.actuators["rotleft"])                    
#            #right
            if rLR < .080 and rLR > .03:         
                freecam.actuators["rotright"].dRot = [0, 0, -camrot1]
                cont.activate(freecam.actuators["rotright"])
            else:
                cont.deactivate(freecam.actuators["rotright"])                                                    

if r_ground.triggered == False:
    own["lF_air_frame"] = own["framenum"]
if r_ground.triggered == True:
    own["lF_ground_frame"] = own["framenum"]   

if own['LAST_GRIND'] == True:
    own['last_grind_frame'] = own['framenum']
if own['LAST_GRIND'] == False and r_ground.triggered and own['jump_timer'] == 0:
    if own['jump_stance'] != 3:
        own['jump_stance'] = 3  

def control_calib():
    #controller calibration test
    scenes = bge.logic.getSceneList()

    controller_calib = [scene for scene in scenes if scene.name=="controller_calib"][0]
    cq1 = controller_calib.objects['q1']
    cq2 = controller_calib.objects['q2']
    cq3 = controller_calib.objects['q3']
    cq4 = controller_calib.objects['q4']
    cq5 = controller_calib.objects['q5']
    cq6 = controller_calib.objects['q6']
    cq7 = controller_calib.objects['q7']
    cq8 = controller_calib.objects['q8']
    if lq1on == 1:
        cq1["q1"] = 1
    else:
        cq1["q1"] = 0    
    if lq2on == 1:
        cq2["q2"] = 1
    else:
        cq2["q2"] = 0  
    if lq3on == 1:
        cq3["q3"] = 1
    else:
        cq3["q3"] = 0    
    if lq4on == 1:
        cq4["q4"] = 1
    else:
        cq4["q4"] = 0
    if lq5on == 1:
        cq5["q5"] = 1
    else:
        cq5["q5"] = 0    
    if lq6on == 1:
        cq6["q6"] = 1
    else:
        cq6["q6"] = 0
    if lq7on == 1:
        cq7["q7"] = 1
    else:
        cq7["q7"] = 0    
    if lq8on == 1:
        cq8["q8"] = 1
    else:
        cq8["q8"] = 0  
def grind_turn():
    jumping = None
    gotcd = 25
    force = [0,0,0]
    grindHit = own['grindTouch']       
    if rUD > turnsens or rLR > turnsens or rUD < -turnsens or rLR < -turnsens:
       jumping = True
    if grindHit == False:
        cont.deactivate(own.actuators['grindoutRight'])
        cont.deactivate(own.actuators['grindoutLeft'])   
    if grindHit == True and jumping == None:
        outloc = 0.022
        bsoutloc = .07
        bsoutvel = .1
        outrot = .02 #0.012
        outrot2 = .24
        outact = own.actuators["grindoutRight"]
        if own['grindpos'] == 'reg_5050':
            if lq3on == 1 or lq2on:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60

                if STANCE == True:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'fak right'                    
                    #outact.dLoc = [0, -outloc, 0]
                    #outact.dRot = [0, 0, -outrot]
                if STANCE == False:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'reg right'                    
                    #outact.dLoc = [0, outloc, 0]
                    #outact.dRot = [0, 0, -outrot]                
                #cont.activate(own.actuators["grindoutRight"])
                own["grindoutturn"] = gotcd    
            if lq7on == 1 or lq8on:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60                
                if STANCE == True:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'fak left'                    
                    #outact.dLoc = [0, outloc, 0]
                    #outact.dRot = [0, 0, outrot]
                if STANCE == False:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'reg left'                    
                    #outact.dLoc = [0, -outloc, 0]
                    #outact.dRot = [0, 0, outrot]                
                #cont.activate(own.actuators["grindoutRight"])
                own["grindoutturn"] = gotcd 
            if lq4on == 1:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60                
                if STANCE == True:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'fak fak right'
                    #outact.dLoc = [0, -outloc, 0]
                    #outact.dRot = [0, 0, outrot2]
                if STANCE == False:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'reg fak right'
                    #outact.dLoc = [0, outloc, 0]
                    #outact.dRot = [0, 0, outrot2]
                #cont.activate(own.actuators["grindoutRight"]) 
                own["grindoutturn"] = gotcd
            if lq6on == 1:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60                
                if STANCE == True:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'fak fak left'
                    #outact.dLoc = [0, outloc, 0]
                    #outact.dRot = [0, 0, -outrot2]
                if STANCE == False:
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'reg fak left'                      
                    #outact.dLoc = [0, -outloc, 0]
                    #outact.dRot = [0, 0, -outrot2]                
                #cont.activate(own.actuators["grindoutRight"]) 
                own["grindoutturn"] = gotcd                
        #use stance for 5050 and grindstance for boards                        
        if own['grindpos'] == 'reg_board':
            outvel = own.getLinearVelocity(1)
            
            
            outact.dLoc = [0, 0, 0]
            outact.dRot = [0, 0, 0]
            if lq5on == 1:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60                 
                if own['grind_stance'] == True:
                    #outact.dLoc = [-bsoutloc, 0, 0]
                    if own['footplant_on'] == True:
                        own.setLinearVelocity([(outvel.x + -bsoutvel), outvel.y, outvel.z], 1)
                        cont.activate(own.actuators["grindoutRight"])                   
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'bs fak back'                     
                    #force = [-40, 0, 0]
                    #own.applyForce(force,1)
                if own['grind_stance'] == False:
                    #outact.dLoc = [bsoutloc, 0, 0]
                    if own['footplant_on'] == True:
                        own.setLinearVelocity([(outvel.x + bsoutvel), outvel.y, outvel.z], 1)
                        cont.activate(own.actuators["grindoutRight"]) 
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'bs reg back'
                    #force = [40, 0, 0]
                    #own.applyForce(force,1)                    
                #cont.activate(own.actuators["grindoutRight"]) 
                own["grindoutturn"] = gotcd 
                own['invert_on'] = 0  
            if lq1on == 1:
                if own['gt_cd2'] == 0:
                    own['gt_cd2'] = 60                 
                if own['grind_stance'] == True:
                    #outact.dLoc = [bsoutloc, 0, 0]
                    #force = [40, 0, 0]
                    #own.applyForce(force,1) 
                    if own['footplant_on'] == True:                   
                        own.setLinearVelocity([(outvel.x + bsoutvel), outvel.y, outvel.z], 1)
                        cont.activate(own.actuators["grindoutRight"])
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'bs fak forward'                                            
                if own['grind_stance'] == False:
                    #outact.dLoc = [-bsoutloc, 0, 0]
                    #force = [-40, 0, 0]
                    #own.applyForce(force,1)
                    if own['footplant_on'] == True:                    
                        own.setLinearVelocity([(outvel.x + -bsoutvel), outvel.y, outvel.z], 1)
                        cont.activate(own.actuators["grindoutRight"])
                    if own['grind_out_type'] == None:
                         own['grind_out_type'] = 'bs reg forward'                                            
                own["grindoutturn"] = gotcd
                own['invert_on'] = 0  
        if lq1on or lq2on or lq3on or lq4on or lq5on or lq6on or lq7on or lq8on:
            gt_cd = own['gt_cd']
            if gt_cd == 0:
                gt_cd = 30
                own['gt_cd'] = gt_cd        
    #else:

        #else:
        if own['grindoutturn'] == 0:    
            cont.deactivate(own.actuators["grindoutRight"])
            own["grindoutturn"] = 0  
        gt_cd = own['gt_cd']
        if gt_cd > 0:
            own['gt_cd'] = gt_cd - 1         
        else:
            own['gt_cd'] = 0 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    reg_move = .05
    reg_rot = 0.01
    reg_rot2 = .26
    reg_move2 = .13
    bsforce = 50
    bs_dloc = .03
    outvel = own.linearVelocity
    if own['gt_cd2'] > 50:
        if own['grind_out_type'] == 'reg right':
            #print("do reg right")
            own.applyMovement([0,reg_move,0], True)
            own.applyRotation([0,0,reg_rot],True)
        if own['grind_out_type'] == 'fak right':
            own.applyMovement([0,-reg_move,0], True)
            own.applyRotation([0,0,-reg_rot],True)
            #print("do fak right") 
        if own['grind_out_type'] == 'reg left':
            #print("do reg left")
            own.applyMovement([0,-reg_move,0], True)
            own.applyRotation([0,0,reg_rot],True)           
        if own['grind_out_type'] == 'fak left':
            own.applyMovement([0,reg_move,0], True)
            own.applyRotation([0,0,-reg_rot],True)
            #print("do fak left") 
        if own['grind_out_type'] == 'reg fak right':
            if own['gt_cd2'] > 55:
                own.applyMovement([0,reg_move2,0], True)
            own.applyRotation([0,0,reg_rot2],True)            
            #print("do reg fak right")
        if own['grind_out_type'] == 'fak fak right':
            if own['gt_cd2'] > 55:
                own.applyMovement([0,-reg_move2,0], True)
            own.applyRotation([0,0,reg_rot2],True)            
            #print("do fak fak right") 
        if own['grind_out_type'] == 'reg fak left':
            if own['gt_cd2'] > 55:
                own.applyMovement([0,-reg_move2,0], True)
            own.applyRotation([0,0,-reg_rot2],True)             
            #print("do reg fak left")                        
        if own['grind_out_type'] == 'fak fak left':
            if own['gt_cd2'] > 55:
                own.applyMovement([0,reg_move2,0], True)
            own.applyRotation([0,0,-reg_rot2],True)            
            #print("do fak fak left")
        if own['grind_out_type'] == 'reg right' or own['grind_out_type'] == 'reg left' or own['grind_out_type'] == 'fak right' or own['grind_out_type'] == 'fak left':   
            own.setLinearVelocity([outvel.x * 1.01, outvel.y, outvel.z], True)
        if own['grind_out_type'] == 'reg fak right' or own['grind_out_type'] == 'reg fak left' or own['grind_out_type'] == 'fak fak right' or own['grind_out_type'] == 'fak fak left':
            if own['gt_cd2'] == 51:
                #print('outforce')
                if STANCE == 0:
                    own.applyForce([-200, 0, 0], True)
                if STANCE == 1:
                    own.applyForce([200, 0, 0], True)
        if own['grind_out_type'] == 'bs reg back' or own['grind_out_type'] == 'bs fak forward':
            if own['gt_cd2'] > 50:
                if STANCE == True:
                    own.applyForce([bsforce, 0, 0], True)
                if STANCE == False:
                    own.applyForce([bsforce, 0, 0], True)
                own.applyMovement([bs_dloc,0,0], True)    
        if own['grind_out_type'] == 'bs fak back' or own['grind_out_type'] == 'bs reg forward':
            if own['gt_cd2'] > 50:
                if STANCE == True:
                    own.applyForce([-bsforce, 0, 0], True)
                if STANCE == False:
                    own.applyForce([-bsforce, 0, 0], True)
                own.applyMovement([-bs_dloc,0,0], True)                                             
                                                       
    #print("setting linvel", own.linearVelocity, outvel)                     
    if own['gt_cd2'] > 0:
        own['gt_cd2'] -= 1
    if own['gt_cd2'] == 0:    
        own['grind_out_type'] = None 
#print(own['grind_out_type'])                       
             
#print(own["gt_cd"])
if own["grindoutturn"] > 0:
    own["grindoutturn"] = own["grindoutturn"] - 1
    
                
def air_height():
    height = own["air_height"]
    if lf_ground == True and r_ground.triggered == False:
        height = 0
    #if     
    
#wallride
def wallride():
    wallride_off = own['wallride_off']
    distance = own.getDistanceTo(gray.hitPosition)
    upforce = 25
    sideforce = 15
    #distance = own["air_height"]
    try:
        obj = gray.hitObject
        objpos = obj.worldPosition
        ownpos = own.worldPosition
        distance = ownpos.z - objpos.z
        #print(distance)
    except:
        pass    
    if wallrideL.triggered and wallride_off == 0 and r_ground.triggered == False:
        #print("wallrideL", distance)
        own['jump_timer'] = 0
        if r_ground.triggered == False:
            own["wallride"] = "L"
            #print(own["wallride"])
            cont.activate(wallrideconstL)
            force = [0,sideforce,upforce]
            own.applyForce(force,1)            
            #own.alignAxisToVect(obj.worldPosition, 1, .9)
            #align
            if STANCE == 0:
                skater.playAction("reg_wall_r", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            else:
                skater.playAction("fak_wall_l", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            deck.playAction("a_reg_wall_r", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            trucks.playAction("a_reg_wall_r", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
    else:
        if own["wallride"] != "R":
            own["wallride"] = None
        cont.deactivate(wallrideconstL) 
        killact(3000)
        killact(3001)
        killact(3002)       
    if wallrideR.triggered and wallride_off == 0:
        own['jump_timer'] = 0
        #print("wallrideR", distance) 
        if r_ground.triggered == False:
            own["wallride"] = "R"
            cont.activate(wallrideconstR)
            force = [0,-sideforce,upforce]
            own.applyForce(force,1)
            #own.alignAxisToVect(obj.worldPosition, 1, .9)
            if STANCE == 0: 
                skater.playAction("reg_wall_l", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            else:
                skater.playAction("fak_wall_r", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            deck.playAction("a_reg_wall_l2", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)
            trucks.playAction("a_reg_wall_l2", 10,10, layer=3000, priority=8, play_mode=1, speed=.5)              
    else:
        if own["wallride"] != "L":
            own["wallride"] = None
        cont.deactivate(wallrideconstR) 
        killact(3003)
        killact(3004)
        killact(3005)   
#    if wallride_col.triggered == True:
#        print("wallride")
#        wallobj = wallride_col.hitObject
#        print(wallobj)
#        xyz = own.worldOrientation.to_euler()
#        rotz = math.degrees(xyz[2])
#        xyz2 = wallobj.worldOrientation.to_euler()
#        rotz2 = math.degrees(xyz2[2])
#        print("prot: ", rotz, "wrot: ", rotz2)
#        try: 
#            zvect = wallobj.getAxisVect( [0.0, 1.0, 0.0]) 
#            print(zvect)
#        except: pass
#        rot = rotz - rotz2 
#        rotation = rot * -1   
#        rotation = [ 0.0, 0, rot]
#        
#        own.applyRotation( rotation, True)    
        #vectTo = obj.getVectTo(wallobj)
        
#        try:
#            if STANCE == 0:
#                own.alignAxisToVect(zvect, 0, .9)
#            if STANCE == 1:
#                own.alignAxisToVect(-zvect, 0, .9) 
#        except: pass                   
#print(wallride_col.triggered)            

def wallride_sound():
    
    sact = own.actuators["wallSound"]
    if own["wallride"] != None:
        sact.volume = .2
        cont.activate(own.actuators["wallSound"])
    else:
        sact.volume = .001
        sact.stopSound()
if own['revert_timer'] > 0:
    own['revert_timer'] = own['revert_timer'] - 1 
    
              
    
def shutoff_timers():
    #print(wallride)
    if (LAST_GRIND == False and grindHit == True) or (jump_timer > 10 and own['wallride'] == None):
        own["Q1oncd"] = 0
        own["Q2oncd"] = 0
        own["Q3oncd"] = 0
        own["Q4oncd"] = 0
        own["Q5oncd"] = 0
        own["Q6oncd"] = 0
        own["Q7oncd"] = 0
        own["Q8oncd"] = 0  
def grindout_cleanup():             
    lgf = own['last_grind_frame']
    if (frame - lgf) == 20:               
        #print("kill grindout anims")
        killact(200)
        #killact(200)
        #killact(200)
    if skater.isPlayingAction(fliplay):    
        #print("flipping")      
        killact(700)
        #killact(700)
        #killact(700)
        killact(200)
        #killact(200)
        #Ekillact(200)    
def trans_jump():
    if own['jump_from_trans'] == 1:
        ground_ray = cont.sensors['ground_look']                        
        #print('align transjump', own['trans_jump_obj'])
        jump_obj = own['trans_jump_obj']
        jump_obj = scene.objects[str(own['trans_jump_obj'])]
        #print(jump_obj)
        worldVect = [1, 0, 0]
        vect = jump_obj.getAxisVect(worldVect)      
        go = jump_obj.worldOrientation
        grinder_axis = [0,1,0]
        player_pos = own.worldPosition
        jump_obj = jump_obj.worldPosition
        try: 
            delta = player_pos - jump_obj
        except:
            #print("delta broke: ", player_pos, grinder_pos)
            pass 
        delta = delta.cross(vect) 
        deltamove = delta[1] * .25
        move = [deltamove, 0, 0]
        #print(deltamove)
        if abs(deltamove) < 1 and delta[1] < 1:
            own.applyMovement(move, True)        
        #print(deltamove, delta, "delta.......")       
        #pos = ground_ray.hitPosition 
        #print(pos)
        
        #linvelloc6 = own.getLinearVelocity(True)
        #xvel6 = linvelloc6.x * .95
        #force = (xvel6, linvelloc6.y, linvelloc6.z)
        #own.setLinearVelocity(force, True)        
    
        
        
        
#control_calib() #scene must be enabled in main                 
jump_Timer()
check_landing()
#SWAG()

#isplaying()
nextframe()
wheelroll()
rollsound()
reset_pos()
ylimit()
getoffboard()
#switchcam()
move_flycam()
move_followcam()
grind_turn()
air_height()
wallride()
wallride_sound()
shutoff_timers()
grindout_cleanup()
#trans_jump()


#printplaying()
#transmult()
linvelx = own.getLinearVelocity(True)
#own["LAST_LEFT"] = LAST_LEFT
#end
#print(linvelx)
own["linvelx"] = linvelx.x
LAST_STANCE = STANCE
LAST_STANCE = own["stance"]
own["last_stance"] = STANCE
own["lastGrab"] = GRAB_ON
own['ground'] = r_ground.triggered
own['last_ground'] = r_ground.triggered
own["LAST_GRIND"] = grindHit
own["rotz"] = rot.z
own['walk'] = 0
own['lasty'] = yBut
own['lastlts'] = ltsBut
own['lastrts'] = rtsBut
own["lF_ground2"] = own["lF_ground"]
own['last_invert'] = invert_on
own['lastbkBut'] = bkBut
own['grab_type'] = grab_type

own['last_last_manual'] = own['last_manual']
own['last_manual'] = own['manual']
own['last_reg_manual'] = own['reg_manual']     
own['last_fak_manual'] = own['fak_manual']
own['last_fak_nmanual'] = own['fak_nmanual'] 
own['last_reg_nmanual'] = own['reg_nmanual']
if own['manual'] == 1:
    own['last_manual_frame'] = frame


#print(own['hippy'], own['last_hippy'])
own['last_hippy'] = own['hippy']
#last pressed down frame
if aBut == 1 and own["lasta"] == 0:
    own["lastaf"] = frame
if xBut == 1 and own["lastx"] == 0:
    own["lastxf"] = frame
own["lasta"] = aBut
own["lastx"] = xBut
own['lastaBut_ground'] = aBut_ground
own['lastxBut_ground'] = xBut_ground
own["last_sel"] = own["sel"]
own["sel"] = bkBut  

#linVelocity = own.getLinearVelocity(1)
#print(linVelocity.z)
#newz = linVelocity.z * .9
if r_ground.triggered and own["jump_timer"] < 20:
    force2 = [0.0, 0, -10]
    own.applyForce(force2, True)
    #own.linearVelocity = [ linVelocity.x, linVelocity.y, newz]
#print(c_ground.triggered, r_ground.triggered, gray.hitPosition[2])
#if c_ground.triggered and r_ground.triggered == False:
#    print("AAAAAAAAAAAAAAlign")
#print("og - new = ", vely)
#print(r_ground.triggered)
#spawn_pos = own['spawn_pos']
#print(lUD)
#.04 to .05
#print("- ",spawn_pos.x, spawn_pos.y, spawn_pos.z)
#printplaying()
#print("-", udPad, ddPad)
#print(own["stance"])
#own["LAST_LEFT"] = LAST_LEFT
#end
#print(rLR)
#print(r_ground.triggered)
#print(own['hippy'], own['last_hippy'])

#print("x: ", round(linvelx.x, 2), "y: ", round(linvelx.y, 2))

