<?php	
$id = $_GET['id'];
$t  = $_GET['t'];
$h  = $_GET['h'];
if (!file_exists("log")) mkdir ("log");
$logf =  'log/check.log';
$cotents = date('H/m/d H:i:s')
             ."\t".$t."\t".$h."\t".$id."\n";
file_put_contents($logf, $cotents, FILE_APPEND);
echo "temerature:".$t;
exit();
?>