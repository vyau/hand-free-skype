
This project attemps to automate Skype interaction for voice/video calls. <br>
Instead of using mouse clicks to manage Skype, I integrated this control with <br>
Sphinx4 voice input<br>
This was designed for those with disability and unable to easily control Skype with their hands<br>
<p>

This project relies on Sikuli (http://www.sikuli.org/) which is an open source project. <br>
 Please visit Sikuli for project setup and their licensing terms.<br>

 <p>

 This project has been tested under Ubuntu and Linux Mint which are my primary development platforms<br>
 Since Sikuli is leveraging Java, this should run on other platforms such as Windows or Mac <br>
 Minor tweaks may be needed to make it portable to other platforms <br>
<p>

 Feel free to contact me if you need help to make it run in your environment.<br>
<p>

Files Listing:<br>
<ui>
<li>  PNG files -- these are used by my Sikuli script to identify areas on screen
<li>  skype.html ; skype.py -- these are sikuli scripts.  Sikuli IDE from Sikuli project will
      open and edit them.   
<li> Skype.jar ; SkypeCredentials.java -- This is a helper Java class that stores and produces 
      the needed Skype login/password.  Refer to SkypeCrendential.java for comments
<li> voinput_single -- this is the JAR file that contains custom code for driving voice input logic.
       Refer to my other Github project about voice input:
 
      https://github.com/vyau/voiceinterface
       

</ul>
<p>

<p>
To install and run, execute these steps in order: 
<ul>
<li> 1)  create symbolic link hand-free-skype.py and point to skype.py
         <br>  ln -s skype.py hand-free-skype.py
<li> 2)  Edit SkypeCredentials.java, enter your Skype account login under getLogin().
        <br> For example, if login is "blackbird", 
        <br>  public static String getLogin() {  return "blackbird" ;  }
<li>  3) Edit SkypeCredentials.java, enter your Skype account password under getPasswd().
        <br>  For example, if password is "hello",
        <br>  public static String getPasswd() { return "hello" ; }

<li>  4) Issue this command  "javac SkypeCredentials.java"
</ul> 
<p><br>

Assuming that you have Sikuli installed, to run this program:

 "cd <to the parent directory of hand-free-skype> ; runIDE -r hand-free-skype" <br>
(runIDE is a script provided by Sikuli)
<br> 
<p>
