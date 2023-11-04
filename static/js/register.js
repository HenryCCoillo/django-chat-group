        
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
    });

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
    });

function validateFormLogin() {
    const lgUsername = document.querySelector(".lg-username").value;  
    const lgPassword = document.querySelector(".lg-passwd").value;
    const lgUsernameRegex = /^[a-zA-Z0-9_]+$/;

    if (!lgUsernameRegex.test(lgUsername)) {
        iziToast.error({
            title: 'Error, Nombre de Usuario',
            message: 'El nombre de usuario solo debe contener letras, números y guiones bajos (_).',
            position: 'topCenter'
        });
        return false;
    }
    
    if (lgPassword.length < 1) {
        iziToast.error({
            title: 'Error, Contraseña',
            message: 'Ingrese su contraseña.',
            position: 'topCenter'
        });
        return false;
    }
    
    return true;
    }

function validateFormRegister() {

    const rgUsername = document.querySelector(".rg-username").value;
    const rgPassword = document.querySelector(".rg-passwd").value;
    const rgPasswordConf = document.querySelector(".rg-passwd-conf").value;
    const rgUsernameRegex = /^[a-zA-Z0-9_]+$/;

    if (!rgUsernameRegex.test(rgUsername)) {
        iziToast.error({
            title: 'Error, Nombre de Usuario',
            message: 'El nombre de usuario solo debe contener letras, números y guiones bajos (_).',
            position: 'topCenter'
        });
        return false;
    }

    if (!rgPasswordRegex.test(rgPassword)) {
        iziToast.error({
            title: 'Error, Contraseña',
            message: 'La contraseña debe tener al menos 8 caracteres, una mayúscula y un carácter especial.',
            position: 'topCenter'
        });
        return false;
    }

    if (rgPassword !== rgPasswordConf) {
        iziToast.error({
            title: 'Error, Contraseña',
            message: 'Las contraseñas no coinciden.',
            position: 'topCenter'
        });
        return false;
    }
                
    return true;
}
