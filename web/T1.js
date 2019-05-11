var imageScaleFactor=0.5;
var outputStride=16;
var flipHorizontal = false;
var maxPoseDetections= 6;

var image= document.getElementById('foto');

posenet.load().then(function(net){
    return net.estimateMultiplePoses(image, imageScaleFactor, flipHorizontal, outputStride, maxPoseDetections)
}).then(function(pose){
    console.log(pose);
})
