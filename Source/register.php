<?php
	session_start();
	
	$dbhost = "127.0.0.1";
	$dbuser = "root";
	$dbpass = "root";
	$errMsg = "";
	
	$conn = mysql_connect($dbhost,$dbuser,$dbpass);
	
	if(! $conn) //if not connected
	{
		die('Could not connect to db'.mysql_error());
	}
	
	mysql_select_db("windguard"); //select database
	
	//validate
	if(isset($_POST['reg']))
	{
			$email = $_POST['email'];
			$userType = "User";
			$username  = $_POST['username'];
			$password  = $_POST['password'];
			$title = $_POST['title'];
			
			
			//select user query
			$sqlQuerry = "INSERT INTO users VALUES ( '$email', '$userType', '$username', '$password', '$title')";
			mysql_query($sqlQuerry);
			
			$_SESSION ['userIdInTable']   = $email;
			$_SESSION ['userNameInTable'] = $username;
			$_SESSION ['userTypeInTable'] = $userType;
			
			echo '<script>';
			echo 'location.href="../home.html"';
			echo '</script>';
			
			
			
	}	
	else{
		$errMsg = 'Error. User email or Passwrod incorrect';
	}
		
	if($errMsg != "")
			{
				echo '<script>';
				echo 'alert("Enter a valid Email or password");';
				echo 'location.href="../index.html"';
				echo '</script>';
			}	

?>