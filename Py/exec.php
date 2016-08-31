<?php

if (isset($_POST['detectbtn']))
{
	//ececute python class to detect annomalies with cascade
	exec("detect_anomalies.py");
}

//redirect to home
header('Location:../home.html');

?>
