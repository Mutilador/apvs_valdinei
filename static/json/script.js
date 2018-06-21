console.clear();

$(".tab-veiculos ul").find("li > a").eq(0).click();

var carros = [];

$("#selectMarcacarro option").each(function(cKey, option) {
    if ($(this).html() != "") {
    	var carKey = carros.length;

        carros[carKey] = {
            "nome": $(this).html(),
            "id": $(this).val(),
            "modelos": []
        };
	}
});

$.each(carros, function(carKey, carInfo) {
	$("#selectMarcacarro").val(carInfo.id).trigger("change");

	$("#selectAnoModelocarro option").each(function(mKey, optModelo) {
		if ($(this).html() != "") {
			var modeloKey = carros[carKey].modelos.length;
    		carros[carKey].modelos[modeloKey] = {
    			'modelo': $(this).html(),
    			'id': $(this).val(),
    			'anos': []
    		};

    		$("#selectAnoModelocarro").val(carros[carKey].modelos[modeloKey].id).trigger("change");

    		$("#selectAnocarro option").each(function() {
    			if ($(this).html() != "") {
    				var yearKey = carros[carKey].modelos[modeloKey].anos.length;

    				carros[carKey].modelos[modeloKey].anos[yearKey] = {
    					'ano': $(this).html(),
    					'id': $(this).val(),
    				};
    			}
    		});
    	}
	});
});

console.log(JSON.stringify(carros));