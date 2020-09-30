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
    $(document).on('click', '#update', function (e) {
        $('#update-row').css('display', 'flex');
        $('#update-row-label').css('display', 'flex');
        $('#hide-update').css('display', 'flex');

        $('html, body').animate({
            scrollTop: $("#update-row").offset().top
        }, 2000);
    });

    $(document).on('click', '#hide-update', function (e) {
        $('#update-row').slideUp()
        $('#update-row-label').slideUp()
        $('#hide-update').slideUp()
    });

     $(document).on('click', '#export-references-btn', function (e) {
          setTimeout(
            function () {
               $('#export-success-div').css('display', 'flex');
            }, 2000);

           setTimeout(
            function () {
                 $('#export-success-div').slideUp()
            }, 10000);


    });



      var export_interval = setInterval(function () {
            if ($('.export-success-div').is(':visible')) {

                setTimeout(
                    function () {
                        $('.export-success-div').slideUp();
                    }, 7000);


                clearInterval(export_interval);
            } else {
                // still hidden
                if (Date.now() - startTime > maxTime) {
                    // hidden even after 'maxTime'. stop checking.
                    clearInterval(export_interval);
                }
            }
        },
        100 // 0.1 second (wait time between checks)
    );


})