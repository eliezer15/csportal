$(document).ready(function() {
	
	/*This event handler is assigned to each of the individual post links in the index page
	 * if clicked, we prevent the default action, and call the post.get ajax function through the
	 * Dajaxice library, and with it we pass the id of the post being requested to be displayed
	 */
/*	
	$('body').on('click', 'a.postLink', function(event) {
		event.preventDefault();
		console.log(Dajaxice);
		Dajaxice.post.get(post_callback, {
			'post_id' : $(this).attr("href"),
			'post_type': 1
		});
	});
	
	function post_callback(data) {
		$('#content').empty();
		$('#content').append(data['post']);
	}
*/
});
