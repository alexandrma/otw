<?php
//$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
//echo $cookie;
//$eli=array("showpassword"=>"no", "bgcolor"=>"#ffffff");
//$key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

//print_r($eli);
//echo $key;
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";

function xor_encrypt($in) {
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
print $key;
print strlen($key);
 $text = $in;
    $outText = '';  
  
    // Iterate through each character  
    for($i=0;$i<strlen($text);$i++) {  
    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
    }  
  
    return $outText;  
}  
  
//echo xor_encrypt(base64_decode($cookie));  
print $cookie;
print base64_decode($cookie);  
?>
