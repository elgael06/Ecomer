
let $MI_URL = `${window.location.protocol}//${window.location.hostname}`,
    $URL_MVC = "/Globales/",
    $URL_API = "/api/";

const  login = new Vue({
    el:"#contenido",
    data: {
        usuario:"",
        password:""
    },
    methods: {
        enviar(event){
            if(this.usuario!="" && this.password!="")
            fetch(`${$URL_API}login/?id=${this.usuario}&password=${this.password}`, {
                method: 'get',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .catch(err =>{
                    console.error("Error=>", err)
                    alert("Error De Acceso!!!")
                    })
                .then(res => res.json().then(respuesta => {
                    console.log(respuesta.existe);
                    if(respuesta.existe){
                         location.href ="/";
                         }
                     else{
                        alert("Error De Acceso!!!");
                      }
                })
                .catch(err =>{
                    console.error("Error=>", err)
                    alert("Error De Acceso!!!")
                    })
                )
             else alert("Falta Colocar Usuario y/o Contraseña!!!");
            event.preventDefault();
        }
    },
});