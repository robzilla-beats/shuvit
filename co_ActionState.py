import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    skater = scene.objects["Char4"]
    deck = scene.objects["deck"]
    trucks = scene.objects["trucks"]
    loop_layer = 450
    trans_layer = 460
    flip_layer = 470
   
    #set possible requestActions
    requestActions_list = ['reg_roll', 'fak_roll', 'reg_turnLeft', 'reg_turnLeft_out', 'reg_turnRight', 'reg_turnRight_out', 'fak_turnLeft', 'fak_turnRight', 'reg_pump', 'fak_pump', 'reg_land', 'fak_land', 'reg_idle', 'reg_idle_nb', 'fak_idle', 'fak_idle_nb', 'reg_walk', 'reg_walk_nb', 'reg_walkFast', 'reg_walkFast_nb', 'fak_walk', 'fak_walk_nb', 'fak_walkFast', 'fak_walkFast_nb', 'reg_pump', 'fak_pump', 'reg_opos', 'fak_opos', 'reg_nopos', 'fak_nopos', 'reg_manual', 'fak_manual', 'reg_nmanual', 'fak_nmanual', 'reg_air', 'fak_air', 'frontside_grab', 'backside_grab', 'fak_backside_grab', 'fak_frontside_grab', 'frontside_nose_grab', 'frontside_tail_grab', 'backside_nose_grab', 'backside_tail_grab', 'fak_frontside_nose_grab', 'fak_frontside_tail_grab', 'fak_backside_nose_grab', 'fak_backside_tail_grab', 'reg_noseg', 'reg_air_nose', 'fak_air_nose', 'reg_air_tail', 'fak_air_tail', 'reg_nosegr','reg_nosegl',  'fak_noseg','fak_nosegr', 'fak_nosegl', 'reg_nosegl', 'fak_tailg', 'fak_tailgr', 'fak_tailgl', 'reg_tailg', 'reg_tailgr', 'reg_tailgl', 'reg_tailslide', 'fak_tailslide', 'reg_noseslide', 'fak_noseslide', 'nose_stall','tail_stall', 'reg_5050', 'fak_5050', 'reg_tailg', 'reg_bsboard', 'fak_bsboard', 'reg_fsboard', 'reg_powerslide', 'fak_powerslide', 'reg_fs_powerslide', 'fak_fs_powerslide']
    oneshotActions_list = ['reg_jump', 'fak_jump', 'reg_onboard', 'fak_onboard', 'reg_dropin', 'fak_dropin', 'reg_land', 'fak_land', 'reg_push', 'fak_push', 'reg_push_goof', 'fak_push_goof', 'reg_manual_revert_ccw', 'revert1', 'revert2', 'revert3', 'revert4', 'reg_ollie', 'reg_nollie', 'reg_nollie', 'fak_ollie', 'fak_nollie', 'reg_kickflip', 'fak_kickflip', 'reg_varial_kickflip', 'fak_varial_kickflip', 'reg_nollie_varial_kickflip', 'fak_nollie_varial_kickflip', 'reg_nollie_varial_heelflip', 'fak_nollie_varial_heelflip', 'reg_varial_heelflip', 'fak_varial_heelflip', 'reg_nollie_kickflip', 'fak_nollie_kickflip', 'reg_heelflip', 'fak_heelflip', 'reg_nollie_heelflip', 'fak_nollie_heelflip', 'reg_shovit', 'fak_shovit', 'reg_shovit360', 'fak_shovit360', 'reg_fsshovit360', 'fak_fsshovit360', 'reg_nollie_shovit', 'fak_nollie_shovit', 'reg_fsshovit', 'fak_fsshovit',  'reg_nollie_fsshovit', 'fak_nollie_fsshovit', 'reg_nollie_shovit360', 'fak_nollie_shovit360', 'reg_nollie_fsshovit', 'fak_nollie_fsshovit', 'reg_turnRight_out', 'reg_turnLeft_out', 'fak_turnRight_out', 'fak_turnLeft_out', 'reg_opos_out', 'fak_opos_out', 'reg_nopos_out', 'fak_nopos_out', 'reg_pump_out', 'fak_pump_out', 'reg_powerslide_out', 'fak_powerslide_out', 'reg_fs_powerslide_out', 'fak_fs_powerslide_out']

    jump_overrideList = ['reg_ollie', 'reg_nollie', 'reg_nollie', 'fak_ollie', 'fak_nollie', 'reg_kickflip', 'fak_kickflip', 'reg_varial_kickflip', 'fak_varial_kickflip', 'reg_nollie_varial_kickflip', 'fak_nollie_varial_kickflip', 'reg_nollie_varial_heelflip', 'fak_nollie_varial_heelflip', 'reg_varial_heelflip', 'fak_varial_heelflip', 'reg_nollie_kickflip', 'fak_nollie_kickflip', 'reg_heelflip', 'fak_heelflip', 'reg_nollie_heelflip', 'fak_nollie_heelflip', 'reg_shovit', 'fak_shovit', 'reg_shovit360', 'fak_shovit360', 'reg_fsshovit360', 'fak_fsshovit360', 'reg_nollie_shovit', 'fak_nollie_shovit', 'reg_fsshovit', 'fak_fsshovit',  'reg_nollie_fsshovit', 'fak_nollie_fsshovit', 'reg_nollie_shovit360', 'fak_nollie_shovit360', 'reg_nollie_fsshovit', 'fak_nollie_fsshovit']
    
    #initialize variables
    try:
        actionState = own['actionState']
        l_actionState = own['l_actionState']
        requestAction = own['requestAction']
        l_requestAction = own['l_requestAction']
        queueAction = own['queueAction']
        actionTimer = own['actionTimer']
    except:
        print("init")
        own['actionState'] = 'empty'
        own['l_actionState'] = 'empty'        
        own['requestAction'] = 'empty'    
        own['l_requestAction'] = 'empty'
        own['queueAction'] = 'empty'
        own['actionTimer'] = 0
        actionTimer = 0
        queueAction = 'empty'
        requestAction = 'empty'
        actionState = 'empty'
        l_actionState = 'empty'
        l_requestAction = 'empty'
    #print("ra1: ", requestAction) \
    if requestAction == 'empty':
        print("*******empty request****")
        
    isplaying = skater.isPlayingAction(flip_layer)
    #if isplaying  == False:    
        #own['actionTimer'] = 0

            
        
    #land action over ride
    if (requestAction == 'reg_land' or requestAction == 'fak_land') and own['grindHit'] == True:
        if l_requestAction == 'reg_land' or l_requestAction == 'fak_land':
            print("landing action fucked")
        else: 
            #print("using old requestAction")   
            requestAction = l_requestAction
            own['requestAction'] = requestAction
            own['l_actionState'] = requestAction
            actionState = requestAction
            own['actionTimer'] = 0
            actionTimer = 0 
    if (own['l_requestAction'] == 'reg_air_nose' or own['l_requestAction'] == 'reg_air_tail' or own['l_requestAction'] == 'fak_air_nose' or own['l_requestAction'] == 'fak_air_tail') and ((requestAction == 'reg_land' or requestAction == 'fak_land') or (own['requestAction'] == 'reg_roll' or own['requestAction'] == 'fak_roll')):            
    #if (own['l_requestAction'] == 'reg_air_nose' or own['l_requestAction'] == 'reg_air_tail' or own['l_requestAction'] == 'fak_air_nose' or own['l_requestAction'] == 'fak_air_tail') and (requestAction == 'reg_land' or requestAction == 'fak_land'):
        requestAction = own['l_requestAction']
        
        
        
    #revert override
    if requestAction == 'revert1' or requestAction == 'revert2' or requestAction == 'revert3' or requestAction == 'revert4':
        #print("@@@revert override")
        actionState = requestAction
        own['actionState'] = requestAction 
        if l_requestAction != 'revert1' and l_requestAction != 'revert2' and l_requestAction != 'revert3' and l_requestAction != 'revert4':   
            print("stopping revert layers")     
            skater.stopAction(loop_layer)
            trucks.stopAction(loop_layer)
            deck.stopAction(loop_layer)
            skater.stopAction(trans_layer)
            trucks.stopAction(trans_layer)
            deck.stopAction(trans_layer)                 
            
    #check last actionState to see if an out action is needed
    
    elif requestAction not in jump_overrideList:
        if l_actionState == 'reg_turnRight' and requestAction != 'reg_turnRight':
            requestAction = 'reg_turnRight_out'
            actionState = 'reg_turnRight_out'
        if l_actionState == 'reg_turnLeft' and requestAction != 'reg_turnLeft':
            requestAction = 'reg_turnLeft_out'
            actionState = 'reg_turnLeft_out'
        if l_actionState == 'fak_turnRight' and requestAction != 'fak_turnRight':
            requestAction = 'fak_turnRight_out'
            actionState = 'fak_turnRight_out'
        if l_actionState == 'fak_turnLeft' and requestAction != 'fak_turnLeft':
            requestAction = 'fak_turnLeft_out'
            actionState = 'fak_turnLeft_out'                        

        if l_actionState == 'reg_opos' and requestAction != 'reg_opos':
            requestAction = 'reg_opos_out'
            actionState = 'reg_opos_out' 
        if l_actionState == 'fak_opos' and requestAction != 'fak_opos':
            requestAction = 'fak_opos_out'
            actionState = 'fak_opos_out' 
        if l_actionState == 'reg_nopos' and requestAction != 'reg_nopos':
            requestAction = 'reg_nopos_out'
            actionState = 'reg_nopos_out' 
        if l_actionState == 'fak_nopos' and requestAction != 'fak_nopos':
            requestAction = 'fak_nopos_out'
            actionState = 'fak_nopos_out' 
            
        if l_actionState == 'reg_pump' and requestAction != 'reg_pump':
            requestAction = 'reg_pump_out'
            actionState = 'reg_pump_out' 
        if l_actionState == 'fak_pump' and requestAction != 'fak_pump':
            requestAction = 'fak_pump_out'
            actionState = 'fak_pump_out'
        if l_actionState == 'reg_powerslide' and requestAction != 'reg_powerslide':
            requestAction = 'reg_powerslide_out'
            actionState = 'reg_powerslide_out' 
        if l_actionState == 'fak_powerslide' and requestAction != 'fak_powerslide':
            requestAction = 'fak_powerslide_out'
            actionState = 'fak_powerslide_out'
        if l_actionState == 'reg_fs_powerslide' and requestAction != 'reg_fs_powerslide':
            requestAction = 'reg_fs_powerslide_out'
            actionState = 'reg_fs_powerslide_out' 
        if l_actionState == 'fak_fs_powerslide' and requestAction != 'fak_fs_powerslide':
            requestAction = 'fak_fs_powerslide_out'
            actionState = 'fak_fs_powerslide_out'                                                       
    else:
        print("action over ridden")
        #own['actionState'] = requestAction                     
    def updateAction(requestAction, actionState):
        try:
            flip_start_frame = own['flip_start_lay']
            flipspeed = own['flipspeed']
            
        except:
            flip_start_frame = 1  
            flipspeed = .6  
        #flipspeed = own['flipspeed'] 
