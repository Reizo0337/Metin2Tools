<?php
// Token
$secret_token = 'REIZONR1';  
// Token
$headers = getallheaders();
$token = isset($headers['Authorization']) ? str_replace('Bearer ', '', $headers['Authorization']) : '';

if ($token !== $secret_token) {
    echo "Error: Token inválido.";
    exit;
}

if (isset($_POST['file_list']) && !empty($_POST['file_list'])) {
    $file_list_path = './file_list.txt';

    if (file_put_contents($file_list_path, $_POST['file_list'])) {
        echo "file_list.txt subido exitosamente.";
    } else {
        echo "Error: No se pudo guardar el file_list.txt.";
    }
} else {
    echo "Error: No se recibió el file_list.";
}
?>
