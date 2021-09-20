$(document).ready(() => {
    $("td#edit-file-field").click(function (e) {
        var obj_hash = $(this).attr("data-href");

        $("#edit-popup").css({
            left: this.offsetLeft + 138,
            top: this.offsetTop + 125,
        });

        $("#edit-popup").toggleClass("showing");  

        $("#edit-delete").unbind("click").click(()=>{
            OnDelete(obj_hash);
        });
    });


    function OnDelete (path) {
        var formData = new FormData();
        formData.append("delete_target", path);
        uploadFormData(formData, "/api/v1/delete");
    }

    function OnRenam(path) {
        
    }

    function OnMove (path) {
        
    }


    function uploadFormData (fd, endpoint) {
        var formData = fd;

        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });

        $.ajax({
            url: endpoint,
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
});