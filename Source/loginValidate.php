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
	if(isset($_POST['loginSubmit']))
	{
			$login_userEmail = $_POST['userid'];
			$login_userPass  = $_POST['password'];
			
			//select user query
			$sqlQuerry = " select * from users where userId = '$login_userEmail' and password = '$login_userPass' ";
			$retVal = mysql_query($sqlQuerry);
			$data = mysql_fetch_array($retVal);
			
			if(mysql_num_rows($retVal) > 0){
				
				$userIdInTable = $data['userId'];
				$userNameInTable = $data['userName'];
				$userTypeInTable = $data['userType'];
				
				$_SESSION ['userIdInTable']   = $userIdInTable;
				$_SESSION ['userNameInTable'] = $userNameInTable;
				$_SESSION ['userTypeInTable'] = $userTypeInTable;
				
				
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
		
		
		
	}
	if(isset($_GET['id'])){
		$_SESSION ['userIdInTable'] = '';
		$_SESSION ['userNameInTable'] = '';
		$_SESSION ['userTypeInTable'] = '';
		
		echo '<script>';
		echo 'location.href="../index.html"';
		echo '</script>';
	}
?>