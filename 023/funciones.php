<?php 
$cnx = mysqli_connect( 'localhost', 'root', '', 'test_paginador_buscador');
$cant_por_pagina = 10;

function buscar( $que = NULL, $pagina = 1 ){
	global $cnx, $cant_por_pagina;
	
	$where = is_null( $que ) ? '' : " WHERE NOMBRE LIKE '%$que%' ";
	$inicio = ( $pagina - 1 ) * $cant_por_pagina;
	$consulta = "SELECT * FROM listado $where ORDER BY NOMBRE LIMIT $inicio, $cant_por_pagina";
	
	$registros = [ ];
	$filas = mysqli_query( $cnx, $consulta );
	while( $r = mysqli_fetch_assoc( $filas ) ){
		$registros[] = $r;
	}

	$consulta2 = "SELECT COUNT(*) AS CANTIDAD FROM listado $where";
	$filas2 = mysqli_query($cnx, $consulta2 );
	$array = mysqli_fetch_assoc($filas2);
	$paginas = ceil( $array['CANTIDAD'] / $cant_por_pagina );

	return [ 'resultados' => $registros, 'paginas' => $paginas, 'actual' => $pagina ];
}




