// const ROUTE_BACK="https://6487c4bd0e2469c038fc7b8a.mockapi.io"
const ROUTE_BACK="http:127.0.0.1:5000"

fetch(ROUTE_BACK+"/route_02",{method:"GET"})
    .then((respuesta)=>{
        respuesta.json();   
    })
    .then((data)=>{
        console.log(data);
    })
    .catch((error)=>{
        console.log(error);
    });