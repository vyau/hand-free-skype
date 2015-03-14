

/**
*  A very simple helper class to hard code Skype login/password.
*  
*  To compile and make ready for Skype automation script:
*
*   1>  javac SkypeCredentials.java
*   2>  jar cvf Skype.jar SkypeCredentials.class
*   
*/

public class SkypeCredentials {
	

	public static String getLogin() {
		return "";
	}

	public static String getPasswd() {
		return "";
	}


	public static void main(String[] args) {
		System.out.println(SkypeCredentials.getLogin());
		System.out.println(SkypeCredentials.getPasswd());
		
	}
}