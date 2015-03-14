
## To-Do
##  1>auto answer call (done)
##  2>auto answer video call  
##  3>selective answer call
##  >>>>>  Need to integrate with voiceinput
##
##  4>loop scan for login page, then perform login if detected  (done)
##  >>>>>  store login/password in external JAR as a function   (done)
## 
##  5>  auto reject  (done)
##  6>  need boolean to control options (e.g. in reject call mode)  (done)
##  
##  7>  dial out (call skyper node.js)
##  >>>>>  need to handle user list on Skype

## storing Skype login credentials at external Java class
## This Java class has 2 methods, for retreiving skype login and skype password.
## Info is hardcoded in Java class and compiled as Java bytecode.
## Loading from Java class would prevent having login/password stored in
## plain text in this Python script.
##
## Please refer to SkypeCredentials.java for details how to prepare your
## skype login/password info.
##
mypath = "Skype.jar"
load(mypath)
import SkypeCredentials

mypath2 = "voinput_single.jar"
load(mypath2)
import org.voinput.dialog.DialogDemo
voiceinput = org.voinput.dialog.DialogDemo().getDialogDemoInstance()
voiceinput.start()

rejectcall = 0
print "In startup default mode, accept all calls"
while True:
    
    lastCommand = voiceinput.lastMatchedInput()
    print ">>>", lastCommand, "<<<"
    if lastCommand.strip() == "reject":
        print "Reject calls"
        rejectcall = 1
    elif lastCommand.strip() == "answer":
        print "Answer calls"
        rejectcall = 0
     
    if rejectcall == 1:
        print "Current state -- reject calls"
    elif rejectcall == 0:
        print "Current state -- answer calls"

        
    ## detected login screen, perhaps after a restart, then login
    if exists("1425260366156.png"):
        click("1425260366156.png")
        sleep(3)
        #doubleClick("1425949584209.png")
        #type(SkypeCredentials.getLogin())
        #sleep(1)

        click("1425260453448.png")

        type(SkypeCredentials.getPasswd())

        click("1425519724951.png")



    ## auto answer calls
    if exists("1425529755998.png") and rejectcall == 0:
        click("1425529755998.png")
    sleep(10)

    ## auto reject calls 
    if exists("1425875181378.png") and rejectcall == 1:
        click("1425875181378.png")
    sleep(10)
    