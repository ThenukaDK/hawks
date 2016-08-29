<?php

if (isset($_POST['detectbtn']))
{
	exec("stich4.py");
}

header('Location:../../home.html');

?>
