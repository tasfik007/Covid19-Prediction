console.log("Hello!!");
let base64Image;
$("#image-selector").change(function () {
    let reader = new FileReader();
    reader.onload = function (e) {
        let dataURL = reader.result;
        $("#selected-image").attr("src", dataURL);
        base64Image = dataURL.replace("data:image/jpeg;base64,", "");
        console.log(base64Image);
    }
    reader.readAsDataURL($("#image-selector")[0].files[0]);
    $("#covid-result").text("");
});

$("#predict-button").click(function (event) {
    let message = {
        image: base64Image
    }
    console.log(message);
    $.post("http://127.0.0.1:5000/predict", JSON.stringify(message), function (response) {
        if (response.prediction.covid == "Covid +ve") {
            $("h3").addClass("danger");
            console.log('danger');

        } else {
            $("h3").addClass("safe");
            console.log('safe');

        }
        $("h3").addClass("safe");
        $("#covid-result").text(response.prediction.covid);
        console.log(response);

    });

});