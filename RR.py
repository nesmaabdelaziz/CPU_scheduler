from chart1 import plottingRR


def RoundRobin(process_data, Q_time):
    start_time = []
    exit_time = []
    sequence_of_process = []
    ready_queue = []
    s_time = 0
    # sort according to arrival time
    process_data.sort(key=lambda x: x[1])
    while 1:
        # Check if the next process is part of the ready_queue
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][3] == 0:
                present = 0
                if len(ready_queue) != 0:
                    for k in range(len(ready_queue)):
                        if process_data[i][0] == ready_queue[k][0]:
                            present = 1
                # Add the process to the ready_queue if it was not there already
                if present == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []

                # Append the recently executed process to the end of the ready_queue
                if len(ready_queue) != 0 and len(sequence_of_process) != 0:
                    for k in range(len(ready_queue)):
                        if ready_queue[k][0] == sequence_of_process[len(sequence_of_process) - 1]:
                            ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))

            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        #If process has remaining burst time greater than the quantum time, it will execute for a time period equal to the quantum and then switch
        if len(ready_queue) != 0:
            if ready_queue[0][2] > Q_time:
                start_time.append(s_time)
                s_time = s_time + Q_time
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - Q_time
                ready_queue.pop(0)

            elif ready_queue[0][2] <= Q_time:
                #If a process has a remaining burst time less than or equal to quantum, it will complete its execution
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    sequence_of_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
        #If process has remaining burst time greater than the quantum time, it will execute for a time period equal to the quantum and then switch
        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            if normal_queue[0][2] > Q_time:
                start_time.append(s_time)
                s_time = s_time + Q_time
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - Q_time
            elif normal_queue[0][2] <= Q_time:
                #If a process has a remaining burst time less than or equal to quantum, it will complete its execution
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(e_time)

    t_time = calculateTurnaroundTime(process_data)
    w_time = FindAvgWaitingRoundRobin(process_data)
    plottingRR(sequence_of_process, e_time, start_time, exit_time)
    return w_time


def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    '''
    average_turnaround_time = total_turnaround_time / no_of_processes
    '''
    return average_turnaround_time

def FindAvgWaitingRoundRobin(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][4]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
    '''
    average_waiting_time = total_waiting_time / no_of_processes
    '''
    return average_waiting_time
