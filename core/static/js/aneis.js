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