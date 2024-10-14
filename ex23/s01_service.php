<?php
$services['test'] ='_test';
function _test() {
     error_log(__FILE__.":".__FUNCTION__);
     $cs ="(".$_POST['func'].")".
         $_SERVER['REMOTE_ADDR']."->".
         $_SERVER['SERVER_ADDR'];
     responseJSON($cs, "success");
};
?>

