jQuery(function ($) {
    $('input[type="file"]').change(function (e) {
        var fileName = e.target.files[0].name;
        $('.selected-file-div').css('display', 'inline-block');
        $('#selected-file-lbl').html('You selected a file: ' + fileName + '.');

        setTimeout(
            function () {
                //$('.selected-file-div').css('display', 'none');
                $('.selected-file-div').fadeOut();
            }, 10000);
    });

    var maxTime = 5000, // 5 seconds
        startTime = Date.now();


     var success_interval = setInterval(function () {
            if ($('.success-div').is(':visible')) {


                setTimeout(
                    function () {
                        $('.success-div').fadeOut();
                    }, 5000);


                clearInterval(success_interval);
            } else {
                // still hidden
                if (Date.now() - startTime > maxTime) {
                    // hidden even after 'maxTime'. stop checking.
                    clearInterval(success_interval);
                }
            }
        },
        100 // 0.1 second (wait time between checks)
    );

    var interval = setInterval(function () {
            if ($('.error-div').is(':visible')) {


                setTimeout(
                    function () {
                        $('.error-div').fadeOut();
                    }, 5000);


                clearInterval(interval);
            } else {
                // still hidden
                if (Date.now() - startTime > maxTime) {
                    // hidden even after 'maxTime'. stop checking.
                    clearInterval(interval);
                }
            }
        },
        100 // 0.1 second (wait time between checks)
    );

})