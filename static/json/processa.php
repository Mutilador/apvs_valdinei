<?php

function call($tabela, $marca, $modelo, $ano, $combustivel) {
	$url = "http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros";

	$ch      = curl_init();
	$timeout = 5;

	$headers = [
		'Pragma: no-cache',
		'Origin: http://veiculos.fipe.org.br',
		'Accept-Encoding: gzip, deflate',
		'Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
		'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
		'Accept: application/json, text/javascript, */*; q=0.01',
		'Cache-Control: no-cache',
		'X-Requested-With: XMLHttpRequest',
		'Cookie: _ga=GA1.3.14956442.1529549542; _gid=GA1.3.953573276.1529549542; nvgc41729=0|0; nvgt41729=1529549543108_1_0|0_0|0; nav41729=896b690ee1b5e0b7bdcc4e87a09|2_173',
		'Connection: keep-alive',
		'Referer: http://veiculos.fipe.org.br/'
	];

	$dados = [
		'codigoTabelaReferencia' => $tabela,
		'codigoMarca' => $marca,
		'codigoModelo' => $modelo,
		'codigoTipoVeiculo' => 1,
		'anoModelo' => $ano,
		'codigoTipoCombustivel' => $combustivel,
		'tipoVeiculo' => 'carro',
		'modeloCodigoExterno' => "",
		'tipoConsulta' => 'tradicional'
	];

	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36');
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($dados));

	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
	$data = curl_exec($ch);
	curl_close($ch);

	return json_decode(strtolower($data), true);
}

$arquivo = "fipe.230.json";

$dados = json_decode(file_get_contents($arquivo), true);

$masterJson = [];

foreach ($dados as $key => $marcas) {
	foreach ($marcas['modelos'] as $mkey => $modelos) {
		foreach ($modelos['anos'] as $akey => $anos) {
			$infoAno = explode("-", $anos['id']);
			$apiData = call(explode(".", $arquivo)[1], $marcas['id'], $modelos['id'], $infoAno[0], $infoAno[1]);

			$masterJson[] = array_merge($apiData, [
				'marca' => $marcas['nome'],
				'modelo' => $modelos['modelo'],
				'valor' => $modelos['valor'],
			]);
		}
	}

	file_put_contents("master.json", json_encode($masterJson));

	echo "Marca {$marcas['nome']} feito!\n";
}