###############################        
        #one shot actions
###############################
        if requestAction in oneshotActions_list:
            
            if requestAction == 'reg_land' and own["grindHit"] == False:
                skater.stopAction(loop_layer)
                trucks.stopAction(loop_layer)
                deck.stopAction(loop_layer)
                skater.stopAction(trans_layer)
                trucks.stopAction(trans_layer)
                deck.stopAction(trans_layer)
                print("stopping loop and trans")                                
                actionState = 'reg_land'
                own['actionTimer'] = 39
                skater.playAction("reg_land", 1,20, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=1, speed=.5)                        
                print("play land") 
            if requestAction == 'fak_land' and own["grindHit"] == False:
                actionState = 'fak_land'
                skater.stopAction(loop_layer)
                trucks.stopAction(loop_layer)
                deck.stopAction(loop_layer)
                skater.stopAction(trans_layer)
                trucks.stopAction(trans_layer)
                deck.stopAction(trans_layer)                                
                own['actionTimer'] = 39
                skater.playAction("fak_land", 1,20, layer=trans_layer, play_mode=0, speed=.5)                        
                deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=1, speed=.5)        
                print("play land")

            if requestAction == 'reg_dropin':
                actionState = 'reg_dropin'
                own['actionTimer'] = 9
                skater.playAction("nreg_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)
                deck.playAction("a_reg_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)
                trucks.playAction("a_reg_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)    
            if requestAction == 'fak_dropin':
                actionState = 'reg_dropin'
                own['actionTimer'] = 9
                skater.playAction("nfak_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)
                deck.playAction("a_fak_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)
                trucks.playAction("a_fak_dropin", 60,80, layer=trans_layer, play_mode=0, speed=.75)    



            if requestAction == 'reg_turnRight_out':
                actionState = 'reg_turnRight_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nreg_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nreg_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5)                   
                    
            if requestAction == 'reg_turnLeft_out':
                actionState = 'reg_turnLeft_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nreg_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nreg_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                
            if requestAction == 'fak_turnRight_out':
                actionState = 'fak_turnRight_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nfak_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nfak_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5)                   
                    
            if requestAction == 'fak_turnLeft_out':
                actionState = 'fak_turnLeft_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nfak_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nfak_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)  
                    trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5)              
                                      

            if requestAction == 'reg_opos_out':
                actionState = 'reg_opos_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("noposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("noposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)

            if requestAction == 'fak_opos_out':
                actionState = 'fak_opos_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("fak_oposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("fak_oposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)

            if requestAction == 'reg_nopos_out':
                actionState = 'reg_nopos_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nnoposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nnoposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)

            if requestAction == 'fak_nopos_out':
                actionState = 'fak_nopos_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("fak_noposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("fak_noposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)    
                    
            if requestAction == 'reg_pump_out':
                actionState = 'reg_pump_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nreg_pump_in", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nreg_pump_in", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    
            if requestAction == 'fak_pump_out':
                actionState = 'fak_pump_out'
                own['actionTimer'] = 19
                trans_playing = skater.isPlayingAction(trans_layer)
                if trans_playing:
                    cur_frame = skater.getActionFrame(trans_layer)
                    #cur_frame -= 2                    
                if trans_playing and cur_frame > 1:                
                    skater.playAction("nfak_pump_in", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    
                    own['actionTimer'] = cur_frame
                else:                      
                    skater.playAction("nfak_pump_in", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)                                                                           
                    
            if requestAction == 'reg_push':
                own['actionTimer'] = 70
                skater.playAction("reg_push", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
            if requestAction == 'reg_push_goof':
                own['actionTimer'] = 70
                skater.playAction("reg_push_goof", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_push':
                own['actionTimer'] = 70
                skater.playAction("fak_push", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_push_goof':
                own['actionTimer'] = 70
                skater.playAction("fak_push_goof", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,40, layer=trans_layer, play_mode=1, speed=.5)
                
            if requestAction == 'reg_manual_revert_ccw':
                own['actionTimer'] = 15
                own['actionState'] = 'reg_manual_revert_ccw'
                skater.playAction("reg_manual_revert_ccw", 70,10, layer=trans_layer, priority=8, play_mode=0, speed=4)
                deck.playAction("a_reg_manual_revert_ccw", 70,10, layer=trans_layer, priority=1, play_mode=0, speed=4)
                trucks.playAction("a_reg_manual_revert_ccw", 70,10, layer=trans_layer, priority=0, play_mode=0, speed=4)                                
            if requestAction == 'revert1':
                own['actionTimer'] = 18
                own['actionState'] = 'revert1'
                skater.playAction("revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5) 
            if requestAction == 'revert2':
                own['actionTimer'] = 18 
                own['actionState'] = 'revert2'
                skater.playAction("revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)                
                 
            if requestAction == 'revert3':
                own['actionTimer'] = 18 
                own['actionState'] = 'revert3'
                skater.playAction("revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_revert1", 1,10, layer=trans_layer, play_mode=0, speed=.5)                                     
                
            if requestAction == 'revert4':
                own['actionTimer'] = 18 
                own['actionState'] = 'revert4'
                skater.playAction("revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_revert2", 1,10, layer=trans_layer, play_mode=0, speed=.5)                

            if requestAction == 'reg_ollie':
                print("*****reg ollie act")
                actionState = 'reg_ollie'
                own['actionState'] = 'reg_ollie'
                own['actionTimer'] = 30           
                skater.playAction("reg_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("t_reg_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                
            if requestAction == 'fak_ollie':
                actionState = 'fak_ollie'
                own['actionTimer'] = 30  
                skater.playAction("fak_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("t_fak_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
            
            if requestAction == 'reg_nollie':
                actionState = 'reg_nollie'
                own['actionTimer'] = 40            
                skater.playAction("nollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("t_fak_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)               
            if requestAction == 'fak_nollie':
                actionState = 'fak_nollie'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("t_reg_ollie", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                                
            if requestAction == 'reg_kickflip':
                actionState = 'reg_kickflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_kickflip':
                actionState = 'fak_kickflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
                  
            if requestAction == 'reg_varial_kickflip':
                actionState = 'reg_varial_kickflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_varial_kickflip':
                actionState = 'fak_varial_kickflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_nollie_varial_kickflip':
                actionState = 'reg_nollie_varial_kickflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_varial_kickflip':
                actionState = 'fak_nollie_varial_kickflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_nollie_varial_heelflip':
                actionState = 'reg_nollie_varial_heelflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_varial_heelflip':
                actionState = 'fak_nollie_varial_heelflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_varialkickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_varial_heelflip':
                actionState = 'reg_varial_heelflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_varial_heelflip':
                actionState = 'fak_nollie_varial_heelflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_varialheelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_nollie_kickflip':
                actionState = 'reg_nollie_kickflip'
                own['actionTimer'] = 40            
                skater.playAction("nollie_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_kickflip':
                actionState = 'fak_nollie_kickflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_kickflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_heelflip':
                actionState = 'reg_heelflip'
                own['actionTimer'] = 40            
                skater.playAction("reg_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_heelflip':
                actionState = 'fak_heelflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
                   
            if requestAction == 'reg_nollie_heelflip':
                actionState = 'reg_nollie_heelflip'
                own['actionTimer'] = 40            
                skater.playAction("nollie_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_heelflip':
                actionState = 'fak_nollie_heelflip'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_heelflip", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
                
            if requestAction == 'reg_shovit':
                actionState = 'reg_shovit'
                own['actionTimer'] = 40            
                skater.playAction("reg_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_shovit':
                actionState = 'fak_shovit'
                own['actionTimer'] = 40  
                skater.playAction("fak_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
              
            if requestAction == 'reg_shovit360':
                actionState = 'reg_shovit360'
                own['actionTimer'] = 40            
                skater.playAction("reg_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_shovit360':
                actionState = 'fak_shovit360'
                own['actionTimer'] = 40  
                skater.playAction("fak_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_fsshovit360':
                actionState = 'reg_fsshovit360'
                own['actionTimer'] = 40            
                skater.playAction("reg_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_fsshovit360':
                actionState = 'fak_fsshovit360'
                own['actionTimer'] = 40  
                skater.playAction("fak_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                                           

            if requestAction == 'reg_nollie_shovit':
                actionState = 'reg_nollie_shovit'
                own['actionTimer'] = 40            
                skater.playAction("nollie_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_shovit':
                actionState = 'fak_nollie_shovit'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
                
            if requestAction == 'reg_fsshovit':
                actionState = 'reg_fsshovit'
                own['actionTimer'] = 40            
                skater.playAction("reg_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_fsshovit':
                actionState = 'fak_fsshovit'
                own['actionTimer'] = 40  
                skater.playAction("fak_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
             
            if requestAction == 'reg_nollie_fsshovit':
                actionState = 'reg_nollie_fsshovit'
                own['actionTimer'] = 40            
                skater.playAction("nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_fsshovit':
                actionState = 'fak_nollie_fsshovit'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 

            if requestAction == 'reg_nollie_shovit360':
                actionState = 'reg_nollie_shovit360'
                own['actionTimer'] = 40            
                skater.playAction("nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_shovit360':
                actionState = 'fak_nollie_shovit360'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
             
            if requestAction == 'reg_nollie_fsshovit':
                actionState = 'reg_nollie_fsshovit'
                own['actionTimer'] = 40            
                skater.playAction("nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_360shovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)                     
            if requestAction == 'fak_nollie_fsshovit':
                actionState = 'fak_nollie_fsshovit'
                own['actionTimer'] = 40  
                skater.playAction("fak_nollie_fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_360fsshovit", flip_start_frame,20, layer=flip_layer, play_mode=0, speed=.5) 
                     

            #reg_jump
            if requestAction == 'reg_jump':
                skater.playAction("reg_jump", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_jump2", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_jump2", 1,35, layer=trans_layer, play_mode=0, speed=.5)

            #fak_jump    
            if requestAction == 'fak_jump':
                skater.playAction("fak_jump", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_fak_jump", 1,35, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_fak_jump", 1,35, layer=trans_layer, play_mode=0, speed=.5)
            #reg_onboard            
            if requestAction == 'reg_onboard':
                skater.stopAction(loop_layer)
                deck.stopAction(loop_layer)
                trucks.stopAction(loop_layer) 
                skater.stopAction(trans_layer)
                deck.stopAction(trans_layer)
                trucks.stopAction(trans_layer)
                own['actionTimer'] = 10
                skater.playAction("reg_noffboard", 9,0, layer=trans_layer, play_mode=0, speed=.5)
                deck.playAction("a_reg_noffboard", 9,0, layer=trans_layer, play_mode=0, speed=.5)
                trucks.playAction("a_reg_noffboard", 9,0, layer=trans_layer, play_mode=0, speed=.5)

            if requestAction == 'fak_onboard':
                skater.stopAction(loop_layer)
                deck.stopAction(loop_layer)
                trucks.stopAction(loop_layer) 
                skater.stopAction(trans_layer)
                deck.stopAction(trans_layer)
                trucks.stopAction(trans_layer)                
                own['actionTimer'] = 10
                skater.playAction("nfak_offboard", 30,1, layer=trans_layer, play_mode=0, speed=1.5)
                deck.playAction("a_fak_offboard", 30,1, layer=trans_layer, play_mode=0, speed=1.5)
                trucks.playAction("a_fak_offboard", 30,1, layer=trans_layer, play_mode=0, speed=1.5)
                
                
            if requestAction == 'reg_powerslide_out':
                actionState = 'reg_powerslide_out'
                own['actionTimer'] = 40  
                skater.playAction("nreg_powerslide2", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                deck.playAction("a_reg_powerslide2_d", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                trucks.playAction("a_reg_powerslide2_t", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
            if requestAction == 'fak_powerslide_out':
                actionState = 'fak_powerslide_out'
                own['actionTimer'] = 40  
                skater.playAction("nfak_powerslide2", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                deck.playAction("a_fak_powerslide2_d", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                trucks.playAction("a_fak_powerslide2_t", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
            if requestAction == 'reg_fs_powerslide_out':
                actionState = 'reg_fs_powerslide_out'
                own['actionTimer'] = 40  
                skater.playAction("nreg_powerslide", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                deck.playAction("a_reg_powerslide", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                trucks.playAction("a_reg_powerslide", 20,0, layer=trans_layer, play_mode=0, speed=1.5)        
            if requestAction == 'fak_fs_powerslide_out':
                actionState = 'fak_fs_powerslide_out'
                own['actionTimer'] = 40  
                skater.playAction("nfak_powerslide", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                deck.playAction("a_fak_powerslide_d", 20,0, layer=trans_layer, play_mode=0, speed=1.5)
                trucks.playAction("a_fak_powerslide_t", 20,0, layer=trans_layer, play_mode=0, speed=1.5)                                        
   

#######################################        
        #loop actions 
######################################        
        #check if request is possible    
        if requestAction in requestActions_list:
            print(requestAction)
            #reg_turnLeft
            if requestAction == 'reg_turnLeft':
                actionState = 'reg_turnLeft'
                #in
                if l_actionState != 'reg_turnLeft':
                    skater.playAction("nreg_left", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_left", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                #loop
                else:
                    skater.playAction("nreg_left", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
                    deck.playAction("a_reg_left", 10,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 10,30, layer=loop_layer, play_mode=1, speed=.5)
            #reg_turnRight        
            if requestAction == 'reg_turnRight':
                actionState = 'reg_turnRight'
                #in
                if l_actionState != 'reg_turnRight':
                    skater.playAction("nreg_right", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_reg_right", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                #loop
                else:
                    skater.playAction("nreg_right", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
                    deck.playAction("a_reg_right", 10,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 10,30, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'reg_turnRight_out':
                pass        
            #fak_turnLeft
            if requestAction == 'fak_turnLeft':
                actionState = 'fak_turnLeft'
                #in
                if l_actionState != 'fak_turnLeft':
                    skater.playAction("nfak_left", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_left", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                #loop
                else:
                    skater.playAction("nfak_left", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
                    deck.playAction("a_fak_left", 10,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 10,30, layer=loop_layer, play_mode=1, speed=.5)
            #fak_turnRight        
            if requestAction == 'fak_turnRight':
                actionState = 'fak_turnRight'
                #in
                if l_actionState != 'fak_turnRight':
                    skater.playAction("nfak_right", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    deck.playAction("a_fak_right", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                    trucks.playAction("a_reg", 1,10, layer=trans_layer, play_mode=0, speed=.5)
                #loop
                else:
                    skater.playAction("nfak_right", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
                    deck.playAction("a_fak_right", 10,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
            #reg_fs_powerslide
            if requestAction == 'reg_fs_powerslide':
                actionState = 'reg_fs_powerslide'
                if l_actionState != 'reg_fs_powerslide':
                    skater.playAction("nreg_powerslide", 0,20, layer=trans_layer, priority=8, play_mode=0, speed=1.5)
                    deck.playAction("a_reg_powerslide", 0,20, layer=trans_layer, priority=1, play_mode=0, speed=1.5)
                    trucks.playAction("a_reg_powerslide", 0,20, layer=trans_layer, priority=0, play_mode=0, speed=1.5)        
                else:                           
                    skater.playAction("nreg_powerslide", 20,80, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_powerslide", 20,80, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_powerslide", 20,80, layer=loop_layer, play_mode=1, speed=.5) 
            #reg_powerslide        
            if requestAction == 'reg_powerslide':
                actionState = 'reg_powerslide'
                if l_actionState != 'reg_powerslide':
                    skater.playAction("nreg_powerslide2", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    deck.playAction("a_reg_powerslide2_d", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    trucks.playAction("a_reg_powerslide2_t", 0,20, layer=trans_layer, priority=0, play_mode=0, speed=1.5)        
                else:                           
                    skater.playAction("nreg_powerslide2", 20,80, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_powerslide2_d", 20,80, layer=loop_layer, speed=.5)
                    trucks.playAction("a_reg_powerslide2_t", 20,80, layer=loop_layer, play_mode=1, speed=.5) 
            #fak_fs_powerslide        
            if requestAction == 'fak_fs_powerslide':
                actionState = 'fak_fs_powerslide'
                if l_actionState != 'fak_fs_powerslide':
                    skater.playAction("nfak_powerslide", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    deck.playAction("a_fak_powerslide_d", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    trucks.playAction("a_fak_powerslide_t", 0,20, layer=trans_layer, priority=0, play_mode=0, speed=1.5)        
                else:                           
                    skater.playAction("nfak_powerslide", 20,80, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_powerslide_d", 20,80, layer=loop_layer, speed=.5)
                    trucks.playAction("a_fak_powerslide_t", 20,80, layer=loop_layer, play_mode=1, speed=.5) 
            #fak_powerslide        
            if requestAction == 'fak_powerslide':
                actionState = 'fak_powerslide'
                if l_actionState != 'fak_powerslide':
                    skater.playAction("nfak_powerslide2", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    deck.playAction("a_fak_powerslide2_d", 0,20, layer=trans_layer, play_mode=0, speed=1.5)
                    trucks.playAction("a_fak_powerslide2_t", 0,20, layer=trans_layer, priority=0, play_mode=0, speed=1.5)        
                else:                           
                    skater.playAction("nfak_powerslide2", 20,80, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_powerslide2_d", 20,80, layer=loop_layer, speed=.5)
                    trucks.playAction("a_fak_powerslide2_t", 20,80, layer=loop_layer, play_mode=1, speed=.5)                                                            

                    
            #reg_roll    
            if requestAction == 'reg_roll':
                if l_actionState == 'reg_pump':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:
                        skater.playAction("nreg_pump_in", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        #print(cur_frame)
                    else:    
                        skater.playAction("nreg_pump_in", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                if l_actionState == 'reg_opos':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                    if trans_playing and cur_frame > 1:
                        skater.playAction("noposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    else:   
                        own['actionTimer'] = 20 
                        skater.playAction("noposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1) 
                if l_requestAction == 'reg_nopos':
                    flipping = skater.isPlayingAction(flip_layer)
                    if flipping == 0:
                        trans_playing = skater.isPlayingAction(trans_layer)
                        if trans_playing:
                            cur_frame = skater.getActionFrame(trans_layer)
                            #cur_frame -= 2                    
                        if trans_playing and cur_frame > 1:
                            #skater.stopAction(trans_layer)
                            #deck.stopAction(trans_layer)
                            #trucks.stopAction(trans_layer)
                            skater.playAction("nnoposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                            deck.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                            trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                            #print(cur_frame)
                        else: 
                            own['actionTimer'] = 20   
                            skater.playAction("nnoposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                            deck.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                            trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                
                if l_requestAction == 'reg_manual':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("reg_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_reg_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    else:
                        skater.playAction("reg_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_reg_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        
                if l_requestAction == 'reg_nmanual':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("reg_nmanual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_fak_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_fak_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    else:
                        skater.playAction("reg_nmanual", 10,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_fak_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_fak_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)

                if l_actionState == 'reg_turnLeft':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("nreg_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_reg_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5) 
                    else:
                        own['actionTimer'] = 20
                        requestAction = 'reg_turnLeft_out'
                        actionState = 'reg_turnLeft_out'
                        skater.playAction("nreg_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_reg_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5) 
                if l_actionState == 'reg_Right':
                    #requestAction = 'reg_turnRight_out'
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("nreg_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_reg_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5) 
                    else:
                        own['actionTimer'] = 20
                        skater.playAction("nreg_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_reg_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5) 
                if requestAction == 'reg_roll':
                    actionState = 'reg_roll' 
                    skater.playAction("nreg", 1,60, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=.5)                           

                                                                                                                              

            #fak_roll    
            if requestAction == 'fak_roll':
                if l_actionState == 'fak_pump':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:
                        #skater.stopAction(trans_layer)
                        #deck.stopAction(trans_layer)
                        #trucks.stopAction(trans_layer)
                        skater.playAction("nfak_pump_in", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        #print(cur_frame)
                    else:    
                        skater.playAction("nfak_pump_in", 20,1, layer=trans_layer, play_mode=0, speed=1)
                if l_actionState == 'fak_opos':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:
                        #skater.stopAction(trans_layer)
                        #deck.stopAction(trans_layer)
                        #trucks.stopAction(trans_layer)
                        skater.playAction("fak_oposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        #print(cur_frame)
                    else:
                        own['actionTimer'] = 20    
                        skater.playAction("fak_oposin", 20,1, layer=trans_layer, play_mode=0, speed=1) 
                        deck.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                if l_requestAction == 'fak_nopos':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:
                        #skater.stopAction(trans_layer)
                        #deck.stopAction(trans_layer)
                        #trucks.stopAction(trans_layer)
                        skater.playAction("fak_noposin", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        #print(cur_frame)
                    else:    
                        own['actionTimer'] = 20
                        skater.playAction("fak_noposin", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        deck.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=1) 
                if l_requestAction == 'fak_manual':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("fak_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_fak_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_fak_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    else:
                        skater.playAction("fak_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_fak_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_fak_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        
                if l_requestAction == 'fak_nmanual':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("fak_nmanual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_reg_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg_manual", cur_frame,1, layer=trans_layer, play_mode=0, speed=1)
                    else:
                        skater.playAction("fak_nmanual", 10,1, layer=trans_layer, play_mode=0, speed=1)                
                        deck.playAction("a_reg_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        trucks.playAction("a_reg_manual", 10,1, layer=trans_layer, play_mode=0, speed=1)
                        
                        
                        
                        
                if l_actionState == 'fak_turnLeft':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("nfak_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_fak_left", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    else:
                        skater.playAction("nfak_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_fak_left", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", 20,1, layer=trans_layer, play_mode=0, speed=.5) 
                if l_requestAction == 'fak_turnRight':
                    trans_playing = skater.isPlayingAction(trans_layer)
                    if trans_playing:
                        cur_frame = skater.getActionFrame(trans_layer)
                        #cur_frame -= 2                    
                    if trans_playing and cur_frame > 1:                
                        skater.playAction("nfak_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_fak_right", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", cur_frame,1, layer=trans_layer, play_mode=0, speed=.5)
                    else:
                        skater.playAction("nfak_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        deck.playAction("a_fak_right", 10,1, layer=trans_layer, play_mode=0, speed=.5)
                        trucks.playAction("a_reg", 10,1, layer=trans_layer, play_mode=0, speed=.5)                                 
                
                if requestAction == 'fak_roll':
                    actionState = 'fak_roll' 
                    skater.playAction("nfak", 1,60, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=.5)                                                                                                                          

            #reg_opos
            if requestAction == 'reg_opos' and own['actionTimer'] == 0:
                actionState = 'reg_opos'
                #in
                if l_actionState != 'reg_opos':
                    skater.playAction("noposin", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                  
                    skater.playAction("nopos", 1,40, layer=loop_layer, play_mode=1, speed=1)
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1)
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1)
            
            #fak_opos
            if requestAction == 'fak_opos':
                actionState = 'fak_opos'
                #in
                if l_actionState != 'fak_opos':
                    skater.playAction("fak_oposin", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("fak_opos", 1,40, layer=loop_layer, play_mode=1, speed=1) 
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1) 
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1) 
            
            #reg_nopos
            if requestAction == 'reg_nopos':
                actionState = 'reg_nopos'
                #in
                if l_actionState != 'reg_nopos':
                    skater.playAction("nnoposin", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("nnopos", 1,40, layer=loop_layer, play_mode=1, speed=1)
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1) 
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1)
            
            #fak_nopos
            if requestAction == 'fak_nopos':
                actionState = 'fak_nopos'
                #in
                if l_actionState != 'fak_nopos':
                    skater.playAction("fak_noposin", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("fak_nopos", 1,40, layer=loop_layer, play_mode=1, speed=1)
                    deck.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1) 
                    trucks.playAction("a_reg", 1,40, layer=loop_layer, play_mode=1, speed=1)                            
            
            #reg_pump
            if requestAction == 'reg_pump':
                actionState = 'reg_pump'
                if l_actionState != 'reg_pump':
                    skater.playAction("nreg_pump_in", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("nreg_pump", 1,60, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg", 1,60, layer=loop_layer, play_mode=1, speed=1) 
                    trucks.playAction("a_reg", 1,60, layer=loop_layer, play_mode=1, speed=1)        

            #fak_pump
            if requestAction == 'fak_pump':
                actionState = 'fak_pump'
                if l_actionState != 'fak_pump':
                    skater.playAction("nfak_pump_in", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg", 1,20, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("nfak_pump.001", 1,60, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg", 1,60, layer=loop_layer, play_mode=1, speed=1) 
                    trucks.playAction("a_reg", 1,60, layer=loop_layer, play_mode=1, speed=1) 
            #reg_manual
            if requestAction == 'reg_manual':
                actionState = 'reg_manual'
                #in
                if l_requestAction != 'reg_manual' and l_actionState != 'reg_air_tail':
                    skater.playAction("reg_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)                
                    deck.playAction("a_reg_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("reg_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)                
                    deck.playAction("a_reg_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
            #fak_manual
            if requestAction == 'fak_manual':
                actionState = 'fak_manual'
                #in
                if l_requestAction != 'fak_manual' and l_actionState != 'fak_air_tail':
                    skater.playAction("fak_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)                
                    deck.playAction("a_fak_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("fak_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)                
                    deck.playAction("a_fak_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
            #reg_nmanual
            if requestAction == 'reg_nmanual':
                actionState = 'reg_nmanual'
                #in
                if l_requestAction != 'reg_nmanual' and l_actionState != 'reg_air_nose':
                    skater.playAction("reg_nmanual", 1,10, layer=trans_layer, play_mode=0, speed=1)                
                    deck.playAction("a_fak_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("reg_nmanual", 10,70, layer=loop_layer, play_mode=1, speed=.5)                
                    deck.playAction("a_fak_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
            #fak_nmanual
            if requestAction == 'fak_nmanual':
                actionState = 'fak_nmanual'
                #in
                if l_requestAction != 'fak_nmanual' and l_actionState != 'fak_air_nose':
                    skater.playAction("fak_nmanual", 1,10, layer=trans_layer, play_mode=0, speed=1)                
                    deck.playAction("a_reg_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_manual", 1,10, layer=trans_layer, play_mode=0, speed=1)
                #loop
                else:
                    skater.playAction("fak_nmanual", 10,70, layer=loop_layer, play_mode=1, speed=.5)                
                    deck.playAction("a_reg_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_manual", 10,70, layer=loop_layer, play_mode=1, speed=.5) 
            if requestAction == 'reg_air':
                actionState = 'reg_air'
                skater.playAction("reg_air", 1,60, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_reg", 1,2, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,2, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_air':
                actionState = 'fak_air'
                skater.playAction("fak_air", 1,60, layer=loop_layer, play_mode=1, speed=.5)        
                deck.playAction("a_reg", 1,2, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 1,2, layer=loop_layer, play_mode=1, speed=.5)                  
            if requestAction == 'frontside_grab':
                actionState = 'frontside_grab'
                if l_actionState != 'frontside_grab':
                    skater.playAction("reg_fg", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("reg_fg", 10,30, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'backside_grab':
                actionState = 'backside_grab'
                if l_actionState != 'backside_grab':
                    skater.playAction("reg_bsg2", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("reg_bsg2", 10,30, layer=loop_layer, play_mode=1, speed=.5)
                    
                    
                    
            if requestAction == 'fak_frontside_grab':
                actionState = 'fak_frontside_grab'
                if l_actionState != 'fak_frontside_grab':
                    skater.playAction("fak_fg", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_fg", 10,30, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_backside_grab':
                actionState = 'fak_backside_grab'
                if l_actionState != 'fak_backside_grab':
                    skater.playAction("fak_bg", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_bg", 10,30, layer=loop_layer, play_mode=1, speed=.5)                                                                                                     
            if requestAction == 'frontside_nose_grab':
                actionState = 'frontside_nose_grab'
                if l_actionState != 'frontside_nose_grab':
                    skater.playAction("frontside_nose_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("frontside_nose_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5)   
            if requestAction == 'backside_nose_grab':
                actionState = 'backside_nose_grab'
                if l_actionState != 'backside_nose_grab':
                    skater.playAction("backside_nose_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("backside_nose_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
            if requestAction == 'fak_frontside_nose_grab':
                actionState = 'fak_frontside_nose_grab'
                if l_actionState != 'fak_frontside_nose_grab':
                    skater.playAction("fak_frontside_nose_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_frontside_nose_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5)   
            if requestAction == 'fak_backside_nose_grab':
                actionState = 'fak_backside_nose_grab'
                if l_actionState != 'fak_backside_nose_grab':
                    skater.playAction("fak_backside_nose_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_backside_nose_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5)  







            if requestAction == 'frontside_tail_grab':
                actionState = 'frontside_tail_grab'
                if l_actionState != 'frontside_tail_grab':
                    skater.playAction("frontside_tail_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("frontside_tail_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5)   
            if requestAction == 'backside_tail_grab':
                actionState = 'backside_tail_grab'
                if l_actionState != 'backside_tail_grab':
                    skater.playAction("backside_tail_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("backside_tail_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
            if requestAction == 'fak_frontside_tail_grab':
                actionState = 'fak_frontside_tail_grab'
                if l_actionState != 'fak_frontside_tail_grab':
                    skater.playAction("fak_frontside_tail_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_frontside_tail_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5)   
            if requestAction == 'fak_backside_tail_grab':
                actionState = 'fak_backside_tail_grab'
                if l_actionState != 'fak_backside_tail_grab':
                    skater.playAction("fak_backside_tail_grab", 1,10, layer=trans_layer, play_mode=0, speed=1)    
                else:
                    skater.playAction("fak_backside_tail_grab", 10,30, layer=loop_layer, play_mode=1, speed=.5) 
                    
            if requestAction == 'reg_noseg':
                actionState = 'reg_noseg'
                if l_actionState != 'reg_noseg' and l_actionState != 'reg_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)
                    skater.playAction("reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5)

            if requestAction == 'fak_noseg':
                actionState = 'fak_noseg'
                if l_actionState != 'fak_noseg' and l_actionState != 'fak_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
            
            if requestAction == 'reg_tailg':
                actionState = 'reg_tailg'
                if l_actionState != 'reg_tailg' and l_actionState != 'reg_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5)

            if requestAction == 'fak_tailg':
                actionState = 'fak_tailg'
                if l_actionState != 'fak_tailg' and l_actionState != 'fak_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)                       
            if requestAction == 'reg_tailgr':
                actionState = 'reg_tailgr'
                if l_actionState != 'reg_tailgr' and l_actionState != 'reg_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_tailgr':
                actionState = 'fak_tailgr'
                if l_actionState != 'fak_tailgr' and l_actionState != 'fak_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_tailgR", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_tailgR", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    
            if requestAction == 'reg_tailgl':
                actionState = 'reg_tailgl'
                if l_actionState != 'reg_tailgl' and l_actionState != 'reg_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_tailgl':
                actionState = 'fak_tailgl'
                if l_actionState != 'fak_tailgl' and l_actionState != 'fak_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_tailgL", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_tailgL", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    
##############################
            if requestAction == 'reg_nosegr':
                actionState = 'reg_nosegr'
                if l_actionState != 'reg_nosegr' and l_actionState != 'reg_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
            if requestAction == 'fak_nosegr':
                actionState = 'fak_nosegr'
                if l_actionState != 'fak_nosegr' and l_actionState != 'fak_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_nosegR", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_nosegR", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    
            if requestAction == 'reg_nosegl':
                actionState = 'reg_nosegl'
                if l_actionState != 'reg_nosegl' and l_actionState != 'reg_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
            print("rA:", requestAction)        
            if requestAction == 'fak_nosegl':
                actionState = 'fak_nosegl'
                print("fak_nosegl state")
                if l_actionState != 'fak_nosegl' and l_actionState != 'fak_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_nosegL", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_nosegL", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    

            if requestAction == 'reg_tailslide':
                actionState = 'reg_tailslide'
                if l_actionState != 'reg_tailslide' and l_actionState != 'reg_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    
            if requestAction == 'fak_tailslide':
                actionState = 'fak_tailslide'
                if l_actionState != 'fak_tailslide' and l_actionState != 'fak_air_tail':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_noses", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_noses", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    

            if requestAction == 'reg_noseslide':
                actionState = 'reg_noseslide'
                if l_actionState != 'reg_noseslide' and l_actionState != 'reg_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("fak_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    
            if requestAction == 'fak_noseslide':
                actionState = 'fak_noseslide'
                if l_actionState != 'fak_noseslide' and l_actionState != 'fak_air_nose':
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_tails", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    skater.playAction("reg_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_tails", 30,1, layer=loop_layer, play_mode=1, speed=.5)                    




            if requestAction == 'reg_5050':
                actionState = 'reg_5050'
                #own['actionTimer'] = 0
                skater.playAction("reg_5050", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_reg", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 11,30, layer=loop_layer, play_mode=1, speed=.5)                                     
            if requestAction == 'fak_5050':
                actionState = 'fak_5050'
                own['actionTimer'] = 0
                skater.playAction("fak_5050", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_reg", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg", 11,30, layer=loop_layer, play_mode=1, speed=.5)                                                                              

            if requestAction == 'reg_bsboard':
                actionState = 'reg_bsboard'
                skater.playAction("reg_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_reg_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)                                     
            if requestAction == 'fak_bsboard':
                actionState = 'fak_bsboard'
                skater.playAction("fak_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_fak_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_fak_BS_Board2", 1,30, layer=loop_layer, play_mode=1, speed=.5)                                                                              

            if requestAction == 'reg_fsboard':
                actionState = 'reg_fsboard'
                skater.playAction("reg_FS_Board", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                deck.playAction("a_reg_FS_Board", 1,30, layer=loop_layer, play_mode=1, speed=.5)
                trucks.playAction("a_reg_FS_Board", 1,30, layer=loop_layer, play_mode=1, speed=.5)                                     



            if requestAction == 'reg_air_nose':
                actionState = 'reg_air_nose'
                if l_actionState != 'reg_air_nose':
                    skater.stopAction(loop_layer)
                    deck.stopAction(loop_layer)
                    trucks.stopAction(loop_layer)
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_noseg.002", 1,10, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    #pass
                    skater.playAction("reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_noseg.002", 11,30, layer=loop_layer, play_mode=1, speed=.5) 
            if requestAction == 'fak_air_nose':
                actionState = 'fak_air_nose'
                if l_actionState != 'fak_air_nose':
                    skater.stopAction(loop_layer)
                    deck.stopAction(loop_layer)
                    trucks.stopAction(loop_layer)
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_noseg", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    #pass
                    skater.playAction("fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_noseg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    
            if requestAction == 'reg_air_tail':
                actionState = 'reg_air_tail'
                if l_actionState != 'reg_air_tail':
                    skater.stopAction(loop_layer)
                    deck.stopAction(loop_layer)
                    trucks.stopAction(loop_layer)
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_reg_tailg.001", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    #pass
                    skater.playAction("reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_tailg.001", 30,1, layer=loop_layer, play_mode=1, speed=.5) 
            if requestAction == 'fak_air_tail':
                actionState = 'fak_air_tail'
                if l_actionState != 'fak_air_tail':
                    skater.stopAction(loop_layer)
                    deck.stopAction(loop_layer)
                    trucks.stopAction(loop_layer)
                    skater.stopAction(flip_layer)
                    deck.stopAction(flip_layer)
                    trucks.stopAction(flip_layer)                    
                    skater.playAction("fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    deck.playAction("a_fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)
                    trucks.playAction("a_fak_tailg", 40,30, layer=trans_layer, play_mode=0, speed=1)        
                else:
                    #pass
                    skater.playAction("fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_tailg", 30,1, layer=loop_layer, play_mode=1, speed=.5)                     
                    
                                         
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #walk anims            
            #reg_idle    
            if requestAction == 'reg_idle':
                actionState = 'reg_idle'
                if l_requestAction != 'reg_idle':
                    if l_requestAction == 'reg_walk' or l_requestAction == 'reg_walkFast':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.stopAction(loop_layer)
                        deck.stopAction(loop_layer)
                        trucks.stopAction(loop_layer)
                        if cur_frame > 11:
                            cur_frame += 1
                            skater.playAction("reg_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                            deck.playAction("a_reg_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                            trucks.playAction("a_reg_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)  
                        else:
                            cur_frame -= 1
                            skater.playAction("reg_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                            deck.playAction("a_reg_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                            trucks.playAction("a_reg_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                    else:
                        #print("#####")
                        trans_playing = skater.isPlayingAction(trans_layer)
                        if trans_playing == 1:
                            skater.playAction("reg_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)
                            #deck.playAction("a_reg_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)
                            #trucks.playAction("a_reg_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)                            
            #reg_idle_nb     
            if requestAction == 'reg_idle_nb':
                actionState = 'reg_idle_nb'
                if l_requestAction != 'reg_idle_nb':
                    if l_requestAction == 'reg_walk_nb' or l_requestAction == 'reg_walkFast_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.stopAction(loop_layer)
                        deck.stopAction(loop_layer)
                        trucks.stopAction(loop_layer)
                        if cur_frame > 11:
                            cur_frame += 1
                            skater.playAction("reg_nwalk_nb.001", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                        else:
                            cur_frame -= 1
                            skater.playAction("reg_nwalk_nb.001", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                    else:
                        trans_playing = skater.isPlayingAction(trans_layer)
                        if trans_playing == 1:
                            #pass
                            skater.playAction("reg_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)
                                
            #fak_idle                
            if requestAction == 'fak_idle':
                actionState = 'fak_idle'
                if l_requestAction != 'fak_idle':
                    if l_requestAction == 'fak_walk' or l_requestAction == 'fak_walkFast':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.stopAction(loop_layer)
                        deck.stopAction(loop_layer)
                        trucks.stopAction(loop_layer)                    
                        if cur_frame > 11:
                            cur_frame += 1
                            skater.playAction("fak_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                            deck.playAction("a_fak_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                            trucks.playAction("a_fak_nwalk", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)  
                        else:
                            cur_frame -= 1
                            skater.playAction("fak_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                            deck.playAction("a_fak_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                            trucks.playAction("a_fak_nwalk", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)                  
                    else:
                        trans_playing = skater.isPlayingAction(trans_layer)
                        if trans_playing == 1:
                            #pass
                            skater.playAction("fak_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)                        

            #fak_idle_nb                
            if requestAction == 'fak_idle_nb':
                actionState = 'fak_idle_nb'
                if l_requestAction != 'fak_idle_nb':
                    if l_requestAction == 'fak_walk_nb' or l_requestAction == 'fak_walkFast_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.stopAction(loop_layer)
                        deck.stopAction(loop_layer)
                        trucks.stopAction(loop_layer)                    
                        if cur_frame > 11:
                            cur_frame += 1
                            skater.playAction("fak_nwalk_nb.001", cur_frame,35, layer=trans_layer, play_mode=0, speed=.5)
                        else:
                            cur_frame -= 1
                            skater.playAction("fak_nwalk_nb.001", cur_frame,0, layer=trans_layer, play_mode=0, speed=.5)
                    else:
                        trans_playing = skater.isPlayingAction(trans_layer)
                        if trans_playing == 1:
                            #pass
                            skater.playAction("fak_idle1", 1,120, layer=loop_layer, play_mode=0, speed=.5)                                                                         

            #reg_walk    
            if requestAction == 'reg_walk':
                actionState = 'reg_walk'
                #in
                if l_requestAction != 'reg_walk':
                    if l_requestAction == 'reg_walkFast':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                        deck.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                        trucks.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5) 
                        skater.setActionFrame(cur_frame, loop_layer)
                        deck.setActionFrame(cur_frame, loop_layer)
                        trucks.setActionFrame(cur_frame, loop_layer)                                       
                #loop
                else:
                    skater.playAction("reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                    deck.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
            
            #reg_walk_nb    
            if requestAction == 'reg_walk_nb':
                actionState = 'reg_walk_nb'
                #in
                if l_requestAction != 'reg_walk_nb':
                    if l_requestAction == 'reg_walkFast_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("reg_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=.5) 
                        skater.setActionFrame(cur_frame, loop_layer)
                                          
                #loop
                else:
                    skater.playAction("reg_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=.5)               

            #reg_walkFast    
            if requestAction == 'reg_walkFast':
                actionState = 'reg_walkFast'
                #in
                if l_requestAction != 'reg_walkFast':
                    if l_requestAction == 'reg_walk':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                        deck.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                        trucks.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1) 
                        skater.setActionFrame(cur_frame, loop_layer)
                        deck.setActionFrame(cur_frame, loop_layer)
                        trucks.setActionFrame(cur_frame, loop_layer)
                        print("set last walk frame", cur_frame)                                       
                #loop
                else:
                    skater.playAction("reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                    deck.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                    trucks.playAction("a_reg_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)          
            #reg_walkFast_nb    
            if requestAction == 'reg_walkFast_nb':
                actionState = 'reg_walkFast_nb'
                #in
                if l_requestAction != 'reg_walkFast_nb':
                    if l_requestAction == 'reg_walk_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("reg_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=1) 
                        skater.setActionFrame(cur_frame, loop_layer)
                                          
                #loop
                else:
                    skater.playAction("reg_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=1)                   
            
            #fak_walk
            if requestAction == 'fak_walk':
                #in
                actionState = 'fak_walk'
                if l_requestAction != 'fak_walk':
                    if l_requestAction == 'fak_walkFast':
                        cur_frame = skater.getActionFrame(loop_layer)
                        #actionState = 'fak_walk'
                        skater.playAction("fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)    
                        deck.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                        trucks.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)      
                        skater.setActionFrame(cur_frame, loop_layer)
                        deck.setActionFrame(cur_frame, loop_layer)
                        trucks.setActionFrame(cur_frame, loop_layer)
                    #pass
                #loop
                else:
                    skater.playAction("fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)    
                    deck.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)
                    trucks.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=.5)

            #fak_walk_nb    
            if requestAction == 'fak_walk_nb':
                actionState = 'fak_walk_nb'
                #in
                if l_requestAction != 'fak_walk_nb':
                    if l_requestAction == 'fak_walkFast_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("fak_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=.5) 
                        skater.setActionFrame(cur_frame, loop_layer)
                                          
                #loop
                else:
                    skater.playAction("fak_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=.5)
            
            #fak_walkFast            
            if requestAction == 'fak_walkFast':
                actionState = 'fak_walkFast'
                #in
                if l_requestAction != 'fak_walkFast':
                    if l_requestAction == 'fak_walk':
                        cur_frame = skater.getActionFrame(loop_layer)
                        #actionState = 'fak_walkFast'
                        skater.playAction("fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)         
                        deck.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                        trucks.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)       
                        skater.setActionFrame(cur_frame, loop_layer)
                        deck.setActionFrame(cur_frame, loop_layer)
                        trucks.setActionFrame(cur_frame, loop_layer)                    
                    #pass
                #loop
                else:
                    skater.playAction("fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)             
                    deck.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1)
                    trucks.playAction("a_fak_nwalk", 0,35, layer=loop_layer, play_mode=1, speed=1) 
            
            #fak_walkFast_nb    
            if requestAction == 'fak_walkFast_nb':
                actionState = 'fak_walkFast_nb'
                #in
                if l_requestAction != 'fak_walkFast_nb':
                    if l_requestAction == 'fak_walk_nb':
                        cur_frame = skater.getActionFrame(loop_layer)
                        skater.playAction("fak_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=1) 
                        skater.setActionFrame(cur_frame, loop_layer)
                                          
                #loop
                else:
                    skater.playAction("fak_nwalk_nb.001", 0,35, layer=loop_layer, play_mode=1, speed=1)                           
        
            own['actionState'] = actionState
        else:
            pass
        #actionTimer = 60
        #try:
        #own['actionTimer'] = 60
        #except: pass
        #print(actionState)
        own['actionState'] = actionState
        return actionState
            
    
    #if (l_actionState == 'reg_land' and own['actionState'] != 'reg_land') or (l_actionState == 'fak_land' and own['actionState'] != 'fak_land'):
    #if (own['actionState'] != 'reg_land') and (own['actionState'] != 'fak_land'):
    l_playing = skater.isPlayingAction(loop_layer)
    t_playing = skater.isPlayingAction(trans_layer)        
    if l_playing == 1 and t_playing == 1:
        skater.stopAction(loop_layer)
        trucks.stopAction(loop_layer)
        deck.stopAction(loop_layer)
    
    ###
    if own['actionTimer'] > 0:
        own['actionTimer'] -= 1
        #requestAction = 'empty'
    
##############
    #turn off land for manuals
    if (requestAction == 'reg_manual' or requestAction == 'fak_manual' or requestAction == 'reg_nmanual' or requestAction == 'fak_nmanual') and (actionState == 'reg_land' or actionState == 'fak_land'):
        own['actionTimer'] = 0
        
    #turn off land for grinds
    #if requestAction == 'reg_noseg' or requestAction == 'reg_5050' or requestAction == 'fak_5050':
        #own['actionTimer'] = 0
                  
    if (own['actionTimer'] == 0 or requestAction == 'reg_land' or requestAction == 'fak_land') or requestAction in jump_overrideList:
        actionState = updateAction(requestAction, actionState)
        #own['actionState'] = actionState
        
  
###################  
    
    #debug
    #print("rA:", requestAction, "|aS:", own['actionState'], "q", queueAction, own['actionTimer'])
    cur_frame = skater.getActionFrame(trans_layer)
    #print(cur_frame)
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

    if actionState == 'empty':
        print("EMPTY ACTION!!!")
        skater.stopAction(loop_layer)
        deck.stopAction(loop_layer)
        trucks.stopAction(loop_layer)    
    #set last variables
    own['l_actionState'] = actionState
    own['l_requestAction'] = requestAction
    #own['actionTimer'] = actionTimer
    own['queueAction'] = queueAction
    
main()
