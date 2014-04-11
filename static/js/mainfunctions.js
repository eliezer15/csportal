$(document).ready(function() {

	if ($('div.info h1').html() == " Get Hired ") {
		$('a.hired').addClass('current');
	}

	var offset = 420;
	var offsetbottom = $('div.footer').offset().top - 900;
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
    
    /*URI implementation to grab URL search parameters and track user searches. We then select the
     * appropriate selectors/input values in the filterdiv
     */
    var uri = new URI(document.URL);
    if(uri.hasSearch("location")){
    	var search = uri.search(true);
    	for(key in search){
    		if(key == 'post_type'){
    			if(search[key] == 'Interview,Offer'){
    				$('div.filterdiv input[value="Offer"]').prop("checked", true);
    				$('div.filterdiv input[value="Interview"]').prop("checked", true);
    			} else
    			$('div.filterdiv input[value='+search[key]+']').prop("checked", true);
    		} else{
    			$('div.filterdiv select[name="'+key+'"] option[value="'+search[key]+'"]').prop('selected', true);
    		}
    	}
    } else{
    		if(uri.segment(1) == "company"){
    			var name = uri.segment(2).replace("-"," ");
    			$('div.filterdiv select[name="company"] option[value="'+name.toProperCase()+'"]').prop('selected', true);
    		}
    }
});

String.prototype.toProperCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};