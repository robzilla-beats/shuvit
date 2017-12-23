os = 'Windows'
from sys import platform
if platform != "win32":
 os = 'Linux'
def onWindows():
 return os == 'Windows'
import bge
import GameLogic
import ctypes
#import bpy
import random

#build global dict (move this to separate script that runs once)
scene = bge.logic.getCurrentScene()
objList = scene.objects

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


cont = GameLogic.getCurrentController() 
obj = bge.logic.getCurrentScene().objects
char = bge.constraints.getCharacter
own = cont.owner
stance = own['stance']
STANCE = own['stance']
r_ground = cont.sensors["r_Ground"]
#Sensor logic bricks connected to the python Controller  
aXis = cont.sensors["sControla.001"]
bUtt = cont.sensors["sControlb.001"]
linvel = own.getLinearVelocity(True)
lasta = own['lasta']
lastx = own['lastx']
last_sit = own['sit']

try:
    own['walk_timer'] = own['walk_timer'] +1
except:
    own['walk_timer'] = 1

truckon = 30
deckon = 30

onW = onWindows()

# windows stuff
lar_lts = 0
uad_lts = 1
lt = 4 if onW else 2
lar_rts = 2 if onW else 3
uad_rts = 3 if onW else 4
rt = 5

a_but = 0 if onW else 0
b_but = 1 if onW else 1
x_but = 2 if onW else 2
y_but = 3 if onW else 3
l_bump = 9 if onW else 4
r_bump = 10 if onW else 5
bk_but = 4 if onW else 6
st_but = 6 if onW else 7
xb_but = 5 if onW else 8
lts_pr = 7 if onW else 9
rts_pr = 8 if onW else 10
l_dp = 13 if onW else 11
r_dp = 14 if onW else 12
u_dp = 11 if onW else 13
d_dp = 12 if onW else 14

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

#user
sens = .04
fliplay = 30
dropinCol = own.sensors['dropinCol']

#no input
def cutOff():
    
 if (abs(lLR) < axisTh 
     and abs(lUD) < axisTh 
     and abs(rLR) < axisTh 
     and abs(rUD) < axisTh
     and aBut == False):
         
  return True
skater = scene.objects["Char4"]
deck = scene.objects["deck"]
trucks = scene.objects["trucks"]

throw_deck_empty = scene.objects["throw_deck_empty"]
wheel1 = scene.objects["rollen.000"]
wheel2 = scene.objects["rollen.001"]
wheel3 = scene.objects["rollen.002"]
wheel4 = scene.objects["rollen.003"]
camobj = scene.objects["Camera.003"]
camera = cont.actuators["Camera"]
replayCam = cont.actuators["replayCam"]
timer = own['dropinTimer']
cam = scene.objects["Camera.003"]
freecam = scene.objects["freecam"]
followcam = scene.objects["followcam"]

noidle = 0

playing_deck = deck.isPlayingAction(deckon)
playing_trucks = trucks.isPlayingAction(truckon)
if playing_deck == 1 or playing_trucks == 1:
    noidle = 1

if own["stance"] == None:
    own["stance"] = True
STANCE = own["stance"]
def killact(layer):
    if skater.isPlayingAction(layer):
        skater.stopAction(layer)
    if deck.isPlayingAction(layer):    
        deck.stopAction(layer)
    if trucks.isPlayingAction(layer):    
        trucks.stopAction(layer)
def killall():
    for x in range(5000):
        skater.stopAction(x)
        deck.stopAction(x)
        trucks.stopAction(x)
def trucksisplaying():
    for x in range(5000):
        if deck.isPlayingAction(x):
            print("deck is playing:", x)
#trucksisplaying() 

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
#printplaying() 
##
if r_ground.positive and xBut == False and lastx == False:
    killact(10)
    #killact(11)
    killact(12)
    killact(13)              
######################################  
#walk out
#print(own['walk_timer'])
#if own['walk_timer'] < 5:
#    
#    if stance == 0 and skater.isPlayingAction(fliplay) == False:
#        
#        if own['throw_deck'] == True:
#            print("walk out1")
#            skater.playAction("reg_nwalk_nb.001", 15,35, layer=29, play_mode=0, speed=.5)
#        else:
#            print("walk out2")
#            skater.playAction("walk.000", 15,35, layer=29, play_mode=0, speed=.5)
#        deck.playAction("a_reg_walk", 0,35, layer=17, play_mode=0)
#        trucks.playAction("a_reg_walk", 0,35, layer=17, play_mode=0)    
    

