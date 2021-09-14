function dragOverHandler(ev) {
    document.querySelector("#drop_zone").className = "dropzone hovering";

    // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
    ev.preventDefault();
}

function dropHandler(ev) {
    console.log('File(s) dropped');

    // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
    ev.preventDefault();

    try {
        var datatTransferFiles = ev.dataTransfer.items;
        console.log(datatTransferFiles);

        if (ev.dataTransfer.files) {
            for (var i = 0; i < ev.dataTransfer.items.length; i++) {
                if (datatTransferFiles[i].kind === 'file') {
                    var file = datatTransferFiles[i].getAsFile();
                    FileUploader(file, i);
                } else  {
                    for (var i = 0; i < ev.dataTransfer.files.length; i++) {
                        var file = ev.dataTransfer.files[i];
                        FileUploader(file, i);
                    }
                }
            }
        }
    }
    catch (e) {
        document.querySelector("#drop_zone").className = "dropzone error";
        console.error(e);
    }

    document.querySelector("#drop_zone").className = "dropzone";
}

function dragLeaveHandler(ev) {
    document.querySelector("#drop_zone").className = "dropzone";
}



function FileUploader (file, index) {

    const fileListBlock = `<div class=\"file-details\"><div class=\"file-progress\"> <span class=\"file-name\"> ${file.name.length > 20 ? (file.name.slice(0, 20) + "...") : file.name} </span><div class=\"progress-bar file_${index}\" id=\"progress-bar\"></div></div></div>`;
    $("#uploadingList").append(fileListBlock);

    var formData = new FormData();
    formData.append("file", file, file.name);

    uploadFormData(formData, file.name, index);
}

function uploadFormData (fd, filename, fileindex) {
    var formData = fd;

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $.ajax({
        xhr: function() {
            var xhr = new window.XMLHttpRequest();
            console.log("xhr started");

            if (xhr.upload) {
                xhr.upload.addEventListener("progress", function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = ((evt.loaded / evt.total) * 100);
                        $(`.progress-bar.file_${fileindex}`).width(percentComplete + '%');
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
            $(`.progress-bar.file_${fileindex}`).width('0%');
        },
        error:function(e){
            console.error(e.statusText);
            $(`.progress-bar.file_${fileindex}`).width('100%');
        },
        success: function(resp){
            $(`.progress-bar.file_${fileindex}`).width('100%');
        }
    });
    
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }