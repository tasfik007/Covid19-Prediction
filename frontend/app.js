var canvas = document.getElementById('our-canvas'),
    context = canvas.getContext('2d');
uploadedFile = document.getElementById('uploaded-file');
window.addEventListener('DOMContentLoaded', initImageLoader);

function initImageLoader() {
    uploadedFile.addEventListener('change', handleManualUploadedFiles);
    function handleManualUploadedFiles(ev) {
        var file = ev.target.files[0];
        handleFile(file);

    }
}
function handleFile(file) {
    var ImageType = /image.*/;

    if (file.type.match(ImageType)) {

        var reader = new FileReader();

        reader.onloadend = function (event) {
            var tempImageStore = new Image();
            tempImageStore.onload = function (ev) {
                canvas.height = ev.target.height;
                canvas.width = ev.target.width;
                context.drawImage(ev.target, 0, 0);
            }
            tempImageStore.src = event.target.result;
            
        }
        reader.readAsDataURL(file);


    }
}