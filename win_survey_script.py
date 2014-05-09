import wmi
import os
import sys
import subprocess
import timeit
import _winreg

c = wmi.WMI()
r = wmi.Registry()

def osCheck(f):
    for os in c.Win32_OperatingSystem ():
        f.write("----------------------------------\n")
        f.write("|         Operating System       |\n")
        f.write("----------------------------------\n")
        f.write("Caption: " + os.Caption + '\n')
        f.write("Version: " + os.Version + '\n')
        
def network(f):
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|         Network                |\n")
    f.write("----------------------------------\n")
    net = os.popen("ipconfig /all").read()
    f.write(net)
    f.write("\n")
    arp = os.popen("arp -a").read()
    f.write(arp)
    f.write("\n")
    netstat = os.popen("netstat -aon").read()
    f.write(netstat)

def processes(f):    
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|         Tasklist               |\n")
    f.write("----------------------------------\n")
    a = os.popen("tasklist\n").read()
    f.write(a)
    tasklistLines = str(a).splitlines()
    f.write("Tasklist Processes: " + str(len(tasklistLines) - 5)), # Subtract 5: 3 for header, 1 each for cmd.exe and tasklist.exe    
    f.write(" (excluding final cmd.exe and tasklist.exe)\n")
    f.write("" )
    f.write("----------------------------------\n")
    f.write("|       WMIC Process List        |\n")
    f.write("----------------------------------\n")
    wmicCount = 0
    for p in c.Win32_Process():
        f.write(str(p.ProcessID) + '\t\t' + p.Caption + '\n')
        wmicCount += 1
    f.write("\n")
    f.write("WMIC Processes: " + str(wmicCount) + '\n')
    
    
def registry(f):    
    f.write("" )
    f.write("----------------------------------\n")
    f.write("|    Registry - HKLM\Software    |\n")
    f.write("----------------------------------\n")
    reg = os.popen("reg query HKLM\Software\n").read()
    f.write(reg)
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("| Registry - Malicious Locations |\n")
    f.write("----------------------------------\n")
    f.write("Run, Runonce, AppInit_DLLs\n")
    f.write("\n")
    reg2 = os.popen("reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Runonce\n").read()
    f.write(reg2)
    reg3 = os.popen("reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run\n").read()
    f.write(reg3)
    reg4 = os.popen('reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Windows\n"').read()
    f.write(reg4)
    
def prefetch(f):
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|           Prefetch             |\n")
    f.write("----------------------------------\n")
    pre = os.popen("dir C:\WINDOWS\Prefetch\n").read()
    f.write(pre)
    
def scheduledJobs(f):
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|            AT Jobs             |\n")
    f.write("----------------------------------\n")
    at = os.popen("at\n").read()
    f.write(at)
    atList = str(at).splitlines()
    if (len(atList) == 0):
        f.write("\n")
        f.write("No AT jobs\n")
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|           Schtasks             |\n")
    f.write("----------------------------------\n")
    sch = os.popen("dir C:\WINDOWS\Tasks\n").read()
    f.write(sch)
   
   
def loadedModules(f):
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("|        Loaded Modules          |\n")
    f.write("----------------------------------\n")
    lm = os.popen("tasklist /m\n").read()
    f.write(lm)
   
def main():
    start = timeit.default_timer()
    
    f = open('win_survey_results.txt', 'w')
    
    osCheck(f)
    network(f)
    processes(f)
    registry(f)
    prefetch(f)
    scheduledJobs(f)
    loadedModules(f)
    
    f.close()
    
    stop = timeit.default_timer()
    
    print("Total Time: " + str(stop - start))

if __name__ == "__main__":
    main()

