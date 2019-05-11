if (window.FaceDetector == undefined){
    console.log('todavia no es soportado el FaceDetector')
}else{
    let imagen = document.getElementById('foto')
    let canvas = document.getElementById('canvas')
    canvas.width=imagen.width;
    canvas.height=imagen.height;

    var ctx= canvas.getContext("2d")
    ctx.drawImage(imagen, 
        0, 0, imagen.width, imagen.height,
        0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = "whitesmoke";


    let fd= new FaceDetector({fastMode:true, maxDetectedFaces:20});

    fd.detect(imagen)
        .then(caras=>{
            for (const cara of caras){
                console.log(cara.boundingBox) // datos de la caja
                ctx.rect(
                    Math.floor(cara.boundingBox.x),
                    Math.floor(cara.boundingBox.y),
                    Math.floor(cara.boundingBox.width),
                    Math.floor(cara.boundingBox.height)
                );
                ctx.stroke();
            }
        }).catch(()=>{
            console.error("falló")
        })
}