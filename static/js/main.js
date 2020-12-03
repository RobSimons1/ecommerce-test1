// Script to highlight active page in navbar to help user navigation. used with CSS #navbar .active {} //

$(function () {
    $('a').each(function () {
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
    });
});


// When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar //

$(document).ready(function () {
    var previousScroll = 0;
    $(window).scroll(function () {
        var currentScroll = $(this).scrollTop();
        if (currentScroll < 100) {

        } else if (currentScroll > 0 && currentScroll < $(document).height() - $(window).height()) {
            if (currentScroll > previousScroll) {
                hideNav();
            } else {
                showNav();
            }
            previousScroll = currentScroll;
        }
    });

    function hideNav() {
        $(".navbar").removeClass("is-visible").addClass("is-hidden");
    }

    function showNav() {
        $(".navbar").removeClass("is-hidden").addClass("is-visible").addClass("scrolling");
    }
});

