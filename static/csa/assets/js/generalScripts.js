$(document).ready(function() {
/*    $('.editable').editable(function(value, settings) {
        console.log(this);
        console.log(value);
        console.log(settings);

        return (value);
    }, {
        event: "click",
            style: "inherit",
            onblur: "submit",
            height:($("div#div_1.editable").width() + 20) + "px", //THIS DOES THE TRICK
            height:($("div#div_1.editable").height() + 5) + "px", //THIS DOES THE TRICK
            cssclass:'onedit',
            placeholder: "Click to set text",
            tooltip: "Click to update"
    });
   $("div").focusout(function(){
        $(this).css("background-color", "red");
    });*/
$.fn.textWidth = function(text, font) {
    if (!$.fn.textWidth.fakeEl) $.fn.textWidth.fakeEl = $('<span hidden>').appendTo(document.body);
    var htmlText = text || this.val() || this.text();
    htmlText = $.fn.textWidth.fakeEl.text(htmlText).html(); //encode to Html
    htmlText = htmlText.replace(/\s/g, "&nbsp;"); //replace trailing and leading spaces
    $.fn.textWidth.fakeEl.html(htmlText).css('font', font || this.css('font'));
    return $.fn.textWidth.fakeEl.width();
};
});
