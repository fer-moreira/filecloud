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

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return typeof sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};