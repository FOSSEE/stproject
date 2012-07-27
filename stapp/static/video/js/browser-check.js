$(document).ready(function(){
    var root = document.URL
    if(($.browser.msie) && ($.browser.version <=6)){
        window.location=root+"/browser-version"
    }
    if(($.browser.mozilla) && (parseInt($.browser.version) <3)){
        window.location=root+"/browser-version"
    }
    if(($.browser.webkit) && (parseInt($.browser.version <=530))){
        window.location=root+"/browser-version"
    }
});

