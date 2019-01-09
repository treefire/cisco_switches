#!/usr/bin/env python
# The above is needed to tell the terminal in which environment to run the code.
from Exscript.util.start import quickstart, start
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

def second_run_job():
    print ('You are currently connected to switch: ' + switch_ip)
    print ('\r')
    selection = 0
    while (selection >=0 or selection<=4):
        print ('1. Run show int status')
        print ('2. Run show mac address-table')
        print ('3. I know my port and want to restart it now.')
        print ('4. Change to a different switch.')
        print ('5. Exit the script')
        selection = int(raw_input('Please select an option: '))
        second_option_chooser[selection]()

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


def get_switch_ip():
    global switch_ip, switch, accounts
    switch_ip = raw_input("What is the IP address of the switch? \r")
    switch = 'ssh://' + switch_ip
    accounts = [Account('admin', 'vtpass#')]
    return switch_ip, switch, accounts


def exit_script():
    print ('\r')
    print('Ending the switch management script. All connections will be terminated.')
    time.sleep(2)
    sys.exit()


def option_1():
    print ('\r')
    quickstart(switch, show_int, max_threads=2)
    second_run_job()
def option_2():
    print ('\r')
    quickstart(switch, show_mac, max_threads=2)
    second_run_job()
def option_3():
    print ('\r')
    quickstart(switch, power_cycle, max_threads=2)  # calling the start function to take all variables and input into reboot_device function.
    second_run_job()
def option_4():
    exit_script()

def second_option_1():
    print ('\r')
    start(accounts, switch, show_int, max_threads=2)
    second_run_job()
def second_option_2():
    print ('\r')
    start(accounts, switch, max_threads=2)
    second_run_job()
def second_option_3():
    print ('\r')
    start(accounts, switch, power_cycle, max_threads=2)  # calling the start function to take all variables and input into reboot_device function.
    second_run_job()
def second_option_4():
    print ('\r')
    get_switch_ip()
    run_job()
def second_option_5():
    exit_script()

option_chooser = {
    1: option_1,
    2: option_2,
    3: option_3,
    4: option_4
}

second_option_chooser = {
    1: second_option_1,
    2: second_option_2,
    3: second_option_3,
    4: second_option_4,
    5: second_option_5
}


#Main Program
get_switch_ip()
run_job() #runs chooser job



