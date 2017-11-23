<?
$key = "";
#var declaraion
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
#array_key_exists
#
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
