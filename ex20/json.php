<pre>
<?php
//Array
$a = array();
$a[] = array("name"=>"sam", "age"=>26);
$a[] = array("name"=>"cat", "age"=>16);
var_dump($a);

//Array -> JSON:File
file_put_contents('data.json', json_encode($a));

//File:JSON -> Array
$b = json_decode(file_get_contents('data.json'), true);
var_dump($b);
?>
</pre>

