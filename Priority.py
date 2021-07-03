from chart1 import plotting, plottingNon


def FindAvgWaitingPriorityPre(process_data):
    start_time = []
    exit_time = []
    s_time = 0
    sequence_of_process = []
    process_data.sort(key=lambda x: x[1])
    '''
    Sort processes according to the Arrival Time
    '''
    while 1:
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                             process_data[i][5]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                             process_data[i][5]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[3])
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(ready_queue[0][0]-1)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)
        if len(ready_queue) == 0:
            normal_queue.sort(key=lambda x: x[1])
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(normal_queue[0][0]-1)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)

    total_duration = e_time
    plotting(sequence_of_process, total_duration, start_time)

    w_time = calculateWaitingTimePriorityPre(process_data)
    return w_time


def calculateWaitingTimePriorityPre(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][5] - process_data[i][1]
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

def FindAvgWaitingPriorityNonpre(process_data):
    start_time = []
    burst_time = []
    exit_time = []
    s_time = 0
    e_time = 0
    sequence_of_process = []
    process_data.sort(key=lambda x: x[1])
    '''
    Sort processes according to the Arrival Time
    '''
    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []
        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][4] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][4] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[3])
            '''
            Sort the processes according to the Priority, considering Higher the Value, Higher the Priority
            '''
            start_time.append(s_time)
            burst_time.append(ready_queue[0][2])
            s_time = s_time + ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)

            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break

            sequence_of_process.append(process_data[k][0]-1)
            process_data[k][4] = 1
            process_data[k].append(e_time)
        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            burst_time.append(ready_queue[0][2])
            s_time = s_time + normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break

            sequence_of_process.append(process_data[k][0]-1)
            process_data[k][4] = 1
            process_data[k].append(e_time)
    total_duration = e_time

    plottingNon(sequence_of_process, total_duration, start_time, burst_time)

    w_time = calculateWaitingTimePriorityNonpre(process_data)
    return w_time

def calculateWaitingTimePriorityNonpre(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][5] - process_data[i][2]  - process_data[i][1]
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
