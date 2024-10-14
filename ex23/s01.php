<?php
error_log( print_r($_POST, true));
function responseJSON($msg, $status ='error') {
     header('Content-Type: application/json');
     die(json_encode(array(
         'data'=>$msg,
         'status'=>$status
     )));
}
 
include_once("s01_service.php");
 
$func = isset($_POST['func'])?$_POST["func"]:"none";
if(!isset($services[$func]))
         responseJSON("No service[$func].");
try{
     call_user_func( $services[$func]);
} catch(Exception $e) {
     responseJSON($e->getMessage());
     error_log(print_r($e->getTrace()));
}
?>

