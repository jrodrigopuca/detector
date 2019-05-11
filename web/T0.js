var imageScaleFactor=0.5;
var outputStride=16;
var flipHorizontal = false;

var image= document.getElementById('foto');

posenet.load().then(function(net){
    return net.estimateSinglePose(image, imageScaleFactor, flipHorizontal, outputStride)
}).then(function(pose){
    console.log(pose);
})