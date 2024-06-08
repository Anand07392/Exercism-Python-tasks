def eat_ghost(power_pellet_active, touching_ghost):      
    if power_pellet_active==True and touching_ghost==True:
        return True
    else:
        return False


def score(touching_power_pellet, touching_dot):
    if touching_dot==True or touching_power_pellet==True:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    if power_pellet_active==True or touching_ghost==False:
        return False
    else:
        return True


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots:
        if touching_ghost and not power_pellet_active:
            return False  
        return True 
    return False  
    
