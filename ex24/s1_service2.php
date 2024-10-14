<?php
 
$services['test'] ='_test';
function _test() {
# Omit the middle ...
}

$services['create'] ='_create';
function _create() {
# Omit the middle ...
}

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
?>

?>

