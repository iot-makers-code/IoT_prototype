<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" 
     content="width=device-width, initial-scale=1.0" />
</head>
<body >
<?php $id = $_GET['id']; ?>
<h2><?php echo($id)?></h2>
<div>
<?php
$files = glob("log/".$id."*.csv", GLOB_BRACE);
foreach($files as $file) {
   echo ('<a href="view2.php?log/'. $file.'>'
         .$file.'</a><br>');
}
?>
</pre>
</body>
</html>