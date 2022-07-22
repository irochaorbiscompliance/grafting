<?php
$pdo = new PDO('sqlite:database.db');
$statement = $pdo->query("SELECT * FROM products");
$rows = $statement->fetchAll(PDO::FETCH_ASSOC);
echo "<pre>";
$result = array_intersect_assoc($rows);
//var_dump($rows);
print_r($result);
echo "</pre>";