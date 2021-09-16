$(document).ready(function () {
    let correct1 = false;
    let correct2 = false;
    let correct3 = false;
    let correct4 = false;

    let regEx1 = /^[a-zA-Z][a-zA-Z0-9-\_\.]{5,19}$/;  // - регулярные выражения для проверки логина
    let regEx2 = /^[a-zA-Z0-9_]{8,}$/;  // - регулярные выражения для проверки пароля
    let regEx3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;  // - регулярные выражения для проверки емайла

    $('#login').blur(function () {
        loginX = $('#login').val();
        console.log(loginX)
        if (regEx1.test(loginX)) {
            // - проверка занятости логина
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + loginX,
                success: function (result) {
                    if (result.message === 'занят') {
                        $('#login-mess').html('логин занят');
                        correct1 = false;
                    } else {
                        $('#login-mess').html('');
                        correct1 = true;
                    }
                }
            });
        } else {
            correct1 = false;
            $('#login-mess').html('Логин не соответствует шаблону валидации!');
        }
    });


    $('#pass1').blur(function () {
        pass1X = $('#pass1').val();
        if (regEx2.test(pass1X)) {
            $('#pass1-mess').html('');
            correct2 = true;
            // - проверка занятости пароля
        } else {
            correct2 = false;
            $('#pass1-mess').html('Пароль не соответствует шаблону валидации!');
        }
    });



    $('#pass2').blur(function () {
        pass1X = $('#pass1').val();
        pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            $('#pass2-mess').html('');
            correct3 = true;
            // - проверка занятости пароля
        } else {
            correct3 = false;
            $('#pass2-mess').html('Пароли не совпадают');
        }
    });

    // проверка емайл дз за 10/08
    $('#email').blur(function () {
        emailX = $('#email').val();
        console.log(emailX)
        if (regEx3.test(emailX)) {
            // - проверка занятости почты
            $.ajax({
                url: '/account/ajax_reg',
                data: 'email=' + emailX,
                success: function (result) {
                    if (result.message === 'существует') {
                        $('#email-mess').html('такая почта уже существует');
                        correct3 = false;
                    } else {
                        $('#email-mess').html('');
                        correct3 = true;
                    }
                }
            });

        } else {
            correct1 = false;
            $('#email-mess').html('Ваша почта не соответствует шаблону валидации!');
        }
    });

    $('#submit').click(function () {
        if (correct1 === true && correct2 === true && correct3 === true && correct4 === true) {
            $('#form1').attr('onesubmit', 'return true');
            alert('Регистрация успешна.');
        } else {
            $('#form1').attr('onesubmit', 'return false');
            alert('Форма содержит некоректные данные\n Отправка данных заблокирована.');
        }
    });

});