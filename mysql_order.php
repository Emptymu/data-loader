<?php

function getRandChar($length){
   $str = null;
   $strPol = "0123456789abcdefghijklmnopqrstuvwxyz";
   $max = strlen($strPol)-1;

   for($i=0;$i<$length;$i++){
    $str.=$strPol[rand(0,$max)];//rand($min,$max)生成介于min和max两个数之间的一个随机整数
   }

   return $str;
  }


$mysql_database = 'test';
$link = mysqli_connect('localhost','root','',$mysql_database); 
if (!$link) { 
	die('Could not connect to MySQL: ' . mysqli_error()); 
}
mysqli_query($link,"set names 'utf8'"); //数据库输出编码

$sql= "insert into benchmark_outorder (theKey,columnA,columnB,filler) values";
for($i=4000000;$i<=5000000;$i++){
$aa = getRandChar(8);
$sql.="(".$i.",".rand(1,50000).",".rand(1,50000).",'".$aa."'),";
};

$sql = substr($sql,0,strlen($sql)-1);

mysqli_query($link,$sql);

echo 'Connection OK'; 
mysqli_close($link); 

?>