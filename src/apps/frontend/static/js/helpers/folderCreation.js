$(document).ready(() => {
    $("#add-folder-btn").click((e) => {
        $("#folder-creator-input").toggleClass("showing");
    });

    $("#make-folder-btn").click(() => {
        var desired_name = $("#folder-name-field").val();

        if (desired_name.length > 4) {
            $("#folder-creator-input").toggleClass("showing");

            var target = getUrlParameter("target");
            
            var formData = new FormData();
            formData.append("new_folder_name", desired_name);
            formData.append("target", target ? target : "public");
            uploadFormData(formData);
        }
    });
    
    function uploadFormData (fd) {
        var formData = fd;

        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });

        $.ajax({
            url: '/api/v1/new-folder',
            type: 'POST',
            data: formData,
            async: true,
            cache: false,
            contentType: false,
            enctype: 'multipart/form-data',
            processData: false,

            error:function(e){
                console.error(e.statusText);
            },

            success: function(resp){
                console.log(resp);
                window.location.reload();
            }
        });
    }
})