<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" 
     content="width=device-width, initial-scale=1.0" />
</head>
<body >
<?php $logf = $_GET['log']; ?>
<h2><?php echo($logf)?></h2>
<pre>
<?php
if (!file_exists($logf)) 
   echo "log is not exist";
else
   echo file_get_contents($logf);
?>
</pre>
</body>
</html>