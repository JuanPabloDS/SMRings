function signup(p, value_p, id  ) {
    document.getElementById(String(p)).innerHTML = String(value_p);
    const input = document.getElementById(String(id));
    input.setAttribute('placeholder', '')
}

function comparador (e, var1, value1, value2) {

    if (!var1.contains(e.target) && var1.value === ""){ 
        var1.setAttribute('placeholder', String(value1));
        document.getElementById(String(value2)).innerHTML = "";
    }
}

function signup_nome() {

    signup('nome-up', 'Nome', 'nome')
}
function signup_sobrenome() {

    signup('sobrenome-up', 'Sobrenome', 'sobrenome')
}
function signup_telefone() {

    signup('telefone-up', 'Telefone', 'telefone')
}
function signup_email() {

    signup('email-up', 'Email', 'email')
}
function signup_senha() {

    signup('senha-up', 'Senha', 'senha')
}

document.addEventListener('mouseup', function(e) {
    var nome = document.getElementById('nome');
    var sobrenome = document.getElementById('sobrenome');
    var telefone = document.getElementById('telefone');
    var email = document.getElementById('email');
    var senha = document.getElementById('senha');

    
    comparador(e, nome, 'Nome', 'nome-up')
    comparador(e, sobrenome, 'Sobrenome', 'sobrenome-up')
    comparador(e, telefone, 'Telefone', 'telefone-up')
    comparador(e, email, 'Email', 'email-up')
    comparador(e, senha, 'senha', 'senha-up')

});


