<?php

if (isset($_POST['detectbtn']))
{
	exec("detect_anomalies.py");
}

header('Location:../index.html');

?>
