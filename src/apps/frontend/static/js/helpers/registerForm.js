$(document).ready(() => {
    $('#register-form').on('keyup change paste', 'input, select, textarea', function(){
        fname    = $("#firstname")[0].value      !== "";
        sname    = $("#secondname")[0].value     !== "";
        email    = isEmail($("#email")[0].value);
        passwd   = $("#password")[0].value       !== "";
        repasswd = $("#password2")[0].value      !== "";
        check1   = $("#check_before_1")[0].checked;
        check2   = $("#check_before_2")[0].checked;

        formisvalid = (fname && sname && email && passwd && repasswd && check1 && check2);

        $("#submit-btn").prop('disabled', !formisvalid);

        if ($("#password")[0].value !== $("#password2")[0].value) {
            $("#password2")[0].className = "sign-field not-equal-pass";
        } else {
            $("#password2")[0].className = "sign-field";
        }
    });

    function isEmail(email) {
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }
});

