$(document).ready(() => {
    var getError = Boolean(getUrlParameter("error"));
    
    if (getError) {
        $("#error-handler-sign").addClass("showing"); 
    } else {
        $("#error-handler-sign").removeClass("showing"); 
    }

    $("#close-error").click(() => {
        $("#error-handler-sign").removeClass("showing"); 
        
        var locUrl = (location.href).split("?")[0].split("/")[3];
        window.history.pushState({}, document.title, "/" + locUrl);
    });
});
