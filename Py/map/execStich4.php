<?php

if (isset($_POST['detectbtn']))
{
	//execute stiching to form 4stiched image maps
	exec("stich4.py");
}

//redirect to home.html
header('Location:../../home.html');

?>
