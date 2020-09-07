jQuery(function ($) {

    $('input[type="file"]').change(function (e) {
        var fileName = e.target.files[0].name;
        $('.selected-file-div').css('display', 'inline-block');
        $('#selected-file-lbl').html('You selected a file: ' + fileName + '.');

        setTimeout(
            function () {
                //$('.selected-file-div').css('display', 'none');
                $('.selected-file-div').slideUp();
            }, 10000);
    });

    var maxTime = 5000, // 5 seconds
        startTime = Date.now();


    var success_interval = setInterval(function () {
            if ($('.success-div').is(':visible')) {
                setTimeout(
                    function () {
                        $('.success-div').slideUp();
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
                        $('.error-div').slideUp();
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

    //reference edit toggle
    $(document).on('click', '#update-reference', function (e) {
        $('#update-reference-row').css('display', 'flex');
        $('#update-reference-row-label').css('display', 'flex');
        $('#hide-update-reference').css('display', 'flex');

        $('html, body').animate({
            scrollTop: $("#update-reference-row").offset().top
        }, 2000);
    });

    $(document).on('click', '#hide-update-reference', function (e) {
        // $('#update-reference-row').css('display', 'none');
        // $('#update-reference-row-label').css('display', 'none');
        // $('#hide-update-reference').css('display', 'none');
        $('#update-reference-row').slideUp()
        $('#update-reference-row-label').slideUp()
        $('#hide-update-reference').slideUp()
    });


})