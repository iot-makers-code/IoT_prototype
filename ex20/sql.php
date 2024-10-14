<pre>
<?php
$db = new SQLite3('test.db');
$version = $db->querySingle('SELECT SQLITE_VERSION()');
echo $version . " \n";

$db->exec("CREATE TABLE user(name TEXT, age INT)");
$db->exec("INSERT INTO user(name, age) VALUES('sam', 25)");
$db->exec("INSERT INTO user(name, age) VALUES('cat', 15)");

$res = $db->query('SELECT * FROM user');
while ($row = $res->fetchArray()) {
     echo "{$row['name'] } {$row['age'] } \n";
}

$db->exec("DELETE FROM user WHERE name = 'sam'");

$db->exec("DROP TABLE user");
?>
</pre>

