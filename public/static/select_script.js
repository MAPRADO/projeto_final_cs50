function refreshModelSelect() {
    var selectBrand = document.getElementById("selectBrand");
    var selectModel = document.getElementById("selectModel");


    // Limpar o segundo select
    selectModel.innerHTML = '';


    // Obter a opção selecionada no select Brand
    var selectedOption = selectBrand.value;


    // Adicionar opções ao select Model baseado na opção selecionada no select Brand
    switch (selectedOption) {
        case "FIAT":
            selectModel.innerHTML += '<option value="MOBI">MOBI</option>';
            selectModel.innerHTML += '<option value="ARGO">ARGO</option>';
            selectModel.innerHTML += '<option value="CRONOS">CRONOS</option>';
            selectModel.innerHTML += '<option value="FASTBACK">FASTBACK</option>';
            selectModel.innerHTML += '<option value="PULSE">PULSE</option>';
            selectModel.innerHTML += '<option value="TORO">TORO</option>';
            break;
        case "Hyundai":
            selectModel.innerHTML += '<option value="HB20">HB20</option>';
            selectModel.innerHTML += '<option value="HB20S">HB20S</option>';
            selectModel.innerHTML += '<option value="CRETA">CRETA</option>';
            break;
        case "PEUGEOT":
            selectModel.innerHTML += '<option value="208">208</option>';
            selectModel.innerHTML += '<option value="2008">2008</option>';
            break;
        case "Renault":
            selectModel.innerHTML += '<option value="Sandero">Sandero</option>';
            selectModel.innerHTML += '<option value="Kwid">Kwid</option>';
            break;
        case "VW":
            selectModel.innerHTML += '<option value="GOL">GOL</option>';
            selectModel.innerHTML += '<option value="NIVUS">NIVUS</option>';
            break;
        case "CHEVROLET":
            selectModel.innerHTML += '<option value="ONIX">ONIX</option>';
            selectModel.innerHTML += '<option value="ONIX (MY24.5)">ONIX (MY24.5)</option>';
            selectModel.innerHTML += '<option value="ONIX PLUS">ONIX PLUS</option>';
            selectModel.innerHTML += '<option value="ONIX PLUS (MY24.5)">ONIX PLUS (MY24.5)</option>';
            selectModel.innerHTML += '<option value="SPIN">SPIN</option>';
            selectModel.innerHTML += '<option value="TRACKER">TRACKER</option>';
            break;
        case "HONDA":
            selectModel.innerHTML += '<option value="CITY">CITY</option>';
            selectModel.innerHTML += '<option value="CITY HATCH">CITY HATCH</option>';
            selectModel.innerHTML += '<option value="HR-V">HR-V</option>';
            break;
        case "CAOA CHERY":
            selectModel.innerHTML += '<option value="TIGGO 5X">TIGGO 5X</option>';
            break;
        case "CITROEN":
            selectModel.innerHTML += '<option value="C4 CACTUS">C4 CACTUS</option>';
            selectModel.innerHTML += '<option value="C3">C3</option>';
            break;
        case "JEEP":
            selectModel.innerHTML += '<option value="RENEGADE">RENEGADE</option>';
            break;
        case "Nissan":
            selectModel.innerHTML += '<option value="Kicks">Kicks</option>';
            break;
        case "LAND ROVER":
            selectModel.innerHTML += '<option value="DISCOVERY SPORT">DISCOVERY SPORT</option>';
            selectModel.innerHTML += '<option value="EVOQUE">EVOQUE</option>'
            break;

        default:
            selectModel.innerHTML += '<option value="">Selecione...</option>';
    }
    refreshMotorSelect();
}


function refreshMotorSelect() {
    var selectModel = document.getElementById("selectModel");
    var selectMotor = document.getElementById("selectMotor");


    // Limpar o terceiro select
    selectMotor.innerHTML = '';


    // Obter a opção selecionada no select Model
    var selectedOption = selectModel.value;

    // Adicionar opções ao select Motor baseado na opção selecionada no select Model
    switch (selectedOption) {
        case "MOBI":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "ARGO":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "CRONOS":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "FASTBACK":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "PULSE":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "TORO":
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "HB20":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "HB20S":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "CRETA":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            selectMotor.innerHTML += '<option value="2.0">2.0</option>';
            break;
        case "208":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "2008":
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "Sandero":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "Kwid":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "GOL":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "NIVUS":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "ONIX":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "ONIX (MY24.5)":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "ONIX PLUS":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "ONIX PLUS (MY24.5)":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            break;
        case "SPIN":
            selectMotor.innerHTML += '<option value="1.8">1.8</option>';
            break;
        case "TRACKER":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.2">1.2</option>';
            break;
        case "CITY":
            selectMotor.innerHTML += '<option value="1.5">1.5</option>';
            break;
        case "CITY HATCH":
            selectMotor.innerHTML += '<option value="1.5">1.5</option>';
            break;
        case "HR-V":
            selectMotor.innerHTML += '<option value="1.5">1.5</option>';
            break;
        case "TIGGO 5X":
            selectMotor.innerHTML += '<option value="1.5">1.5</option>';
            break;
        case "C4 CACTUS":
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "C3":
            selectMotor.innerHTML += '<option value="1.0">1.0</option>';
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "RENEGADE":
            selectMotor.innerHTML += '<option value="1.3">1.3</option>';
            break;
        case "Kicks":
            selectMotor.innerHTML += '<option value="1.6">1.6</option>';
            break;
        case "DISCOVERY SPORT":
            selectMotor.innerHTML += '<option value="2.0">2.0</option>';
            break;
        case "EVOQUE":
            selectMotor.innerHTML += '<option value="2.0">2.0</option>';
            break;
        default:
            selectMotor.innerHTML += '<option value="">Selecione...</option>';
    }
}


document.getElementById("button").addEventListener("submit", function(event){
    event.preventDefault();
    // Aqui você pode adicionar código para processar as seleções do usuário
    var selectBrand = document.getElementById("selectBrand").value;
    var selectModel = document.getElementById("selectModel").value;
    var selectMotor = document.getElementById("selectMotor").value;
    // Exemplo de saída para demonstração
    alert("Seleção do select Brand: " + selectBrand + "\nSeleção do select Model: " + selectModel + "\nSeleção do select Motor:" + selectMotor);
});

