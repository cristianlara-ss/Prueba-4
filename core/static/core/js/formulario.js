function validar(){
    var nombres, apellidos, correo, numero, motivo;
    nombres = document.getElementById("nombres").value;
    apellidos = document.getElementById("apellidos").value;
    correo = document.getElementById("correo").value;
    numero = document.getElementById("numero").value;
    motivo = document.getElementById("motivo").value;

    if(nombres && apellidos && correo && numero && motivo ){
        if(numero.length == 8){
            alert("En breve se te contactara");
            window.location = "index.html";
            return false;
        }
        else{
            alert('El numero debe contener 8 digitos');
        }
    }
    else{
        alert('Todos los campos son obligatorios');
    }

}
