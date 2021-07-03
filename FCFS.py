from chart1 import plottingNon

def FindAvgWaitingFCFS(process, n):
    sequence_of_process = []
    burst_time = []
    process.sort(key=lambda x: x[2])
    for i in range(n):
        sequence_of_process.append(process[i][0])
        burst_time.append(process[i][1])

    wait_time = []
    start_time = []
    total_waitingTime = 0


    for i in range(n):
        if i == 0:
            start_time.append(process[i][2])
        elif (start_time[i-1]+process[i-1][1]) < process[i][2]:
            start_time.append (process[i][2])
        else:
            start_time.append(start_time[i-1] + process[i-1][1])

        wait_time.append(start_time[i] - process[i][2])

        total_waitingTime += wait_time[i]
    e_time = start_time [n-1] + process[n-1][1]
    plottingNon (sequence_of_process, e_time, start_time, burst_time)
    w_time = total_waitingTime / n
    return w_time