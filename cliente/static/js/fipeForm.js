let dropdownMarcas = $('#marcas-dropdown');

dropdownMarcas.empty();

dropdownMarcas.append('<option selected="true" disabled>Marca do veiculo</option>');
dropdownMarcas.prop('selectedIndex', 0);

let dropdownModelos = $('#modelos-dropdown');

let dropdownAnoModelos = $('#anos-dropdown');

var marcas = []
var marcasFiltradas = [];

var modelos = [];
var modelosFiltrados =  [];

var carDetails = [];
var modelDetails = [];
var lblValor = document.getElementById("valor-fipe");

var valorVeiculo = "";

function dropDownModelosClear()
{
    dropdownModelos.empty();
    modelos = [];
    modelosFiltrados = [];

    dropdownAnoModelos.empty();

}

// Populate dropdown with list of provinces
$.getJSON(url, function (data) {

  $.each(data, function (key, entry) {
        marcas[key] = entry['marca']
  })

  $(marcas).each(function (key, entry){
       if($.inArray(entry, marcasFiltradas) === -1) marcasFiltradas.push(entry);
  });

  $(marcasFiltradas).each(function (key, elemento) {
        dropdownMarcas.append($('<option></option>').attr('value', key).text(elemento));
  });

});

 $("#marcas-dropdown").change(function () {
    carDetails = [];
    modelDetails = [];

    dropDownModelosClear();

    dropdownModelos.append('<option selected="true" disabled>Modelo do veiculo</option>');
    dropdownModelos.prop('selectedIndex', 0);

    $.getJSON(url, function (data) {

      $.each(data, function (key, entry) {

            if($("#marcas-dropdown option:selected").text() == entry['marca'])
            {
                modelos[key] = entry['modelo'];
            }

      })

      $(modelos).each(function (key, entry){
            if($.inArray(entry, modelosFiltrados) === -1) modelosFiltrados.push(entry);
      });

      $(modelosFiltrados).each(function (key, elemento) {
            dropdownModelos.append($('<option></option>').attr('value', key).text(elemento));
      });

    });

 });

  $("#modelos-dropdown").change(function () {

    dropdownAnoModelos.empty();

    dropdownAnoModelos.append('<option selected="true" disabled>Ano do veiculo</option>');
    dropdownAnoModelos.prop('selectedIndex', 0);


    $.getJSON(url, function (data) {

        $.each(data, function (key, entry) {

            if($("#marcas-dropdown option:selected").text() == entry['marca'] && $("#modelos-dropdown option:selected").text() == entry['modelo'])
            {
                dropdownAnoModelos.append($('<option></option>').attr('value', key).text(entry['anomodelo']));
                valorVeiculo = entry['valor'].split(" ")[1];
            }

        });

    });
 });


$("#anos-dropdown").change(function (){
    lblValor.value = valorVeiculo;
});
