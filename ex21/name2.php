<?php
if ($_POST["func"] == "create") {
     $data = array("func"=>$_POST["func"],
                 "name"=>$_POST["name"],
                 "age"=>$_POST['age'] );
     error_log(print_r($data, true));
    
     $name = array();
     if (file_exists("name.json")) {
         $json = file_get_contents('name.json');
         $name = json_decode($json, true);
     }
     $name[$_POST["name"]] = $_POST['age'];
     file_put_contents("name.json",
                       json_encode($name));
    
     die(json_encode($data));
}

if ($_POST["func"] == "list") {
     error_log(print_r($_POST, true));
    
     $list = array();
     if (file_exists("name.json")) {
         $list = json_decode(
               file_get_contents('name.json'),
               true);
     }
     error_log(print_r($list, true));
     die(json_encode($list));
}

die($_POST["func"]." is not exist");

?>

