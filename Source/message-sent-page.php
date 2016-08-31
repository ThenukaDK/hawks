<?php
	session_start();
	
	
	mysql_connect("localhost","root","root") or die("not cncted");
	mysql_select_db('windguard') or die("Not connected to the db") or die("not concted");

	if(isset($_POST['userMsg'])){
		$userId=$_SESSION['userIdInTable'];
		$userName = $_GET['userName'];
		$message=$_POST['message'];
		$subject=$_POST['subject'];
		$messageId=uniqid();
		$dateTime=date('Y-m-d H:i:s');


		$sql ='INSERT INTO messages VALUES('.'"'.$messageId.'","'.$userId.'","'.$userName.'","'.$subject.'","'.$message.'","","","'.$dateTime.'")';
		$reslt=mysql_query($sql);
		
		header("Location:../pages/charts/messages.html");
	}
	
	if(isset($_POST['adminReply'])){
		
		$userNameInTable = $_GET['userNameInTable'];
		$userId = $_GET['userId'];
		$messageId = $_GET['messageId'];
		$reply = $_POST['reply'];

		$query = "update sf_messages set reply='$reply' where messageId='$messageId' and userId='$userId'";
		mysql_query($query) or die('Error!: '.mysql_error());
		
		header("Location:../../views/adminPanelViewMessages.php");
	}





?>