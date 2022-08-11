function tamanho_aneis() {
     var n = 1 
    for (var i = 0; i < 33; i++) {
        document.write('<option value="">', n,'</option>');
        n++;
     } 
}

function remove_item() {
     sessionStorage.removeItem('carrinho', '1')
}


function real_br_money(din) {
     var money = parseInt(din)
     var formate = money.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
     document.write(formate)
}


function total() {
     var valor_total = parseInt(document.getElementById("quantidade").value);
     var valor = parseFloat(document.getElementById("form-submit").value);
     var preco = valor_total * valor;
     var formate = preco.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});

     document.getElementById("valor_total").innerHTML = formate;
     
}

function multi(var_qtd, var_preco) {
     var qtd = parseInt(var_qtd);
     var preco = parseFloat(var_preco);

     total = qtd * preco;
     document.write("R$ ",total);

}

 