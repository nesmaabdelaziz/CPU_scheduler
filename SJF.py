from chart1 import plotting, plottingNon

def FindAvgWaitingSJFPre(final_pre):
    flag=1
    e_time = 1
    total_waiting_time = 0
    total_duration = 0

    start_time = []
    exit_time = []
    temp_time = 0
    seq_pro = []
    final_pre.sort(key=lambda x: x[1])
    while flag == 1:
        second_queue = []
        queue = []
        for i in range(len(final_pre)):
            if final_pre[i][1] <= temp_time and final_pre[i][3] == 0:
                second_queue.append(final_pre[i])
            elif final_pre[i][3] == 0:
                queue.append(final_pre[i])

        if len(second_queue) != 0:
            second_queue.sort(key=lambda x: x[2])
            start_time.append(temp_time)
            temp_time += 1
            e_time = temp_time
            exit_time.append(temp_time)
            seq_pro.append(second_queue[0][0])
            for k in range(len(final_pre)):
                if final_pre[k][0] == second_queue[0][0]:
                    break
            final_pre[k][2] = final_pre[k][2] - 1
            if final_pre[k][2] == 0:
                final_pre[k][3] = 1
                final_pre[k].append(e_time)

        elif len(second_queue) == 0 and len(queue) == 0:
            break

        if len(second_queue) == 0:
            if temp_time < queue[0][1]:
                temp_time = queue[0][1]
            start_time.append(temp_time)
            temp_time += 1
            exit_time.append(temp_time)
            seq_pro.append(queue[0][0])
            for i in range(len(final_pre)):
                if final_pre[i][0] == queue[0][0]:
                    break
            final_pre[i][2] = final_pre[i][2] - 1
            if final_pre[i][2] == 0:
                final_pre[i][3] = 1
                final_pre[i].append(e_time)

    for i in range(len(final_pre)):
        duration = final_pre[i][5] - final_pre[i][1]
        total_duration += duration
        waiting_time = duration - final_pre[i][4]
        total_waiting_time += waiting_time
        final_pre[i].append(waiting_time)

    t_duration = e_time
    plotting(seq_pro,t_duration,start_time)

    average_waiting_time = total_waiting_time / len(final_pre)
    return average_waiting_time

def FindAvgWaitingSJFNonpre(process_data):
    start_time = []
    exit_time = []
    sequence_of_process = []
    burst_time = []
    s_time = 0
    e_time = 0
    k = 0
    process_data.sort(key=lambda x: x[1])

    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][3] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            burst_time.append(ready_queue[0][2])
            start_time.append(s_time)
            s_time = s_time + ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            sequence_of_process.append(process_data[k][0])
            process_data[k][3] = 1
            process_data[k].append(e_time)

        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            burst_time.append(ready_queue[0][2])
            start_time.append(s_time)
            s_time = s_time + normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            sequence_of_process.append(process_data[k][0])
            process_data[k][3] = 1
            process_data[k].append(e_time)

    total_duration = e_time
    plottingNon(sequence_of_process, total_duration, start_time, burst_time)

    w_time = calculateWaitingTime(process_data)
    return w_time


def calculateWaitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][4] - process_data[i][2] - process_data[i][1]
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