#idle      
if stance == 0 and skater.isPlayingAction(fliplay) == False and yBut == False and r_ground.triggered and xBut == False and noidle == 0 and own['walk_idling'] == 0 and own['sit'] == 0:
    own['requestAction'] = 'reg_idle'
    if own['throw_deck'] == True:
        own['requestAction'] = 'reg_idle_nb'
        skater.playAction("reg_idle1", 1,120, layer=3, play_mode=1, speed=.5)
    else:
        #cont.activate(skater.actuators['aRest'])
        skater.playAction("reg_idle1", 1,120, layer=3, play_mode=1, speed=.5)
        deck.playAction("a_reg_idle1", 1,120, layer=3, play_mode=1, speed=.5)
        trucks.playAction("a_reg_idle1", 1,120, layer=3, play_mode=1, speed=.5) 
if stance == 1 and skater.isPlayingAction(fliplay) == False and yBut == False and r_ground.triggered and xBut == False and noidle == 0 and own['walk_idling'] == 0 and own['sit'] == 0:
    own['requestAction'] = 'fak_idle'
    if own['throw_deck'] == True:
        own['requestAction'] = 'fak_idle_nb'
        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=1, speed=.5)
    else:
        #cont.activate(skater.actuators['aRest'])
        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=1, speed=.5)
        deck.playAction("a_fak_idle1", 1,120, layer=3, play_mode=1, speed=.5)
        trucks.playAction("a_fak_idle1", 1,120, layer=3, play_mode=1, speed=.5) 

if lUD < -sens:
    lup = 1
else:
    lup = 0
if lUD > sens:
    ldown = 1
else:
    ldown = 0    
    
#walking

#new walking
#if (lup == 1 and aBut == 0 and yBut == False and (r_ground.positive or own['stair_counter'] > 0) and xBut == 0):
vel = own.getLinearVelocity(True)
if own['walk_timer'] < 50:
    velx = vel.x * .95             
    own.setLinearVelocity([velx, 0, vel.z], True)
else:
    own.setLinearVelocity([0, 0, vel.z], True)
    #print("set 0 vel")
    
if (lup == 1 and aBut == 0 and (r_ground.positive or own['stair_counter'] > 0) and xBut == 0):    
    own['walking'] = "regular"
    walking = "regular"
elif lup == 1 and aBut == 1 and yBut == False and (r_ground.positive or own['stair_counter'] > 0) and xBut == 0:
    own['walking'] = "fast"
    walking = "fast"
else:
    own['walking'] = None
    walking = None
#print(own['walk_timer'])    
if walking == "regular":
    cont.deactivate(own.actuators['forward2']) 
    cont.deactivate(own.actuators['backward2'])    
    if stance == 0:
        cont.activate(own.actuators['forward'])
    else:
        cont.activate(own.actuators['backward'])
if walking == "fast":
    cont.deactivate(own.actuators['forward']) 
    cont.deactivate(own.actuators['backward'])    
    if stance == 0:
        cont.activate(own.actuators['forward2'])
    else:
        cont.activate(own.actuators['backward2'])            
        

if walking == None:
    cont.deactivate(own.actuators['forward2']) 
    cont.deactivate(own.actuators['backward2'])
    cont.deactivate(own.actuators['forward']) 
    cont.deactivate(own.actuators['backward'])        
    if own['walk_timer'] < 50:
        velx = vel.x * .95             
        own.setLinearVelocity([velx, 0, vel.z], True)
    else:
        own.setLinearVelocity([0, 0, vel.z], True)
        #print("set 0 vel")    
                
    
#old walking
if (lup == 1 and aBut == 0 and yBut == False and (r_ground.positive or own['stair_counter'] > 0) and xBut == 0):
    own.actuators["walkondirt"].volume = .2
    own.actuators["walkondirt"].pitch = 1
    cont.activate(own.actuators["walkondirt"])
    if lasta == 1:
        #cont.deactivate(own.actuators['forward2']) 
        #cont.deactivate(own.actuators['backward2'])
        killact(6)
        killact(7)
        killact(8)
        killact(9)
        killact(17)
        killact(18)                
    if stance == 0 and skater.isPlayingAction(fliplay) == False:             
        #cont.activate(own.actuators['forward'])
        #cont.activate(skater.actuators['aWalk'])
        #cont.activate(deck.actuators['a_reg_walk'])
        #cont.activate(deck.actuators['a_reg_walk'])
        #without deck
        if own['throw_deck'] == True:
            own['requestAction'] = 'reg_walk_nb'
            #skater.playAction("reg_nwalk_nb.001", 0,35, layer=24, play_mode=1, speed=.5)
        else:
            own['requestAction'] = 'reg_walk'
