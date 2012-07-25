$(document).ready(function(){
    if(($.browser.msie) && ($.browser.version <=6)){
        window.location="/browser-version"
    }
    if(($.browser.mozilla) && (parseInt($.browser.version) <3)){
        window.location="/browser-version"
    }
    if(($.browser.webkit) && (parseInt($.browser.version <=530))){
        window.location="/browser-version"
    }
});
