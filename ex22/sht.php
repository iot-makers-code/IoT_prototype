<?php
if ($_POST["func"] == "create") {
     $t = $_POST["t"];
     $h = $_POST["h"];
     
     if(!file_exists("log")) mkdir("log");
     $logf = 'log/'.date("Ymd").'.csv';
     $contents = date('Y/m/d H:i:s').","
             .$_SERVER['REMOTE_ADDR'].","
             .$t.",".$h."\n";
     file_put_contents($logf, $contents, FILE_APPEND);
     die(json_encode($t."/".$h));
}
?>