#            skater.playAction("reg_nwalk", 0,35, layer=24, play_mode=1, speed=.5)
#        deck.playAction("a_reg_nwalk", 0,35, layer=16, play_mode=1, speed=.5)
#        trucks.playAction("a_reg_nwalk", 0,35, layer=16, play_mode=1, speed=.5)
        killact(25) 
        killact(305)
        killact(306)                
    if stance == 1 and skater.isPlayingAction(fliplay) == False:        
        #cont.activate(own.actuators['backward'])
        #cont.activate(skater.actuators['aWalk_fak'])
        #cont.activate(deck.actuators['a_fak_walk'])
        #cont.activate(trucks.actuators['a_fak_walk'])
        #without deck
        if own['throw_deck'] == True:
            own['requestAction'] = 'fak_walk_nb'
            #skater.playAction("fak_nwalk_nb.001", 0,35, layer=25, play_mode=1, speed=.5)
        else:
            own['requestAction'] = 'fak_walk'
#            skater.playAction("fak_nwalk", 0,35, layer=25, play_mode=1, speed=.5)    
#        deck.playAction("a_fak_nwalk", 0,35, layer=15, play_mode=1, speed=.5)
#        trucks.playAction("a_fak_nwalk", 0,35, layer=15, play_mode=1, speed=.5)        
elif lup == 1 and aBut == 1 and yBut == False and (r_ground.positive or own['stair_counter'] > 0) and xBut == 0:
    own.actuators["walkondirt"].volume = .2
    own.actuators["walkondirt"].pitch = 1.3
    cont.activate(own.actuators["walkondirt"])
    if stance == 0 and skater.isPlayingAction(fliplay) == False:        
        #cont.activate(own.actuators['forward2'])
        #cont.activate(skater.actuators['aWalk'])
        if own['throw_deck'] == True:
            own['requestAction'] = 'reg_walkFast_nb'
            skater.playAction("reg_nwalk_nb.001", 0,35, layer=25, play_mode=1, speed=1)
        else:
            own['requestAction'] = 'reg_walkFast'
#            skater.playAction("reg_nwalk", 0,35, layer=25, play_mode=1, speed=1)         
#        
#        deck.playAction("a_reg_nwalk", 0,35, layer=305, play_mode=1, speed=1)
#        trucks.playAction("a_reg_nwalk", 0,35, layer=306, play_mode=1, speed=1)
    else:
        killact(25) 
        killact(305)
        killact(306)           
    if stance == 1 and skater.isPlayingAction(fliplay) == False:        
        #cont.activate(own.actuators['backward2'])
        #cont.activate(skater.actuators['aWalk_fak'])
        if own['throw_deck'] == True:
            own['requestAction'] = 'fak_walkFast_nb'
            skater.playAction("fak_nwalk_nb.001", 0,35, layer=24, play_mode=1, speed=1)           
        else:
            own['requestAction'] = 'fak_walkFast'
#            skater.playAction("fak_nwalk", 0,35, layer=24, play_mode=1, speed=1)                       
#        deck.playAction("a_fak_nwalk", 0,35, layer=15, play_mode=1, speed=1)
#        trucks.playAction("a_fak_nwalk", 0,35, layer=15, play_mode=1, speed=1)             
else:
    vel = own.getLinearVelocity(True)
    cont.deactivate(own.actuators["walkondirt"])
    if stance == 0:
        #cont.deactivate(own.actuators['forward'])
        #cont.deactivate(own.actuators['forward2'])
        cont.deactivate(skater.actuators['aWalk'])
        cont.deactivate(deck.actuators['a_reg_walk'])
        cont.deactivate(trucks.actuators['a_reg_walk'])        
        killact(4)
        killact(5)
        killact(6)
        killact(7)
        killact(15)
        killact(16)
        killact(17)
        killact(18)
        killact(24)
        killact(25) 
        killact(305)
        killact(306)         
#        if own['walk_timer'] < 50:
#            velx = vel.x * .95             
#            #own.setLinearVelocity([velx, 0, vel.z], True)
#            
#        else:
#            if r_ground.triggered:
#                own.setLinearVelocity([0, 0, vel.z], True)
#            #velz = vel.z
#            #print(velz)
#            #own.localLinearVelocity[0, 0, velz]
    if stance == 1:
        #cont.deactivate(own.actuators['backward'])
        #cont.deactivate(own.actuators['backward2'])
        cont.deactivate(skater.actuators['aWalk_fak'])
        cont.deactivate(deck.actuators['a_fak_walk'])
        cont.deactivate(trucks.actuators['a_fak_walk'])        
        killact(4)
        killact(5)
        killact(6)
        killact(7)
        killact(15)
        killact(16)
        killact(17)
        killact(18)
        killact(24)
        killact(25) 
        killact(305)
        killact(306)             
