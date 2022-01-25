/* navbar active effect */

const url = window.location.pathname;

urlRegExp = new RegExp(url.replace(/\/$/, '') + "$");

$('a').each(function () {
     if (urlRegExp.test(this.href.replace(/\/$/, ''))) {
        if(!$(this).hasClass("disabled")){
            $(this).addClass('active');
        }
    }
});