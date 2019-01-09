#!/usr/bin/env python
# The above is needed to tell the terminal in which environment to run the code.
from Exscript.util.start import quickstart
from Exscript import Account, Host
import time, getpass


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


switch = 'ssh://' + raw_input("What is the IP address of the switch? ")



quickstart(switch, power_cycle, max_threads=2) # calling the start function to take all variables and input into reboot_device function.