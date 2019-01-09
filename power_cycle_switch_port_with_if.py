#!/usr/bin/env python
# The above is needed to tell the terminal in which environment to run the code.
from Exscript.util.start import quickstart
from Exscript import Account, Host
import time, getpass, sys

#Declared Functions
def run_job():
    selection = 0
    while (selection >=0 or selection<=4):
        print ('1. Run show int status')
        print ('2. Run show mac address-table')
        print ('3. I know my port and want to restart it now.')
        print ('4. Exit the script')
        selection = int(raw_input('Please select an option: '))
        option_chooser[selection]()



def power_cycle(job, host, conn):
    print("Connecting to Server.")
    conn.execute('terminal length 0') #sets terminal to not require the spacebar to read all info

    conn.execute('show int status')
    print conn.response
    print('\r')
    port_name = raw_input('Which port would you like to restart?  i.e. gi1/0/1 ')

    conn.execute('config t\r') #enters config mode
    conn.execute('int ' + port_name)
    conn.execute('\r')  # execute a carriage return to confirm choice
    print('Taking down switch port: ' + port_name)
    conn.execute('shutdown\r') #takes port down
    print('Waiting 30 seconds before bring port back online.')
    time.sleep(30)
    conn.execute('no shutdown\r') # brings port back up
    print('The port should now be back up!')
    time.sleep(5) #pause 1 second


    conn.send('exit\r')  #exits the session
    conn.close() # waits for the connection to close

def show_int(job, host, conn): #This function runs the show show int status function
    print("Connecting to Server.\r")
    time.sleep(1)
    conn.execute('terminal length 0') #sets terminal to not require the spacebar to read all info

    conn.execute('show int status')
    print conn.response
    print('\r')


    conn.send('exit\r')  #exits the session
    conn.close() # waits for the connection to close

def show_mac(job, host, conn): #This function runs the show mac address-table command
    print("Connecting to Server.\r")
    time.sleep(1)
    conn.execute('terminal length 0') #sets terminal to not require the spacebar to read all info

    conn.execute('show mac address-table')
    print conn.response
    print('\r')


    conn.send('exit\r')  #exits the session
    conn.close() # waits for the connection to close



def option_1():
    quickstart(switch, show_int, max_threads=2)
    run_job()
def option_2():
    quickstart(switch, show_mac, max_threads=2)
    run_job()
def option_3():
    quickstart(switch, power_cycle, max_threads=2)  # calling the start function to take all variables and input into reboot_device function.
    run_job()
def option_4():
    print('Ending the Power Cycle script. All connections will be terminated.')
    time.sleep(2)
    sys.exit()


option_chooser = {
    1: option_1,
    2: option_2,
    3: option_3,
    4: option_4
}


#Main Program
switch = 'ssh://' + raw_input("What is the IP address of the switch? ")

run_job() #runs chooser job



