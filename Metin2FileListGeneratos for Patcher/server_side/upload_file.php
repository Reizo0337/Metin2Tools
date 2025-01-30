<?php
$upload_dir = './uploads/';
$secret_token = 'REIZONR1';
$response = [];

header('Content-Type: application/json');
// var_dump($headers);
$headers = getallheaders();
$token = isset($headers['Authorization']) ? str_replace('Bearer ', '', $headers['Authorization']) : '';

if ($token !== $secret_token) {
    $response['error'] = "Error: Token inválido.";
    echo json_encode($response);
    exit;
}

$folder = isset($_GET['folder']) && !empty($_GET['folder']) ? $_GET['folder'] : '';

$folder = str_replace(['../', '..\\'], '', $folder);

$upload_path = $upload_dir . $folder;

if (empty($folder)) {
    $upload_path = $upload_dir; 
} else {
    // Si la carpeta contiene subdirectorios, los creamos si no existen
    $folder_path = $upload_dir . $folder;
    if (!is_dir($folder_path)) {
        if (!mkdir($folder_path, 0777, true)) {
            $response['error'] = "Error: No se pudo crear la carpeta '$folder'.";
            echo json_encode($response);
            exit;
        }
    }
}

// Verificar si se subió un archivo
if ($_FILES['file']['error'] == UPLOAD_ERR_OK) {
    $file_name = basename($_FILES['file']['name']);
    $file_path = $upload_path . DIRECTORY_SEPARATOR . $file_name;

    // Depuración: Ver la ruta completa del archivo
    $response['file_path'] = "Archivo se moverá a: $file_path";

    // Mover el archivo subido al directorio deseado
    if (move_uploaded_file($_FILES['file']['tmp_name'], $file_path)) {
        $response['success'] = "Archivo '$file_name' subido exitosamente a '$folder'.";
    } else {
        $response['error'] = "Error: No se pudo mover el archivo.";
    }
} else {
    $response['error'] = "Error: El archivo no se pudo subir. Código de error: " . $_FILES['file']['error'];
}

echo json_encode($response);
var_dump($response);
?>
