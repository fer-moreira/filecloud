function SubmitFormWithoutRedirect () {
    console.log("Submit form");

    $('#uploadForm').submit(function(e){
        e.preventDefault();
        console.log("prevent default");

        var formData = new FormData($('#uploadForm')[0]);

        $.ajax({
            
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                console.log("xhr started");


                if (xhr.upload) {
                    xhr.upload.addEventListener("progress", function(evt) {

                        console.log("progress");

                        if (evt.lengthComputable) {
                            var percentComplete = ((evt.loaded / evt.total) * 100);
                            $(".progress-bar").width(percentComplete + '%');
                            $(".progress-bar").html(percentComplete.toFixed()+'%');
                        }
                    }, false);

                    return xhr;
                }
            },
            

            url: '/api/v1/uploader',
            type: 'POST',
            data: formData,
            async: true,
            cache: false,
            contentType: false,
            enctype: 'multipart/form-data',
            processData: false,

            beforeSend: function(){
                $(".progress-bar").width('0%');
                $('#uploadStatus').html('<p>Uploading...<img height="32px" width="32px" src="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif"/></p>');
            },
            error:function(e){
                console.error(e.statusText);
                $('#uploadStatus').html('<p style="color:#EA4335;">File upload failed, please try again.</p>');
            },
            success: function(resp){
                $('#uploadForm')[0].reset();
                $('#uploadStatus').html('<p style="color:#28A74B;">File has uploaded successfully!</p>');
            }
        });
    });
}