#        if own['walk_timer'] < 50:
#            velx = vel.x * .95             
#            #own.setLinearVelocity([velx, 0, vel.z], True)
#        else:
#            own.setLinearVelocity([0, 0, vel.z], True)
#in air        
if lup == 1 and r_ground.positive == False:
    
    if stance == 0:
        cont.deactivate(own.actuators['forward'])
        cont.deactivate(own.actuators['forward2'])
        cont.deactivate(skater.actuators['aWalk'])
        killact(4)
        killact(5)
        killact(6)
        killact(7)        
        velx = linvel.x - 1
        own.setLinearVelocity([-1.5, linvel.y, linvel.z], 1)
        #cont.activate(own.actuators['forward2'])
    if stance == 1:    
        cont.deactivate(own.actuators['backward'])
        cont.deactivate(own.actuators['backward2'])
        cont.deactivate(skater.actuators['aWalk_fak'])
        killact(4)
        killact(5)
        killact(6)
        killact(7)        
        velx = linvel.x + 1
        own.setLinearVelocity([1.5, linvel.y, linvel.z], 1) 
        #cont.activate(own.actuators['backward2'])       
#---------------
if rLR > .05:
    cont.activate(camobj.actuators['camRight'])
else:
    cont.deactivate(camobj.actuators['camRight'])    
if rLR < -.05:
    cont.activate(camobj.actuators['camLeft'])
else:
    cont.deactivate(camobj.actuators['camLeft'])     
if rUD > .05:
    cont.activate(camobj.actuators['camDown'])
else:
    cont.deactivate(camobj.actuators['camDown'])     
if rUD < -.05:
    cont.activate(camobj.actuators['camUp'])
else:
    cont.deactivate(camobj.actuators['camUp'])     
                
#----------------
camera.height = .9 #-.4
camera.min = 1.5
camera.max = 2
#camera.object = "Char4:Mhair01"
#camera.damping = 0
#camera.axis = 4 
lasty = own['lasty']     
#if yBut == False and lasty == True:

#    if own['walk'] == 1: 
#        killact(fliplay) 
        #killall() 
    #camera.damping = 0     
    #camera.axis = 4            
#print(stance)


def onboard():
#    pass
    if own['walk'] == 0:
        print("start walking")
        if own['framenum'] > 100 and own['fall'] == False:
            #pass
            cont.activate(own.actuators['pop'])
        own['getoffboard'] = False
        #set_vibration(0, 0.0, 0.0)
        fliplay = 301
        fliplay2 = 302 
        fliplay3 = 303
        try:
            vel = own['offboard_vel']
            #velx = vel.x *2
            vel = [velx, vel.y, vel.z]
            #vel = vel * 4
            #vel = [-100, 0, 0]
            #print(vel)
            #own.localLinearVelocity = vel
            #JUMPHEIGHT = 1100
            #force = [600, 0.0, 10]
            # use local axis
            #local = True
            # apply force
            #own.applyForce(force, local)            
        except: 
            pass
         
        if STANCE == 0:
            #killact(3)
            #killact(4)
            killall()
            skater.stopAction(fliplay)
            deck.stopAction(deckon)
            trucks.stopAction(truckon)             
#            skater.playAction("nreg_offboard", 1,30, layer=fliplay, priority=0, play_mode=0, speed=1.5)
#            deck.playAction("a_reg_offboard", 1,30, layer=deckon, priority=0, play_mode=0, speed=1.5)
#            trucks.playAction("c_reg_offboard", 1,30, layer=truckon, priority=0, play_mode=0, speed=1.5)
            skater.playAction("reg_noffboard", 0,26, layer=fliplay, priority=0, play_mode=0, speed=.5)
            deck.playAction("a_reg_noffboard", 0,26, layer=deckon, priority=0, play_mode=0, speed=.5)
            trucks.playAction("a_reg_noffboard", 0,26, layer=truckon, priority=0, play_mode=0, speed=.5)            
        if STANCE == 1:
            killact(3)
            killact(4)
            killall()
            skater.stopAction(fliplay)
            deck.stopAction(deckon)
            trucks.stopAction(truckon)             
            skater.playAction("nfak_offboard", 1,30, layer=fliplay, priority=0, play_mode=0, speed=1.5)
            deck.playAction("a_fak_offboard", 1,30, layer=deckon, priority=0, play_mode=0, speed=1.5)
            trucks.playAction("a_fak_offboard", 1,30, layer=truckon, priority=0, play_mode=0, speed=1.5)             
def jump():
    if xBut == True:
        if own['lastx'] == 0:
            killact(3)
            killact(4)
            killact(5)
            killact(6)
            killact(7) 
            #why does this layer have to be so high?      
            if STANCE == 0:  
                own['requestAction'] ='reg_jump'   
