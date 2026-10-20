// ==========================
// LOGIN DO SITE
// ==========================


const botao = document.getElementById("btnLogin");
botao.addEventListener("click", fazerLogin);


function fazerLogin(){
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem");
   
    if(email === "teste@email.com" &&
       senha === "Senha123"){


        mensagem.innerText = "Bem-vindo de volta!";
        mensagem.style.color = "green";


    }else{


        mensagem.innerText = "Login inválido";
        mensagem.style.color = "red";


    }


}






// ==========================
// FUNÇÃO DE PAUSA
// ==========================


function esperar(ms){


    return new Promise(resolve =>
        setTimeout(resolve, ms)
    );


}






// ==========================
// COMANDOS DO ROBÔ
// ==========================


async function OPEN(){


    console.log("OPEN site");


    await esperar(1000);
}






async function TYPE(idCampo, texto){


    console.log(`TYPE "${texto}" no campo ${idCampo}`);


    const campo =
        document.getElementById(idCampo);


    campo.value = "";


    for(let letra of texto){


        campo.value += letra;


        await esperar(120);
    }


    await esperar(500);
}






async function CLICK(idBotao){


    console.log(`CLICK no botão ${idBotao}`);


    await esperar(500);


    document.getElementById(idBotao).click();


    await esperar(1000);
}






async function ASSERT_TEXT(textoEsperado){


    const textoTela =
        document.getElementById("mensagem").innerText;


    console.log(
        `ASSERT esperando: "${textoEsperado}"`
    );


    await esperar(700);


    if(textoTela === textoEsperado){


        console.log("ASSERT PASSOU");


    }else{


        console.error("ASSERT FALHOU");
    }
}






// ==========================
// TESTE AUTOMATIZADO
// ==========================


async function testeLoginSucesso(){


    await OPEN();


    await TYPE(
        "email",
        "teste@email.com"
    );


    await TYPE(
        "senha",
        "Senha123"
    );


    await CLICK("btnLogin");


    await ASSERT_TEXT(
        "Bem-vindo de volta!"
    );
}






// ==========================
// EXECUTAR TESTE
// ==========================


testeLoginSucesso();



