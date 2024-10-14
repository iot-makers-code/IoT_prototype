<?php
$data = array("name"=>$_POST["name"],
             "age"=>$_POST['age'] );
error_log(print_r($data, true));
die(json_encode($data));
?>

