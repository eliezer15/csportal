$(document).ready(function() {

	if ($('div.info h1').html() == " Get Hired ") {
		$('a.hired').addClass('current');
	}

	var offset = 420;
	var offsetbottom = $('div.footer').offset().top - 900;
	console.log(offsetbottom);
	var duration = 200;
	jQuery(window).scroll(function() {
		if (jQuery(this).scrollTop() > offsetbottom) {
			jQuery('.back-to-top').fadeOut(duration);
		} else if (jQuery(this).scrollTop() > offset) {
			jQuery('.back-to-top').fadeIn(duration);
		} else {
			jQuery('.back-to-top').fadeOut(duration);
		}

	});

	jQuery('.back-to-top').click(function(event) {
		event.preventDefault();
		jQuery('html, body').animate({
			scrollTop : 0
		}, duration);
		return false;
	})
	
	$('div.filteroptions input.updatebtn').click(function(){
	$('div.filteroptions input').each(function(){
	this.checked ? sessionStorage.setItem(this.value, true) : sessionStorage.removeItem(this.value);
	});

	$('div.filteroptions select').each(function(event) {
		console.log(event.currentTarget.value.substr(0,str.indexOf(' ')));
	});
	});
	
	var L = sessionStorage.length;
	for(var i = 0; i < L; i ++){
		$('div.filteroptions input.'+sessionStorage.key(i)).prop("checked", true);
		console.log(sessionStorage.key(i));
	}

	$('div.newform').find('input').addClass('form-control');
	$('div.newform').find('input').css('width', '100%');
	$('div.newform').find('select').addClass('form-control');
	$('div.newform').find('select').css('width', '100%');
	$('div.newform').find('textarea').addClass('form-control');
	$('div.newform').find('textarea').css('width', '100%');
	
    $(function () {
        $("[rel='tooltip']").tooltip();
    });
    if ($(document).height() == $(window).height()) {
    	$('div.footer').css('position','absolute');
    	$('div.footer').css('bottom','0');
    }
});