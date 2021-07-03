from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PySide2.QtWidgets import *
from Priority import FindAvgWaitingPriorityPre,FindAvgWaitingPriorityNonpre
from RR import RoundRobin
from FCFS import FindAvgWaitingFCFS
from SJF import FindAvgWaitingSJFPre,FindAvgWaitingSJFNonpre

AlgorithmName = "First Come First Serve (FCFS)"
NumOfProcess = 0
process_data = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Algorithm_cmb = QtWidgets.QComboBox(self.centralwidget)
        self.Algorithm_cmb.setGeometry(QtCore.QRect(230, 20, 341, 25))
        self.Algorithm_cmb.addItems(["First Come First Serve (FCFS)","Round Robin (RR)","Preemptive Priority","Non Preemptive Priority","Preemptive Shortest Job First (SJF)","Non Preemptive Shortest Job First (SJF)"])

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Algorithm_cmb.sizePolicy().hasHeightForWidth())
        self.Algorithm_cmb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Algorithm_cmb.setFont(font)
        self.Algorithm_cmb.setCurrentText("")
        self.Algorithm_cmb.setMaxVisibleItems(7)
        self.Algorithm_cmb.setMaxCount(2147483647)
        self.Algorithm_cmb.setIconSize(QtCore.QSize(16, 20))
        self.Algorithm_cmb.setObjectName("Algorithm_cmb")
        self.Algorithm_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Algorithm_lbl.setGeometry(QtCore.QRect(30, 20, 180, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Algorithm_lbl.setFont(font)
        self.Algorithm_lbl.setObjectName("Algorithm_lbl")
        self.NumProcesses_lbl = QtWidgets.QLabel(self.centralwidget)
        self.NumProcesses_lbl.setGeometry(QtCore.QRect(590, 20, 180, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NumProcesses_lbl.setFont(font)
        self.NumProcesses_lbl.setObjectName("NumProcesses_lbl")
        self.ProcessNum_spn = QtWidgets.QSpinBox(self.centralwidget,value = 1, minimum = 1, singleStep = 1)
        self.ProcessNum_spn.setGeometry(QtCore.QRect(790, 20, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ProcessNum_spn.setFont(font)
        self.ProcessNum_spn.setAlignment(QtCore.Qt.AlignCenter)
        self.ProcessNum_spn.setObjectName("ProcessNum_spn")
        self.Submit1_btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.Submit1())
        self.Submit1_btn .setFont(font)
        self.Submit1_btn.setGeometry(QtCore.QRect(920, 10, 150, 40))
        self.Submit1_btn.setObjectName("Submit1_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 60, 930, 460))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ProcessEntry_glo = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ProcessEntry_glo.setContentsMargins(0, 0, 0, 0)
        self.ProcessEntry_glo.setRowMinimumHeight(30,30)
        self.ProcessEntry_glo.setContentsMargins(5, 5, 5, 5)
        self.ProcessEntry_glo.setSpacing(10)
        self.ProcessEntry_glo.setObjectName("ProcessEntry_glo")


        self.Submit2_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Submit2())
        self.Submit2_btn.setFont(font)
        self.Submit2_btn.setGeometry(QtCore.QRect(500, 500, 150, 40))
        self.Submit2_btn.setObjectName("Submit2_btn")
        ###################################################################
        self.Submit2_btn.hide()

        self.Restart_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Restart())
        self.Restart_btn.setFont(font)
        self.Restart_btn.setGeometry(QtCore.QRect(920, 10, 150, 40))
        self.Restart_btn.setObjectName("Restart_btn")

        ###################################################################
        self.Restart_btn.hide()

        #   Process Average Wait Duration Label
        self.AvgWait_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AvgWait_lbl.setGeometry(QtCore.QRect(260, 490, 600, 30))
        self.AvgWait_lbl.setFont(font)
        self.AvgWait_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.AvgWait_lbl.setObjectName("AvgWait_lbl")
        self.AvgWait_lbl.setMaximumSize(16777215, 50)
        self.AvgWait_lbl.hide()


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.Algorithm_cmb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler"))
        self.Algorithm_lbl.setText(_translate("MainWindow", "Scheduling Algorithm"))
        self.NumProcesses_lbl.setText(_translate("MainWindow", "Number of Processes"))
        self.ProcessNum_spn.setPrefix(_translate("MainWindow", "# "))
        self.Submit1_btn.setText(_translate("MainWindow", "Submit"))
        self.Restart_btn.setText(_translate("MainWindow", "Restart"))
        self.Submit2_btn.setText(_translate("MainWindow", "Submit"))



    #   The Function that is Called When Submit 1 Btn is Clicked
    ###########################################################################################
    def Submit1(self):
        global AlgorithmName
        global NumOfProcess
        self.Submit1_btn.hide()
        self.Restart_btn.show()
        AlgorithmName = self.Algorithm_cmb.currentText()
        NumOfProcess = self.ProcessNum_spn.value()
        self.DrawLayout()




    #   The Function that Draws the Layout
    ###########################################################################################
    def DrawLayout(self):
        global AlgorithmName
        global NumOfProcess
        _translate = QtCore.QCoreApplication.translate
        self.Submit2_btn.show()

        #   Process Priority Label
        if (AlgorithmName == "Preemptive Priority") or (AlgorithmName == "Non Preemptive Priority"):
            self.ProcessPriority_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.ProcessPriority_lbl.setFont(font)
            self.ProcessPriority_lbl.setAlignment(QtCore.Qt.AlignCenter)
            self.ProcessPriority_lbl.setObjectName("ProcessPriority_lbl")
            self.ProcessEntry_glo.addWidget(self.ProcessPriority_lbl, 0, 3, 1, 1)
            self.ProcessPriority_lbl.setMaximumSize(16777215, 50)
            self.ProcessPriority_lbl.setText(_translate("MainWindow", "Process Priority"))

        #   Process Arrival Label
        self.ProcessArrival_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessArrival_lbl.setFont(font)
        self.ProcessArrival_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ProcessArrival_lbl.setObjectName("ProcessArrival_lbl")
        self.ProcessEntry_glo.addWidget(self.ProcessArrival_lbl, 0, 1, 1, 1)
        self.ProcessArrival_lbl.setMaximumSize(16777215, 50)
        self.ProcessArrival_lbl.setText(_translate("MainWindow", "Process Arrival Time"))

        #   Process CPU Burst Duration Label
        self.ProcessBurs_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessBurs_lbl.setFont(font)
        self.ProcessBurs_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ProcessBurs_lbl.setObjectName("ProcessBurs_lbl")
        self.ProcessEntry_glo.addWidget(self.ProcessBurs_lbl, 0, 2, 1, 1)
        self.ProcessBurs_lbl.setMaximumSize(16777215, 50)
        self.ProcessBurs_lbl.setText(_translate("MainWindow", "Process CPU Burst Duration"))

        #   Process ID Label
        self.ProcessId_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessId_lbl.setFont(font)
        self.ProcessId_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ProcessId_lbl.setObjectName("ProcessId_lbl")
        self.ProcessEntry_glo.addWidget(self.ProcessId_lbl, 0, 0, 1, 1)
        self.ProcessId_lbl.setMaximumSize(16777215, 50)
        self.ProcessId_lbl.setText(_translate("MainWindow", "Process ID"))

        #   Quantum Label
        if AlgorithmName == "Round Robin (RR)":
            self.Quantum_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.Quantum_lbl.setFont(font)
            self.Quantum_lbl.setAlignment(QtCore.Qt.AlignCenter)
            self.Quantum_lbl.setObjectName("Quantum_lbl")
            self.ProcessEntry_glo.addWidget(self.Quantum_lbl, NumOfProcess+1, 0, 1, 1)
            self.Quantum_lbl.setMaximumSize(16777215, 50)
            self.Quantum_lbl.setText(_translate("MainWindow", "Quantum Time"))

            # Quantum Entry
            self.Quantum_spn = QtWidgets.QSpinBox(self.gridLayoutWidget,value = 0, minimum = 1, singleStep = 1, prefix = "The Quantum Duration is ")
            self.Quantum_spn.setAlignment(Qt.AlignHCenter)
            self.Quantum_spn.setFont(font)
            self.Quantum_spn.setObjectName("Quantum_spn")
            self.ProcessEntry_glo.addWidget(self.Quantum_spn, NumOfProcess+1, 1, 1, 1)



        i=0
        self.TempId_lbl = []
        self.TempArrival_spn = []
        self.TempPriority_spn = []
        self.TempBurst_spn = []

        while i < NumOfProcess:
            #   Process ID Label
            self.TempId_lbl.append(QtWidgets.QLabel(self.gridLayoutWidget))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.TempId_lbl[i].setFont(font)
            self.TempId_lbl[i].setAlignment(QtCore.Qt.AlignCenter)
            self.TempId_lbl[i].setObjectName(f"TempId_lbl{i}")
            self.ProcessEntry_glo.addWidget(self.TempId_lbl[i], i+1, 0, 1, 1)
            self.TempId_lbl[i].setText(_translate("MainWindow", f"# {i + 1}"))

            #   Process Arrival Entry
            #if AlgorithmName != "Round Robin (RR)":
            self.TempArrival_spn.append(QtWidgets.QSpinBox(self.gridLayoutWidget,value = 0, minimum = 0, singleStep = 1, prefix = "The Arrival Time is "))
            self.TempArrival_spn[i].setAlignment(Qt.AlignHCenter)
            self.TempArrival_spn[i].setFont(font)
            self.TempArrival_spn[i].setObjectName(f"TempArrival_spn{i}")
            self.ProcessEntry_glo.addWidget(self.TempArrival_spn[i], i+1, 1, 1, 1)

            #   Process Priority Entry
            if (AlgorithmName == "Preemptive Priority") or (AlgorithmName == "Non Preemptive Priority"):
                self.TempPriority_spn.append(QtWidgets.QSpinBox(self.gridLayoutWidget,value = 1, minimum = 1, singleStep = 1, prefix = "The Priority is "))
                self.TempPriority_spn[i].setAlignment(Qt.AlignHCenter)
                self.TempPriority_spn[i].setFont(font)
                self.TempPriority_spn[i].setObjectName(f"TempPriority_spn{i}")
                self.ProcessEntry_glo.addWidget(self.TempPriority_spn[i], i+1, 3, 1, 1)

            #   Process CPU Burst Entry
            self.TempBurst_spn.append(QtWidgets.QSpinBox(self.gridLayoutWidget,value = 1, minimum = 1, singleStep = 1, prefix = "CPU Burst Duration is "))
            self.TempBurst_spn[i].setAlignment(Qt.AlignHCenter)
            self.TempBurst_spn[i].setFont(font)
            self.TempBurst_spn[i].setObjectName(f"TempBurst_spn{i}")
            self.ProcessEntry_glo.addWidget(self.TempBurst_spn[i], i+1, 2, 1, 1)
            i=i+1





    #   The Function that is Called When Submit 2 Btn is Clicked
    ###########################################################################################
    def Submit2(self):
        self.Submit2_btn.hide()
        self.Restart_btn.show()
        self.ReadValues()

    #   Read Value & Put them in Global Lists
    ###########################################################################################
    def ReadValues(self):
        _translate = QtCore.QCoreApplication.translate
        global AlgorithmName
        global NumOfProcess
        i = 0
        w_time = 0

        if (AlgorithmName == "Preemptive Priority") or (AlgorithmName == "Non Preemptive Priority"):
            for i in range(NumOfProcess):
                temporary = []
                process_id = int(self.TempId_lbl[i].text().replace('# ', ''))
                arrival_time = self.TempArrival_spn[i].value()
                burst_time = self.TempBurst_spn[i].value()
                priority = self.TempPriority_spn[i].value()
                if AlgorithmName == "Preemptive Priority":
                    temporary.extend([process_id, arrival_time, burst_time, priority, 0, burst_time])
                elif AlgorithmName == "Non Preemptive Priority":
                    temporary.extend([process_id, arrival_time, burst_time, priority, 0])
                # '0' is the state of the process. 0 means not executed and 1 means execution complete
                process_data.append(temporary)

            if AlgorithmName == "Preemptive Priority":
                w_time = FindAvgWaitingPriorityPre(process_data)
            elif AlgorithmName == "Non Preemptive Priority":
                w_time = FindAvgWaitingPriorityNonpre(process_data)





        elif (AlgorithmName == "Preemptive Shortest Job First (SJF)") or (AlgorithmName == "Non Preemptive Shortest Job First (SJF)"):
            for i in range(NumOfProcess):
                temporary = []
                process_id = i
                arrival_time = self.TempArrival_spn[i].value()
                burst_time = self.TempBurst_spn[i].value()
                if (AlgorithmName == "Preemptive Shortest Job First (SJF)"):
                    temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
                elif (AlgorithmName == "Non Preemptive Shortest Job First (SJF)"):
                    temporary.extend([process_id, arrival_time, burst_time, 0])
                process_data.append(temporary)
            if AlgorithmName == "Preemptive Shortest Job First (SJF)":
                w_time = FindAvgWaitingSJFPre(process_data)

            elif AlgorithmName == "Non Preemptive Shortest Job First (SJF)":
                w_time = FindAvgWaitingSJFNonpre(process_data)


        elif AlgorithmName == "First Come First Serve (FCFS)":
            for i in range(NumOfProcess):
                temporary = []
                process_id = i
                arrival_time = self.TempArrival_spn[i].value()
                burst_time = self.TempBurst_spn[i].value()
                temporary.extend([process_id, burst_time, arrival_time])
                process_data.append(temporary)
            w_time = FindAvgWaitingFCFS(process_data,NumOfProcess)


        elif AlgorithmName == "Round Robin (RR)":
            Q_time = self.Quantum_spn.value()
            for i in range(NumOfProcess):
                temporary = []
                process_id = i
                arrival_time = self.TempArrival_spn[i].value()
                burst_time = self.TempBurst_spn[i].value()
                temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
                # 0 means not executed
                process_data.append(temporary)
            w_time = RoundRobin(process_data, Q_time)
            #w_time = FindAvgWaitingRoundRobin(process_data)

        self.AvgWait_lbl.setText(_translate("MainWindow", f"The Average Wait time is {w_time} Unit time"))
        self.AvgWait_lbl.show()


    #   Restart Code
    ###########################################################################################
    def Restart(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)



#   Main
######################################################################
if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