#                skater.playAction("reg_jump", 1,35, layer=400, priority=0, play_mode=0, speed=.5)
#                deck.playAction("a_reg_jump2", 1,35, layer=400, priority=0, play_mode=0, speed=.5)
#                trucks.playAction("a_reg_jump2", 1,35, layer=400, priority=0, play_mode=0, speed=.5)
            if STANCE == 1:
                own['requestAction'] ='fak_jump'
                #skater.playAction("fak_jump", 1,35, layer=400, priority=0, play_mode=0, speed=.5)    
            #deck.playAction("a_reg_jump", 1,30, layer=11, play_mode=0, speed=.5)
            #trucks.playAction("a_reg_jump", 1,30, layer=12, priority=0, play_mode=0, speed=1)             
            JUMPHEIGHT = 1100
            force = [ 0.0, 0.0, JUMPHEIGHT]
            # use local axis
            local = False
            # apply force
            own.applyForce(force, local)
        own['lastx'] = 1
    else:
        own['lastx'] = 0
def dropin():
    if dropinCol.positive == True:
        #print("DROPIN") 
        pass       
        
def getonboard():
    getonboard = own['getonboard']
    fliplay2 = 50#8560
    if yBut == True:
        #camera.height = -.4
        #camera.min = 1.5
        #camera.max = 2 #2
        #camera.damping = .99
        #camera.axis = 0
        
        #cont.deactivate(cam.actuators['replayCam'])
        #cont.deactivate(cam.actuators['Camera'])
        #camera.height = 10 #-.5
        #print("high cam")
        #camera.min = .75
        #camera.max = 1.25
        #cont.activate(cam.actuators['Camera']) 
        
        deckact = deck.actuators["Visibility"]
        trucksact = trucks.actuators["Visibility"]
        wheel1act = wheel1.actuators["Visibility"]
        wheel2act = wheel2.actuators["Visibility"]
        wheel3act = wheel3.actuators["Visibility"]
        wheel4act = wheel4.actuators["Visibility"]        
        deckact.visibility = True
        trucksact.visibility = True
        wheel1act.visibility = True
        wheel2act.visibility = True
        wheel3act.visibility = True
        wheel4act.visibility = True  
        cont.activate(deck.actuators['Visibility'])
        cont.activate(trucks.actuators['Visibility'])
        cont.activate(wheel1.actuators['Visibility'])
        cont.activate(wheel2.actuators['Visibility'])
        cont.activate(wheel3.actuators['Visibility'])
        cont.activate(wheel4.actuators['Visibility']) 
        own['throw_deck'] = False 
        throw_deck_empty = scene.objects["throw_deck_empty"]
        throw_deck_empty['kill_deck'] = 1 
        fliplay3 = fliplay2 + 1  
        if STANCE == 0 and dropinCol.positive == True: 
            cont.deactivate(skater.actuators['aRest'])
            cont.deactivate(skater.actuators['aRest_fak'])
            killact(4)
            killact(5)
            killact(6)
            killact(7)                        
            skater.playAction("nreg_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            deck.playAction("a_reg_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            trucks.playAction("a_reg_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            if lasty == False:
                skater.playAction("nreg_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                deck.playAction("a_reg_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                trucks.playAction("a_reg_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)                
                
        if STANCE == 1 and dropinCol.positive == True: 
            cont.deactivate(skater.actuators['aRest'])
            cont.deactivate(skater.actuators['aRest_fak'])
            killact(4)
            killact(5)
            killact(6)
            killact(7)                        
            skater.playAction("nfak_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            deck.playAction("a_fak_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            trucks.playAction("a_fak_dropin", 50,60, layer=fliplay2, priority=0, play_mode=1, speed=.5)
            if lasty == False:
                skater.playAction("nfak_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                deck.playAction("a_fak_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)
                trucks.playAction("a_fak_dropin", 30,50, layer=fliplay3, priority=0, play_mode=0, speed=.75)                      
    if getonboard == 1:
        fliplay3 = 6000 
        onboard_speed = .1   
#        if STANCE == 1:
#            skater.playAction("nfak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)
#            deck.playAction("a_fak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)
#            trucks.playAction("a_fak_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)
#        if STANCE == 0:
#            skater.playAction("nreg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)
#            deck.playAction("a_reg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)
#            trucks.playAction("a_reg_dropin", 60,80, layer=fliplay3, priority=0, play_mode=0, speed=onboard_speed)                                    
        own['getonboard'] = 0 
    if yBut == False and lasty == True:
        own['getonboard'] = 1
        #camera.height = -.5
        #camera.min = .75
        #camera.max = 1.25         

def nextframe():
    framenumber = own["framenum"]
    framenumber = framenumber + 1
    if framenumber == 900000:
        framenumber = 0
    own["framenum"] = framenumber
    own['last_walk_frame'] = framenumber
            
def checkidle():
    idle = cont.sensors["idle"]
    #print(idle.positive)
    idle_frame = own["walk_idle_frame"]
    if idle.positive:
        own["walk_idle_frame"] = 0
        cont.deactivate(camobj.actuators['idle_camRight'])  
        camera.height = .5
    else: 
        if idle_frame == 0:
            own["walk_idle_frame"] = own["framenum"] 
        diff = own["framenum"] - idle_frame
        
        if (diff > 700 and idle_frame != 0 and dropinCol.positive == False and own['walk'] != 0) or own['sit'] == 1:
            #print("you are idle", diff)  
            cont.activate(camobj.actuators['idle_camRight'])  
            camera.height = .9   
            camera.min = 2
            camera.max = 2.50
            own['walk_idling'] = 1
        else:
            own['walk_idling'] = 0    
            
def idle_anim():
    if own['walk_idling'] == 1 and own['sit'] == 0:
        walk_idle_frame = own['walk_idle_frame']
        #print("walk_idling")
        mod_num = (own["framenum"] - walk_idle_frame) % 240
        #print(walk_idle_frame, mod_num)
        #killact(3)
        if mod_num == 0:
            if own['idle_skipper'] > 0:
               own['idle_skipper'] -= 1 
            ran_num = random.randint(1, 8)
            #print(ran_num, "modding")
            if own['last_idle_num'] == ran_num:
                ran_num = 1
            if own['idle_skipper'] == 0:
                own['last_idle_num'] = ran_num
                if ran_num == 1 or ran_num > 7:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle1", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                                                                           
                elif ran_num == 2:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle2_", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle2", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle2", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle2_nb", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle1", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle1", 1,120, layer=3, play_mode=0, speed=.5)  
                elif ran_num == 3:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle3", 1,240, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle3", 1,240, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle3", 1,240, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle3", 1,240, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle1", 1,240, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle1", 1,240, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle1", 1,240, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle1", 1,240, layer=3, play_mode=0, speed=.5)
                    own['idle_skipper'] = 2 
                elif ran_num == 4:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle4", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle4", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle4", 1,120, layer=3, play_mode=0, speed=.5) 
                elif ran_num == 5:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle5", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle5", 1,120, layer=3, play_mode=0, speed=.5)
                elif ran_num == 6:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle6", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle6", 1,120, layer=3, play_mode=0, speed=.5) 
                elif ran_num == 7:    
                    killact(3)
                    if STANCE == 0 and own['throw_deck'] == 0:
                        skater.playAction("reg_idle7", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_reg_idle7", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_reg_idle7", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 0 and own['throw_deck'] == 1:
                        skater.playAction("reg_idle7", 1,120, layer=3, play_mode=0, speed=.5)
                    elif STANCE == 1 and own['throw_deck'] == 0:
                        skater.playAction("fak_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        deck.playAction("a_fak_idle6", 1,120, layer=3, play_mode=0, speed=.5)
                        trucks.playAction("a_fak_idle6", 1,120, layer=3, play_mode=0, speed=.5) 
                    elif STANCE == 1 and own['throw_deck'] == 1:
                        skater.playAction("fak_idle6", 1,120, layer=3, play_mode=0, speed=.5)                                                                                                                 
        #deck.playAction("a_reg_idle1", 1,120, layer=3, play_mode=1)
        #trucks.playAction("a_reg_idle1", 1,120, layer=3, play_mode=1) 
                

def reset_pos():
    #reset
    if ddPad == 1:
        
        spawn_pos = own['spawn_pos']
        spawn_rot = own['spawn_rot']
        spawnz = spawn_pos[2] + .1
        try:
            own.worldPosition = (spawn_pos[0], spawn_pos[1], spawnz)
            own.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
        except:    
            own.worldPosition = (0, 0, .1)
            own.worldOrientation = [[1.0, 0.0, 0.0], [ 0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]    
        if own["spawn_stance"] == 1:
            own.setLinearVelocity([.1,0,0], 1)
            #cam.worldPosition = (spawn_pos[0], spawn_pos[1], (spawn_pos[2] + .25))
            #lx = cam.localPosition[1] 
            #lx = lx - 4
            #cam.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
            #cam.localPosition[1] = lx
         
        else: 
            own.setLinearVelocity([-.1,0,0], 1)         
            #cam.worldPosition = (spawn_pos[0], spawn_pos[1], (spawn_pos[2] + .25))
            #lx = cam.localPosition[1]
            #lx = lx - 4
            #cam.worldOrientation = [[spawn_rot[0][0],spawn_rot[0][1],spawn_rot[0][2]], [spawn_rot[1][0],spawn_rot[1][1],spawn_rot[1][2]], [0.0, 0.0, 1.0]]
            #cam.localPosition[1] = lx
    if udPad == 1:
        own['spawn_pos'] = [own.worldPosition[0], own.worldPosition[1], own.worldPosition[2]] 
        own['spawn_rot'] = [[own.worldOrientation[0][0],own.worldOrientation[0][1],own.worldOrientation[0][2]], [own.worldOrientation[1][0],own.worldOrientation[1][1],own.worldOrientation[1][2]], own.worldOrientation[2][2]]
        stance = own["stance"]
        own["spawn_stance"] = stance    
def falldeck():
    #print("falldeck")
    throw_deck_empty = scene.objects["throw_deck_empty"]
    deckact = deck.actuators["Visibility"]
    trucksact = trucks.actuators["Visibility"]
    wheel1act = wheel1.actuators["Visibility"]
    wheel2act = wheel2.actuators["Visibility"]
    wheel3act = wheel3.actuators["Visibility"]
    wheel4act = wheel4.actuators["Visibility"]
            
    if own['throw_deck'] == False:
        own['throw_deck'] = True
        deckact.visibility = False
        trucksact.visibility = False
        wheel1act.visibility = False
        wheel2act.visibility = False
        wheel3act.visibility = False
        wheel4act.visibility = False
        act = throw_deck_empty.actuators['throw_dec_act']
        if STANCE == True:
            #skater.playAction("fak_throw", 10,30, layer=29, priority=0, play_mode=0, speed=.5)
            act.linearVelocity = [0.0, 1.0, 1.0]
        if STANCE == False:
            #skater.playAction("reg_throw", 10,30, layer=29, priority=0, play_mode=0, speed=.5)  
            act.linearVelocity = [0.0, 1.0, -1.0]  
        cont.activate(act)
    else:
        own['throw_deck'] = False    
        deckact.visibility = True
        trucksact.visibility = True
        wheel1act.visibility = True
        wheel2act.visibility = True
        wheel3act.visibility = True
        wheel4act.visibility = True
        throw_deck_empty['kill_deck'] = 1 
        #print("trying to kill deck")     
    cont.activate(deck.actuators['Visibility'])
    cont.activate(trucks.actuators['Visibility'])
    cont.activate(wheel1.actuators['Visibility'])
    cont.activate(wheel2.actuators['Visibility'])
    cont.activate(wheel3.actuators['Visibility'])
    cont.activate(wheel4.actuators['Visibility']) 

def throwdeck():
    throw_deck_empty = scene.objects["throw_deck_empty"]
    deckact = deck.actuators["Visibility"]
    trucksact = trucks.actuators["Visibility"]
    wheel1act = wheel1.actuators["Visibility"]
    wheel2act = wheel2.actuators["Visibility"]
    wheel3act = wheel3.actuators["Visibility"]
    wheel4act = wheel4.actuators["Visibility"]
            
    if own['throw_deck'] == False:
        own['throw_deck'] = True
        deckact.visibility = False
        trucksact.visibility = False
        wheel1act.visibility = False
        wheel2act.visibility = False
        wheel3act.visibility = False
        wheel4act.visibility = False
        act = throw_deck_empty.actuators['throw_dec_act']
        if STANCE == True:
            skater.playAction("fak_throw", 10,30, layer=29, priority=0, play_mode=0, speed=.5)
            act.linearVelocity = [0.0, 5.0, 5.0]
        if STANCE == False:
            skater.playAction("reg_throw", 10,30, layer=29, priority=0, play_mode=0, speed=.5)  
            act.linearVelocity = [0.0, 5.0, -5.0]  
        cont.activate(act)
    else:
        own['throw_deck'] = False    
        deckact.visibility = True
        trucksact.visibility = True
        wheel1act.visibility = True
        wheel2act.visibility = True
        wheel3act.visibility = True
        wheel4act.visibility = True
        throw_deck_empty['kill_deck'] = 1 
        #print("trying to kill deck")     
    cont.activate(deck.actuators['Visibility'])
    cont.activate(trucks.actuators['Visibility'])
    cont.activate(wheel1.actuators['Visibility'])
    cont.activate(wheel2.actuators['Visibility'])
    cont.activate(wheel3.actuators['Visibility'])
    cont.activate(wheel4.actuators['Visibility'])    
        
def throwdeck_trigger():
    lastb = own['lastb']
    throw_deck_empty = scene.objects["throw_deck_empty"]
    if bBut == False:
        throw_deck_empty['kill_deck'] = 0
    if bBut == False and own['lastb'] == True:        
        #print("throw deck")
        throwdeck()        
              
def fall():
    if own['fall'] == True:
        falldeck()
        if STANCE == 1:
            own.setLinearVelocity([3,2,0], True)
        else:
            own.setLinearVelocity([-3,-2,0], True)    
        own['fall'] = False

def sit():
    #turn off sit
    if lup == 1 or ldown == 1 or lUD > sens or lUD < -sens:
        if own['sit'] == 1:
            killact(300)
            killact(299)
        own['sit'] = 0

    if aBut == False and lasta == True:
        #print(lasta)
        try:
            #print(r_ground.hitObject)
            if 'sit' in r_ground.hitObject:
                print("sit")
                own['sit'] = 1
                #killall()
                killact(3)
                if STANCE == 0:
                    skater.playAction("reg_sit", 1,65, layer=300, play_mode=0, speed=1)
                    deck.playAction("a_reg_sit", 1,65, layer=300, play_mode=0, speed=1)
                    trucks.playAction("a_reg_sit", 1,65, layer=300, play_mode=0, speed=1)
                elif STANCE == 1:
                    skater.playAction("fak_sit", 1,65, layer=300, play_mode=0, speed=1)
                    deck.playAction("a_fak_sit", 1,65, layer=300, play_mode=0, speed=1)
                    trucks.playAction("a_fak_sit", 1,65, layer=300, play_mode=0, speed=1)                                         
    #if own['sit'] == 1 and last_sit == 0:
                 
                     
                
        except:
            #print("sit broke")
            pass    
    if own['sit'] == 1:
        try:
            killact(3)
            sit_vect = r_ground.hitObject.getAxisVect( [0, 1, 0])
            if STANCE == 0:
                own.alignAxisToVect(-sit_vect, 0, .2)
                skater.playAction("reg_sit", 65,65, layer=299, play_mode=1, speed=1)
                deck.playAction("a_reg_sit", 65,65, layer=299, play_mode=1, speed=1)
                trucks.playAction("a_reg_sit", 65,65, layer=299, play_mode=1, speed=1)                                 
                
            elif STANCE == 1:
                own.alignAxisToVect(sit_vect, 0, .2) 
                skater.playAction("fak_sit", 65,65, layer=299, play_mode=1, speed=1)
                deck.playAction("a_fak_sit", 65,65, layer=299, play_mode=1, speed=1)
                trucks.playAction("a_fak_sit", 65,65, layer=299, play_mode=1, speed=1)                    
        except:
            pass    

                      
def switchcam():
    if ltsBut == False and own['lastlts'] == True and rtsBut == False:
        if own['camera'] == 1:
            own['camera'] = 0
        else:
            own['camera'] = 1
    if rtsBut == False and own['lastrts'] == True and ltsBut == False:
        if own['camera'] == 2:
            own['camera'] = 0
        else:
            own['camera'] = 2 
#followcam 
def move_followcam():
    if own['camera'] == 2:
        #if rtsBut == False and own['lastrts'] == True:
        if own['lastbkBut'] == True and bkBut == False:
            print("activate move followcam") 
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
                print("fastup")
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
    cont.deactivate(own.actuators["walk_align"])
else:
    cont.activate(own.actuators["walk_align"])                    

if r_ground.triggered:
    #print("on stair")
    try:
        if 'stair' in r_ground.hitObject:
            own['stair_counter'] = 20
            force = [ 0.0, 0.0, -100]
            # use local axis
            local = True
            # apply force
            #own.applyForce(force, local)        
    except:
        pass        
    if own['stair_counter'] > 0:
       own['stair_counter'] -= 1     

if yBut == True:
    own['walk_idling'] = 0
    own["walk_idle_frame"] = 0

                    
onboard() 
jump()
dropin()
throwdeck_trigger()

nextframe()
checkidle()
getonboard()
reset_pos()
switchcam()
move_flycam()
move_followcam()
fall()
idle_anim()
sit()
#cont.activate(cam.actuators['Camera'])
#printplaying() 

own.alignAxisToVect([0.0,0.0,1.0], 2, .03)
own.actuators["sroll"].stopSound() 
wheel1 = scene.objects["rollen.000"]
wheel2 = scene.objects["rollen.001"]
wheel3 = scene.objects["rollen.002"]
wheel4 = scene.objects["rollen.003"]
wheel1.stopAction(2)
wheel2.stopAction(2)
wheel3.stopAction(2)
wheel4.stopAction(2)


own['lasty'] = yBut
own['lastb'] = bBut  
own['lasta'] = aBut
own['lastx'] = xBut   
own['lastlts'] = ltsBut
own['lastrts'] = rtsBut        
own['lastbkBut'] = bkBut
own['dropinCol'] = dropinCol
own['walk'] = 1
    