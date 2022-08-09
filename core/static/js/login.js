function change() {

    document.getElementById("email-new").innerHTML = "Email";
    const input = document.getElementById('email');
    input.setAttribute('placeholder', '')

}

function change_senha() {

    document.getElementById("senha-new").innerHTML = "Senha";
    const input = document.getElementById('senha');
    input.setAttribute('placeholder', '')

}



document.addEventListener('mouseup', function(e) {
    var container = document.getElementById('email');
    var senha = document.getElementById('senha');
    if (!container.contains(e.target) && container.value === ""){ 
        container.setAttribute('placeholder', 'Email');
        document.getElementById("email-new").innerHTML = "";
   
    }

    if (!senha.contains(e.target) && senha.value === "") {
        senha.setAttribute('placeholder', 'Senha');
        document.getElementById("senha-new").innerHTML = "";
    }
});
