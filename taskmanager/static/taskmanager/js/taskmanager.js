$("a").on('focusout.dropdown.data-api', '.dropdown-menu', function(e) {
    var $this = $(this)
    setTimeout(function() {
        if (!$(document.activeElement).is($this.find("a"))) {
            $this.parent().removeClass('open')
            $this.parent().find('[data-toggle=dropdown]').attr('aria-expanded', 'false')
        }
    }, 150)
});
