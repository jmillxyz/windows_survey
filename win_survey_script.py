import wmi
import os
import sys
import timeit

c = wmi.WMI()

def osCheck():
    osLevel = 0
    for os in c.Win32_OperatingSystem ():
        print "----------------------------------"
        print "|         Operating System       |"
        print "----------------------------------"
        print "Caption: " + os.Caption
        print "Version: " + os.Version
        osLevel = os.Version[:3]
        print "Checking modules specific to",
    options = {
        "6.3" : win63,
        "6.2" : win62,
        "6.1" : win61,
        "6.0" : win60,
        "5.2" : win52,
        "5.1" : win51,
        "5.0" : win50
    }
    options[osLevel]()

def win63():
    print "Windows 8.1 and Server 2012 R2"

def win62():
    print "Windows 8 and Server 2012"

def win61():
    print "Windows 7 and Server 2008 R2"

def win60():
    print "Windows Vista and Server 2008"

def win52():
    print "Windows XP 64-bit, Server 2003, and Server 2003 R2"

def win51():
    print "Windows XP 32-bit"

def win50():
    print "Windows 2000"

def processes():    
    print ""    # space out from osCheck()
    print "----------------------------------"
    print "|         Tasklist               |"
    print "----------------------------------"
    a = os.popen("tasklist").read()
    print a
    tasklistLines = str(a).splitlines()
    print("Tasklist Processes: " + str(len(tasklistLines) - 5)), # Subtract 5: 3 for header, 1 each for cmd.exe and tasklist.exe    
    print " (excluding final cmd.exe and tasklist.exe)"
    print ""
    print "----------------------------------"
    print "|       WMIC Process List        |"
    print "----------------------------------"
    wmicCount = 0
    for p in c.Win32_Process():
        print(str(p.ProcessID) + '\t\t' + p.Caption)
        wmicCount += 1
    print ""
    print("WMIC Processes: " + str(wmicCount))
    
def hardware():
    print "hardware"
        
def main():
    start = timeit.default_timer()
    
    osCheck()
    processes()
    hardware()
    
    stop = timeit.default_timer()
    print stop - start

if __name__ == "__main__":
    main()

