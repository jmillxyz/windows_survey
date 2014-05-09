Description
----
This is a survey script - that is, once tasked with surveying a potentially compromised Windows host, use this as one of your first tools to determine what has gone wrong.

Background
----
This was basically born out of my frustration with the WMIC tool for Windows failing to format its output in an acceptable manner. Thus, I have committed to the silly idea of using Python, the Python WMI module, and Py2exe in order to code in Python, access Win32 APIs, and package it all up into an executable runnable on any Windows host.

Usage
----
0) Make sure you have [Python 2.7](https://www.python.org/download/releases/2.7.6/), the [Python WMI module](https://pypi.python.org/pypi/WMI/1.4.9) and [py2exe](http://www.py2exe.org/). If this is your first time installing all of this, you'll probably also need [pywin32 extensions](http://sourceforge.net/projects/pywin32/files/). Other versions of Python may work but this is what works for me.
1) Run the batch script - it will create a 'dist' directory and within it, the win\_survey\_script.exe executable. 
2) Run win\_survey\_script.exe on the compromised machine to determine what's going wrong - it will create a win\_survey\_results.txt in the same directory.