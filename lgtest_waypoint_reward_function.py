def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
     
    # Read input parameters
    center_variance = params["distance_from_center"] / params["track_width"]
     
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    closest_waypoints = params["closest_waypoints"]
     
    left_lane = [25,26,27,28,29,30,31,57,58,59,60,61,62,63,72,73,74,75,76,77,78,79,80,81,82,83,84,
                 101,102,103,104,105,106,127,128,129,130,131,159,160,161,162,163,164]
    right_lane = [38,39,40,41,42,43,44,45,46,85,86,87,88,89,90,91,91,93,94,95]
    center_lane = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
                    32,33,34,35,36,37,46,47,48,49,50,51,52,53,54,55,56,64,65,66,67,68,69,70,71,
                    96,97,98,99,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,
                    132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158]
     
#     after_closest_waypoints = params["closest_waypoints"][1]
     
    # Calculate 3 markers that are at varying distances away from the center line
    reward = 21
     
    if all_wheels_on_track:
        reward += 10
    else:
        reward -= 10
     
    # Give higher reward if the car is closer to center line and vice versa
     
    if closest_waypoints[1] in left_lane and params['is_left_of_center']:
        reward += 10
    elif closest_waypoints[1] in right_lane and not params['is_left_of_center']:
        reward += 10
    elif closest_waypoints[1] in center_lane and center_variance <0.4:
        reward += 10
    else:
        reward -= 10
         
    return float(reward)