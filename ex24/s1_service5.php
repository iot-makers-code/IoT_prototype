<?php
$services['test'] ='_test';
function _test() {
     error_log(__FILE__.":".__FUNCTION__);
     $cs ="(".$_POST['func'].")".
         $_SERVER['REMOTE_ADDR']."->".
         $_SERVER['SERVER_ADDR'];
     responseJSON($cs, "success");
};
 
$services['create'] ='_create';
function _create() {
    $ctx = array();
    if(!file_exists("log")) mkdir("log");
    if(file_exists("log/api.json")) {
      $ctx = json_decode(
         file_get_contents("log/api.json"), true);
    }
   
    $sid =$_POST['sid'];
    $api =$_POST['api'];
    $ctx[$sid]=array("sid"=>$sid, "api"=>$api);
    file_put_contents("log/api.json", json_encode($ctx));
    responseJSON($sid, 'success');
};
 
$services['testapi'] ='_testapi';
function _testapi() {
    $api =$_POST['api'];
    $test =$_POST['test'];
    $postdata =http_build_query(
        array(
            'func' => $test
        )
    );
    $opts =array('http' =>
        array(
          'method' => 'POST',
          'header' =>
             'Content-Type: application/x-www-form-urlencoded',
          'content' => $postdata
        )
    );
    $context = stream_context_create($opts);
    $rt =file_get_contents($api, false, $context);
    die($rt);
};

$services['listapi'] ='_listapi';
function _listapi() {
    $ctx = array();
    if(file_exists("log/api.json")) {
       $ctx = json_decode(
           file_get_contents("log/api.json"), true);
    }
    $rt =array_values($ctx);
    responseJSON($rt, 'success');
};

$services['deleteapi'] ='_deleteapi';
function _delteapi() {
    error_log(__FILE__.__FUNCTION__);
    $sid =$_POST['sid'];
    if(!file_exists("log/api.json"))
        responseJSON("nofile", "success");
 
     $old = json_decode(
              file_get_contents("log/api.json"), true);
     $ctx = array();
     forEach($old as$k =>$v) {
         if("x".$sid =="x".$k) continue;
         $ctx[$k]=$v;
     }
     file_put_contents("log/api.json", json_encode($ctx));
     responseJSON($sid, "success");
};

$services['upload'] ='_upload';
function _upload() {
     if($_FILES['file']['error'] >0) {
         responseJSON('An error['
              .$_FILES['file']['error']
              .'] occurred while uploading.');
     }
 
     $file =$_FILES["file"]["name"];
     $file =str_replace(" ","",$file);
     error_log("file name ".$file);
     if(!file_exists("media")) mkdir("media");
     if(!move_uploaded_file($_FILES['file']['tmp_name'],
             'media/'.$file)) {
         responseJSON('Error uploading file :'
                          .print_r($_FILES, true));
     }
     // Success!
     responseJSON('File uploaded : ['.$file .'].'
                     , 'success');
};

?>

