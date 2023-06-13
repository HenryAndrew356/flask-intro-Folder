// const ROUTE_BACK="https://6487c4bd0e2469c038fc7b8a.mockapi.io"
const ROUTE_BACK="http://127.0.0.1:5000"

fetch(ROUTE_BACK+"/route_dictionaire",{method:"GET"})
    .then((respuesta)=>{
        return respuesta.json();
    })
    .then((data)=>{
        console.log(data);
    })
    .catch((error)=>{
        console.log(error);
    });

fetch(ROUTE_BACK+"/products",{
    method:"POST",
    body:JSON.stringify({
        name:"Zanahoria",
        precio:1055.55
    }),
    headers:{
        "Content-Type":"application/json",
    }
})
    .then((respuesta)=>{
        return respuesta.json();
    })
    .then((data)=>{
        console.log(data)
    })
    .catch((error)=>{
        console.error(error)
    })