$(document).ready(() => {
    var dropmenu = $("#profile-dropmenu")[0];

    $("#profile-container").click(() => {
        if (dropmenu.className.split(" ").includes("showing-menu")) {
            dropmenu.className = "profile-dropmenu";
        } else {
            dropmenu.className = "profile-dropmenu showing-menu";
        }
    });

    $("#profile-dropmenu").mouseleave(() => {
        dropmenu.className = "profile-dropmenu";
    });

});