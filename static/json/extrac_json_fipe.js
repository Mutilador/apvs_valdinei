// Abre o formulario para a marca do veiculo

$(".tab-veiculos ul").find("li > a").eq(0).click()

// Lista a marca de todos os carros
var marcaCarros = [];
var modeloCarros = [];
$("#selectMarcacarro option").each('click', function(event) {
	marcaCarros[marcaCarros.length] = {"marca": $(this).html(), "id": $(this).val()};

    $(this).click(function(){
        $("#selectAnoModelocarro_chosen option").each(function(){
            modeloCarros.push({"modelo": $(this).html(), "id": $(this).val()});
        });
    });

});



console.log(JSON.stringify(marcaCarros));
console.log(JSON.stringify(modeloCarros));


selectAnoModelocarro_chosen

selectAnocarro_chosen
