<?php
$rec = $_POST['recipient'];
$num = $_POST['num'];
$from = $_POST['fromemail'];
$pass = $_POST['password'];
$sub = $_POST['subject'];
$body = $_POST['body'];
$inter = $_POST['interval'];
$enum = $_POST['enum'];

$wowplskill = shell_exec("python3 emailspam.py -i -t $rec -e $enum -f $from -p $pass -s $sub -b $body -n $num -d $inter");
print("Your emails have been sent");
?>
