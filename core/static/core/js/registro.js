function registro(){
    var correo1, clave, clave1;
    correo1 = document.getElementById("#correo1")
    clave = document.getElementById("#clave")
    clave1 = document.getElementById("#clave1")

    if(correo1 && clave && clave1){
        if(correo1.includes("@duoc")||correo1.includes("@gmail")||correo1.includes("@outlook")){
            if(clave.length > 8){
                if(clave == clave1){
                    alert("Registrado correctamente");
                    window.location = "index.html";
                    return false;
                }
                else{
                    alert('La contraseña no es igual');
                }
            }
            else{
                alert('La contraseña debe tener al menos 8 digitos');
            }
        }
        else{
            alert('Falta el dominio al correo');
        }
    }
    else{
        alert('Debes completar los campos');
    }
}

function modal(){
    var expReg= /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    var esValido = expReg.test(correomod);
    var clavemod = document.getElementById("clavemod");

    if(esValido == true){
        alert('Te has suscrito')
    }
    else{
        alert('El correo no es valido')
    }
}