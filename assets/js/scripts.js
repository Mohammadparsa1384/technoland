$(function() {
    

    /* On Sale Counter */
    function countDown(){
        var today = new Date();
        var eventDate = new Date("November 30,2022 00:00:00"); /* Change This Date To Update Counter */
        var currentTime = today.getTime();
        var eventTime = eventDate.getTime();
        var remTime = eventTime - currentTime;

        var sec = Math.floor(remTime/1000);
        var min = Math.floor(sec/60);
        var hrs = Math.floor(min/60);
        var days = Math.floor(hrs/24);

        hrs %= 24;
        min %= 60;
        sec %= 60;

        days = (days<10) ? "0"+days : days;
        hrs = (hrs<10) ? "0"+hrs : hrs;
        min = (min<10) ? "0"+min : min;
        sec = (sec<10) ? "0"+sec : sec;

        var elTimeCounter = $('.time-counter');
        var elDays = $('.days', elTimeCounter);
        var elHours = $('.hours', elTimeCounter);
        var elMinutes = $('.minutes', elTimeCounter);
        var elSeconds = $('.seconds', elTimeCounter);

        $('.num', elDays).html(days);
        $('.num', elHours).html(hrs);
        $('.num', elMinutes).html(min);
        $('.num', elSeconds).html(sec);

        setTimeout(countDown, 1000);
    }
    countDown();
    /* /On Sale Counter */

    /* Initialize menu */
    $('.droopmenu-navbar').droopmenu({
        dmArrow:true,
        dmArrowDirection:'dmarrowdown'
    });
    /* /Initialize menu */

    /* Featured Products Filter */
    if($('.featured-categories').length) {
        $('.featured-categories').click(function () {
            var category = $(this).data('val');
            $('.featured-product').each(function () {
                if ($(this).hasClass(category))
                    $(this).fadeIn();
                else
                    $(this).fadeOut(0);
            })

            /* Update Active Menu */
            $('.featured-categories').each(function () {
                $(this).removeClass('active');
                if ($(this).data('val') == category)
                    $(this).addClass('active');
            })
        })
        $('.featured-categories').eq(0).trigger('click');
    }
    /* /Featured Products Filter */

    /* Most Sold Products Filter */
    if($('.most-sales-categories').length) {
        $('.most-sales-categories').click(function () {
            var category = $(this).data('val');
            $('.most-sales-product').each(function () {
                if ($(this).hasClass(category))
                    $(this).fadeIn();
                else
                    $(this).fadeOut(0);
            })

            /* Update Active Menu */
            $('.most-sales-categories').each(function () {
                $(this).removeClass('active');
                if ($(this).data('val') == category)
                    $(this).addClass('active');
            })
        })
        $('.most-sales-categories').eq(0).trigger('click');
    }
    /* /Most Sold Products Filter */

    /* Collapse In Mobile */
    if($('.collapse').length) {
        if (($(window).width()) < 992) {
            $('.collapse').removeClass('show');
        }
    }
    /* /Collapse In Mobile */

    /* Num Format Functions */
    function intFormat(number) {
        var regex = /(\d)((\d{3},?)+)$/;
        number = number + '';
        number = number.split(',').join('');

        while(regex.test(number)){
            number = number.replace(regex, '$1,$2');
        }
        return number;
    }

    function numFormat(number) {
        var pointReg = /([\d,\.]*)\.(\d*)$/, f;
        if(pointReg.test(number)){
            f = RegExp.$2;
            return intFormat(RegExp.$1) + '.' + f;
        }
        return intFormat(number);
    }
    /* /Num Format Functions */

    /* Products Carousel */
    if($('.products-carousel').length > 0) {
        var owl = $('.products-carousel');
        owl.owlCarousel({
            rtl: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 25,
            nav: false,
            dots: false,
            loop: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 3
                },
                1000: {
                    items: 4
                }
            }
        })
    }
    /* /Products Carousel */

    /* Product Order Number */
    if($('.btn-plus').length > 0) {
        $('.btn-plus').click(function () {
            var index = $(this).index('.btn-plus');
            var orderNumber = Number($('input.order-number').eq(index).val());
            $('input.order-number').eq(index).val(orderNumber + 1);
        })

        $('.btn-minus').click(function () {
            var index = $(this).index('.btn-minus');
            var orderNumber = Number($('input.order-number').eq(index).val());
            if (orderNumber > 1)
                $('input.order-number').eq(index).val(orderNumber - 1);
        })
    }
    /* /Product Order Number */

    AOS.init();
});

