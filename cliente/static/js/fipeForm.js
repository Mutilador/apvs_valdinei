let dropdownMarcas = $('#marcas-dropdown');

dropdownMarcas.empty();

dropdownMarcas.append('<option selected="true" disabled>Marca do veiculo</option>');
dropdownMarcas.prop('selectedIndex', 0);

let dropdownModelos = $('#modelos-dropdown');

let dropdownAnoModelos = $('#anos-dropdown');



var modelos;

var lblValor = document.getElementById("valor-fipe");
lblValor.readOnly = true;

var valorVeiculo = "";
var valores = {};
var anos_list = {};

function dropDownModelosClear()
{
    dropdownModelos.empty();
    dropdownAnoModelos.empty();
    valores = {};
}

// Populate dropdown with list of provinces
$.getJSON(url, function (data) {

  $(Object.keys(data)).each(function (key, elemento) {
        dropdownMarcas.append($('<option></option>').prop('value',elemento).text(elemento));
  });

});

 $("#marcas-dropdown").change(function () {
    carDetails = [];
    modelDetails = [];

    dropDownModelosClear();

    dropdownModelos.append('<option selected="true" disabled>Modelo do veiculo</option>');
    dropdownModelos.prop('selectedIndex', 0);

    $.getJSON(url, function (data) {

      $.each(Object.keys(data), function (key, entry) {

            if($("#marcas-dropdown option:selected").text() == entry)
            {
                modelo = Object.keys(data[entry]);
                $.each(Object.keys(data[entry]), function (key2, entry2) {
                    dropdownModelos.append($('<option></option>').prop('value',entry2).text(entry2));
                });

            }
      });
    });

 });

  $("#modelos-dropdown").change(function () {

    dropdownAnoModelos.empty();

    dropdownAnoModelos.append('<option selected="true" disabled>Ano do veiculo</option>');
    dropdownAnoModelos.prop('selectedIndex', 0);

    $.getJSON(url, function (data) {

      $.each(Object.keys(data), function (key, entry) {

            if($("#marcas-dropdown option:selected").text() == entry)
            {
                $.each(Object.keys(data[entry]), function (key2, entry2) {

                    if($("#modelos-dropdown option:selected").text() == entry2)
                    {
                        valores = Object.values(data[entry][entry2]['valor']);
                        anos_list = Object.values(data[entry][entry2]['anomodelo']);
                        $.each(Object.values(data[entry][entry2]['anomodelo']), function (key3, entry3) {
                            dropdownAnoModelos.append($('<option></option>').prop('option', entry3).text(entry3));
                        });
                    }
                });

            }
      });
    });

 });

 function retornaValor(id)
 {
    count = 0;
    id_count = 0;

    $(anos_list).each( function (key, year) {
        if (year == id)
        {
            id_count = count;
        }
        count += 1;
    });
    return valores[id_count];
 }


$("#anos-dropdown").change(function (){

    lblValor.value = retornaValor($("#anos-dropdown option:selected").val());
});
