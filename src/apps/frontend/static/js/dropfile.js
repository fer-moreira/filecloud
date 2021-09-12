function dragOverHandler(ev) {
    document.querySelector("#drop_zone").className = "hovering";

    // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
    ev.preventDefault();
}

function dropHandler(ev) {
    console.log('File(s) dropped');

    // Impedir o comportamento padrão (impedir que o arquivo seja aberto)
    ev.preventDefault();


    try {
        if (ev.dataTransfer.items) {
            // Use a interface DataTransferItemList para acessar o (s) arquivo (s)
            for (var i = 0; i < ev.dataTransfer.items.length; i++) {
                // Se os itens soltos não forem arquivos, rejeite-os
                if (ev.dataTransfer.items[i].kind === 'file') {
                    var file = ev.dataTransfer.items[i].getAsFile();
                    console.log(file);
                }
            }
        } else {
            // Use a interface DataTransfer para acessar o (s) arquivo (s)
            for (var i = 0; i < ev.dataTransfer.files.length; i++) {
                var file = ev.dataTransfer.files[i];
                console.log(file);
            }
        }
    }
    catch (e) {
        document.querySelector("#drop_zone").className = "error";
        console.error(e);
    }


    document.querySelector("#drop_zone").className = "";
}

function dragLeaveHandler(ev) {
    document.querySelector("#drop_zone").className = "";
}
