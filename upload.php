<?php 
 if(isset($_POST['submit'])){
    $name       = $_FILES['file']['name'];  
    $temp_name  = $_FILES['file']['tmp_name'];  
    $name2       = $_FILES['file2']['name'];  
    $temp_name2  = $_FILES['file2']['tmp_name'];  
    if(isset($name) && isset($name2)){
        if(!empty($name) && !empty($name2)){ 
            $location = 'uploadfiles/';      
            if(move_uploaded_file($temp_name, $location.$name) && move_uploaded_file($temp_name2, $location.$name2)){
                echo 'File uploaded successfully';
            }
        }       
    }  else {
        echo 'You should select a file to upload !!';
    }
}
?>