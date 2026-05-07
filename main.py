from pexpect import pxssh
import subprocess

s = pxssh.pxssh()
if not s.login ('yourServer', 'yourID', 'yourPassword'):
    print ("SSH session failed on login.\n")
    print (str(s))
else:
    print ("SSH session login successful!\n")

    # Modify the command so the program does whatever you want
    result = subprocess.run(['ls'], capture_output=True, text=True)
    print(result.stdout)
    result = subprocess.run(['free -h'], capture_output=True, text=True)
    print(result.stdout)
    # Add your subprocess bash commands here
    s.logout()
