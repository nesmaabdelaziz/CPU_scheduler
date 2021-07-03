import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

colors = ['red', 'green', 'blue', 'purple', 'black', 'orange', 'gray', 'pink', 'yellow', 'navy','violet', 'maroon']

def plottingRR(sequence_of_process, total_duration, start_time, exit_time):
# declaration
	global colors
	fig, gnt = plt.subplots()
	fig.canvas.set_window_title('Grantt Chart')
	gnt.set_title('Grantt Chart')

	gnt.set_ylim(0, 60)
	gnt.set_xlim(0, total_duration+2)

	gnt.set_xlabel('Process Time')
	gnt.set_ylabel('Processor')

	patch =[]

	for i in range(len(colors)):
		patch.append(mpatches.Patch(color=colors[i], label=f'Process #{i + 1}'))
	plt.legend(handles=patch, loc='upper right', borderaxespad=0., ncol = 3)

	# Setting ticks on y-axis
	gnt.set_yticks([0, 20, 40, 60])
	gnt.set_yticklabels(['', '', '', ''])

	gnt.grid(True)

	for i in range(len(sequence_of_process)):
		gnt.broken_barh([(start_time[i], exit_time[i] - start_time[i])], (20,20),
							color = colors[sequence_of_process[i]])


	plt.show()

def plotting(seq_pro,total_duration,start_time):
	# declaration
	global colors
	fig, gnt = plt.subplots()
	fig.canvas.set_window_title('Grantt Chart')
	gnt.set_title('Grantt Chart')

	gnt.set_ylim(0, 60)
	gnt.set_xlim(0, total_duration + 2)

	gnt.set_xlabel('Process Time')
	gnt.set_ylabel('Processor')

	patch = []

	for i in range(len(colors)):
		patch.append(mpatches.Patch(color=colors[i], label=f'Process #{i + 1}'))
	plt.legend(handles=patch, loc='upper right', borderaxespad=0., ncol = 3)

	# Setting ticks on y-axis
	gnt.set_yticks([0, 20, 40, 60])
	gnt.set_yticklabels(['', '', '', ''])

	gnt.grid(True)

	for i in range(len(seq_pro)):
		gnt.broken_barh([(start_time[i], 1)], (20,20),
							color = colors[seq_pro[i]])


	plt.show()

def plottingNon(sequence_of_process, total_duration, start_time, burst_time):
# declaration
	global colors
	fig, gnt = plt.subplots()
	fig.canvas.set_window_title('Grantt Chart')
	gnt.set_title('Grantt Chart')

	gnt.set_ylim(0, 60)
	gnt.set_xlim(0, total_duration+2)

	gnt.set_xlabel('Process Time')
	gnt.set_ylabel('Processor')

	patch =[]

	for i in range(len(colors)):
		patch.append(mpatches.Patch(color=colors[i], label=f'Process #{i + 1}'))
	plt.legend(handles=patch, loc='upper right', borderaxespad=0., ncol = 3)

	# Setting ticks on y-axis
	gnt.set_yticks([0, 20, 40, 60])
	gnt.set_yticklabels(['', '', '', ''])

	gnt.grid(True)


	for i in range(len(sequence_of_process)):
		gnt.broken_barh([(start_time[i], burst_time[i])], (20,20),
							color = colors[sequence_of_process[i]])


	plt.show()
