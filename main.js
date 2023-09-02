
const formContainerUser = document.getElementById('form-container');
const loginCorporativo = document.querySelector('.login-corporativo');
const loginUsuario = document.querySelector('.login-usuario');
const container = document.querySelector('.login-container');
const closeButtonForm = document.querySelector('.close-btn-form');
const buttonFormEntrar = document.getElementById('button-form-entrar');

document.getElementById('button-usuario').addEventListener('click', () => {
    loginCorporativo.style.display = 'none'; 
    loginUsuario.style.display = 'flex';
    formContainerUser.style.display = 'flex'; 
      // Move o form para depois do loginUsuario
    container.insertBefore(formContainerUser, loginCorporativo);
});

document.getElementById('button-corporativo').addEventListener('click', () => {
    loginUsuario.style.display = 'none';
    loginCorporativo.style.display = 'flex'; 
    formContainerUser.style.display = 'flex'; 
    // Move o form para antes do loginUsuario
    container.insertBefore(formContainerUser, loginUsuario);
});

function fecharFormulario() {
    formContainerUser.style.display = 'none';
    loginUsuario.style.display = 'none';
    loginCorporativo.style.display = 'none';
    
    container.appendChild(formContainerUser);
}

closeButtonForm.addEventListener('click', fecharFormulario);

