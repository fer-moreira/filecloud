$(document).ready(() => {
    var dropmenu = $("#profile-dropmenu")[0];

    $("#profile-container").click(() => {
        $("#profile-dropmenu").toggleClass("showing-menu");
    });

    $("#profile-dropmenu").mouseleave(() => {
        dropmenu.className = "profile-dropmenu";
    });
});