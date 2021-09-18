var ItemsUploading = {};


function dragOverHandler(ev) {
    document.querySelector("#dropzone-indicator").className = "dropzone-filter showing-filter";
    ev.preventDefault();
}

function dropHandler(ev) {
    ev.preventDefault();

    $("#uploadingList").attr("class","uploading-list showing");

    try {
        var datatTransferFiles = ev.dataTransfer.items;
        console.log(datatTransferFiles);

        if (ev.dataTransfer.files) {
            for (var i = 0; i < ev.dataTransfer.items.length; i++) {
                console.log(i);

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
        document.querySelector("#dropzone-indicator").className = "dropzone-filter";
        console.error(e);
    }

    document.querySelector("#dropzone-indicator").className = "dropzone-filter";
}

function dragLeaveHandler(ev) {
    document.querySelector("#dropzone-indicator").className = "dropzone-filter";
}



function FileUploader (file, index) {
    var randHash = getRandomHash();
    
    ItemsUploading[`file_${index}_${randHash}`] = false
    
    const fileListBlock = '<div class="upload-item">'+
    '        <div class="upload-item__detail">'+
    '            <div class="item-detail">'+
    `                <div class="item-detail--text" ><img class="rotating" id="image_file_${index}_${randHash}" height="28px" width="28px" src="/static/public/loading.svg" alt=""></div>`+
    `                <div class="item-detail--text" >${file.name.length > 20 ? (file.name.slice(0, 20) + "...") : file.name}</div>`+
    '                <div class="item-detail--text" >|</div>'+
    `                <div class="item-detail--text" >840 kb</div>`+
    '            </div>'+
    '            <div class="item-buttons">'+
    '                <button class="item-buttons--close">x</button>'+
    '            </div>'+
    '        </div>'+
    '        <div class="upload-item__progress-bar">'+
    `           <div class="progress-bar file_${index}_${randHash}" id="progress-bar"></div>`+
    '        </div>'+
    '    </div>';
	
    $("#uploadingList").append(fileListBlock);

    setTimeout(() => {
        var formData = new FormData();
        formData.append("file", file, file.name);

        uploadFormData(formData, index, randHash);
    }, 10);
}

function uploadFormData (fd, fileindex, randHash) {
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
                        $(`.progress-bar.file_${fileindex}_${randHash}`).width(percentComplete + '%');
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
            $(`.progress-bar.file_${fileindex}_${randHash}`).width('0%');
        },
        error:function(e){
            console.error(e.statusText);
            $(`.progress-bar.file_${fileindex}_${randHash}`).width('100%');

            $(`#image_file_${fileindex}_${randHash}`).attr("src","/static/public/error.svg");
            $(`#image_file_${fileindex}_${randHash}`).attr("class","");
        },
        success: function(resp){
            $(`.progress-bar.file_${fileindex}_${randHash}`).width('100%');
            $(`#image_file_${fileindex}_${randHash}`).attr("src","/static/public/checkmark.svg");
            $(`#image_file_${fileindex}_${randHash}`).attr("class","");

            ItemsUploading[`file_${fileindex}_${randHash}`] = true

            setTimeout(() => {
                var values = $.map(ItemsUploading, function(value, key) { return value });
                console.log(values);
                if (values.every(e => e === true)) {
                    window.location.reload();
                }
            }, 300);
        }
    });
    
}

function getRandomHash () {
    return (Math.random() + 1).toString(36).substring(4);
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