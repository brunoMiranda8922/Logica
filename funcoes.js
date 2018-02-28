function devolveUmNumeroDecimal(texto){
    return parseFloat(prompt(texto).replace(",", "."));

}

function formatarNumero(resposta, numeroCasas){
    return resposta.toFixed(numeroCasas).replace(".", ",");
   
}

function formatarGrana(resposta){
    return formatarNumero(resposta, 2);
}

Array.prototype.contain = function (valor){
    return this.indexOf(valor) >= 0;  
}