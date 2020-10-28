input_file = open("input.txt", "r")
num_test_cases = int(input_file.readline())

"""
Parenting partner activities

Give a list of "activities", returns a string representing a schedule for the
co-parents C and J that need to attend said activities. "Activities" are defined as parameter 
inputs of two ints, representing start and end times of the activities. A co-parent 
can only attend one activity at a time.

For example, for activities
0-10
5-10
The output string could be CJ or JC, denoting co-parent C or J could cover the first 
activity, and the other co-parent could attend the second activity (that starts during
the course of the first activity)

If such a schedule cannot be determined, outputs IMPOSSIBLE
"""
for i in range(1, num_test_cases + 1):
    num_activities = int(input_file.readline())
    activities = []
    time_map = {}
    result = ""

    # this first step is to read through the data and get all the activities in a map
    # where the key is start time and the values are the possible stop times (can't be more than 2)
    for j in range(0, num_activities):
        start_end = input_file.readline().split()
        start = int(start_end[0])
        end = int(start_end[1])
        activities.append(start)

        if start in time_map:
            if len(time_map[start]) == 2: # more than two activities start at same time
                result = "IMPOSSIBLE"
            time_map[start].append(end)
        else:
            time_map[start] = []
            time_map[start].append(end)
    
    if result == "IMPOSSIBLE":
        print("Case #{}: {}".format(i, result))
    else:
        # we don't know that the given activities will be in order, so we need to sort first
        sorted_keys = sorted(time_map.keys())
        task_map = {} # map start time to who is doing task
        
        c_last_occupied = -1
        j_last_occupied = -1
        
        for start_time in sorted_keys:
            for end_time in time_map[start_time]:
                if c_last_occupied > start_time:
                    if j_last_occupied > start_time:
                        # this is the case where both parents are occupied + can't add another activity
                        result = "IMPOSSIBLE"
                    else:
                        # assign to J
                        j_last_occupied = end_time
                        if start_time in task_map:
                            # this is the edge case where C could have started an activity at the same
                            # time, and thus our dictionary already has a key value for that start time
                            task_map[start_time].append("J")
                        else:
                            task_map[start_time] = []
                            task_map[start_time].append("J")
                else:
                    # assign to C
                    c_last_occupied = end_time
                    if start_time in task_map:
                        task_map[start_time].append("C")
                    else:
                        task_map[start_time] = []
                        task_map[start_time].append("C")
        
        if result == "IMPOSSIBLE":
            print("Case #{}: {}".format(i, result))
        else:
            for start_time in activities:
                for task_owner in task_map[start_time]:
                    result += task_owner
            print("Case #{}: {}".format(i, result))