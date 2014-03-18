$(document).ready(function() {

	/*
	 * This event handler is assigned to each of the individual post links in
	 * the index page if clicked, we prevent the default action, and call the
	 * post.get ajax function through the Dajaxice library, and with it we pass
	 * the id of the post being requested to be displayed
	 */

	$('body').on('click', 'a.postLinks', function(event) {
		event.preventDefault();
		Dajaxice.post.get(post_callback, {
			'p_id' : $(this).attr("href")
		});
	});

	$(document).scroll(function() {
		$.cookie('document', $(document).scrollTop());
	});

	$('div.post_bar').scroll(function() {
		if ($('div.post_bar').length) {
			$.cookie('post_bar', $('div.post_bar').scrollTop());
		}
	});

	if ($.cookie('document')) {
		$(document).scrollTop($.cookie('document'));
	}

	if ($.cookie('post_bar')) {
		$('div.post_bar').scrollTop($.cookie('post_bar'));
	}

});

/*
 * This function handles the enter button being pressed while in a form if the
 * action was not prevented from default, django would process the form as a url
 * and errors would be displayed. So instead, we get the onlick function that is
 * pressented in the buttons and call that function, which is what the user
 * intended to do by pressing enter
 */

$(document).keypress(
		function(e) {
			if (e.which == 13) {
				e.preventDefault();
				if ($('body').hasClass('modal-open')) {
					var click = $('div.modal-footer button.btn-danger').attr(
							"onclick");
					var fn = window[click.replace("();", "")];
					fn();
				} else {
					var click = $('#contentDiv input.btn').attr("onclick");
					var fn = window[click.replace("();", "")];
					fn();
				}
			}
		});

/*
 * This function is the callback function for the post ajax function called
 * above This will make sure the contentDiv is empty, and then append the post
 * data to it which is a json string of the rendered template from django
 */

function post_callback(data) {
	$('div.post_bar').empty();
	$('div.post_bar').addClass('postBar');
	$('div.post_bar').removeClass('post_bar');
	$('div.postBar').empty();
	$('div.postBar').append(data['post']);
}

/*
 * This function is called when the Add Post button is pressed the function will
 * properly call the newpost method in the ajax.py file the newpost_callback
 * parameter is the name of the function that will handle the call back from the
 * server
 */

function call_newpost() {
	Dajaxice.new_post.get(newpost_callback);
}

/*
 * This function is the callback function for newpost above this will handle the
 * rendered template string from django and append it to the contextDiv,
 * stlyeinputs is called because django tempalte tags do not give the ability to
 * customize inputs.
 */
function newpost_callback(data) {
	$('div.post_bar').empty();
	$('div.post_bar').addClass('postBar');
	$('div.post_bar').removeClass('post_bar');
	$('div.postBar').empty();
	$('div.postBar').append(data['form']);
	styleInputs();
}

/*
 * This method is called when the user is in the create post form view it is
 * called when the user clicks the Create Post button, we promptly grab the
 * post_form object and searlize its values to be send to the val_post function
 * in the ajax.py file. This function uses Dajax, and so it will not have a
 * callback function.
 */

function new_post() {
	Dajaxice.Tutor.val_post(Dajax.process, {
		'form' : $('#post_form').serialize(true)
	});
}

/*
 * This function is called when a user clicks the edit button in a post We grab
 * the id of the post and send it over to the edit_post_pass function in the
 * ajax.py file.
 */

function call_passView() {
	var id = $('#id').html();
	Dajaxice.edit_post_pass.get(passView_callback, {
		'p_id' : id
	});
}

/*
 * This function handles the callback function for the passView call it
 * appropriately handles the rendered string passed to it through ajax.
 */

function passView_callback(data) {
	$('div.post_bar').empty();
	$('div.post_bar').addClass('postBar');
	$('div.post_bar').removeClass('post_bar');
	$('div.postBar').empty();
	$('div.postBar').append(data['pass']);
}

/*
 * This function is called when the user has entered a password to be validated
 * We grab the id of the post wanting to be edited the and the password value
 * entered. The checkpass will handle the response.
 */

function call_checkPass() {
	var value = $('div.postBar input').val();
	var id = $('div.postBar span').html();
	Dajaxice.check_pass.post(checkPass_callback, {
		'p_id' : id,
		'passw' : value
	});
}

/*
 * This function handles the response from the server for checking the provided
 * password if the password is valid, the form to edit the post is rendred and
 * posted to the content div if not valid, the proper error message is posted.
 */

function checkPass_callback(data) {
	if (data['form']) {
		$('div.postBar').empty();
		$('div.postBar').append(data['form']);
		styleInputs();
	}
	if (data['Error']) {
		$('div.errors').remove();
		$('div.postBar')
				.append(
						"<div class='errors' style='color: red;'>You have entered an incorrect password.</div>");
	}
}

/*
 * This method is called when the user clicks the Update Post button We grab the
 * form and id of the object being updated and send it to the server
 */

function update_post() {
	Dajaxice.update_post.post(update_post_callback, {
		'form' : $('#post_form').serialize(true),
		'p_id' : $('#pid').html()
	});
}

/*
 * This function handles the response from the server when an update form is
 * sent to be validated, if the form is valid then the user is redirected to the
 * index page. Else the rendered error form is sent as a string through json and
 * then injected into the contentDiv
 */

function update_post_callback(data) {
	if (data['form']) {
		$('div.postBar').empty();
		$('div.postBar').append(data['form']);
		styleInputs();
	}
	if (data['posted']) {
		$('div.postBar').empty();
		$('div.postBar').append("<h1>Form has been updated.</h1>");
		location.reload();
	}
}

/*
 * This function is called when the delete button is pressed in the delete modal
 * window It grabs the given password and id of the post being requested to be
 * deleted and sends it to the delete_post ajax function in the ajax.py file,
 * the call bakc is handled by delete_post_callback
 */

function delete_post() {
	var pid = $('#dpid').html();
	var value = $('#id_DelPassword').val();
	Dajaxice.delete_post.post(delete_post_callback, {
		'p_id' : pid,
		'passw' : value
	});
}

/*
 * This function handles the callback from the delete post function/ajax call
 * from django and above This will check whether the password was verified, if
 * it was then the json object send from the server will contain a 'deleted'
 * fielded, we check for it hide the modal and empty the div and reload the page
 * for the user. Else the 'deleted' field will not exist in the json and we will
 * have a 'error' message meaning the password was not correct, so we attach the
 * appropriate error message to the modal window.
 */

function delete_post_callback(data) {
	if (data['deleted']) {
		$('#myModal').modal('hide')
		$('div.postBar').empty();
		$('#contentDiv').append("<h1>Post has been deleted.</h1>");
		location.reload();
	}
	if (data['error']) {
		$('div.modal-body div.errors').remove();
		$('div.modal-body')
				.append(
						"<div class='errors' style='color: red;'>You have entered an incorrect password.</div>");
	}
}

/*
 * This function enables us to add bootstrap styling to the inputs of forms
 * which is not allowed to be done through djangos forms manipulation and
 * rendering
 */

function styleInputs() {
	$('div.postBar').find('input').addClass('form-control');
	$('div.postBar').find('input').css('width', '70%');
	$('div.postBar').find('select').addClass('form-control');
	$('div.postBar').find('select').css('width', '70%');
	$('div.postBar').find('textarea').addClass('form-control');
	$('div.postBar').find('textarea').css('width', '70%');
}