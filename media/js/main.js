$(function() {
	$(".todo").contentEditable().change(function(e) {
		var tid = $("div.todo").attr("tid");
		console.log(tid);
		for (k in e.changed) {
			td_idx = k.match(/\d+/g)[0];
			new_todo = e.changed[k];
			console.log(td_idx);
			console.log(new_todo);
			var a = document.createElement("div");
			a.innerHTML = new_todo;
			if($.trim($(a).text()) === ""){
				new_todo = "";
			}
			$.ajax({
				type: "POST",
				url: "/update",
				data: {
						tid: tid,
						td_idx: td_idx,
						new_todo: new_todo,
				},
				success: function(result){
					$("#status").addClass("status-success").html("Successfully Update!");
					window.setTimeout(function(){
											$("#status").removeClass("status-success").html("");
										}, 2000);
					if(new_todo === ""){
						$("#"+k).parent().parent().remove();
					}
				},
			});
		};
	});

	$(".done_div").click(function() {
		alert(123);
	});
});

function htmlDecode (input) {
	var a = document.createElement("div");
	a.innerHTML = input;
	return a.childNodes.length === 0 ? "" : a.childNodes[0].nodeValue;
}

function setTodoHTML (escaped_html, div_id) {
//	need 2 times of htmlDecode because there're 2 times of encode:
//	1. POST the todo content to server
//	2. "xhtml_escape" in UpdateHandler
//	console.log(escaped_html);
	html = htmlDecode(escaped_html);
//	console.log(html);
	html = htmlDecode(html);
//	console.log(html);
	$("#" + div_id).html(html);
}

