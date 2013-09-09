$(function() {

	function ajaxSuccess (res) {
		$("#status").addClass("status-success").html("Successfully Update!");
		window.setTimeout(function(){
								$("#status").removeClass("status-success").html("");
							}, 2000);		
	}

	function ajaxFail (res) {
		$("#status").addClass("status-fail").html("Update Failed!");
		window.setTimeout(function(){
								$("#status").removeClass("status-fail").html("");
							}, 2000);			
	}

	function updateTODO (e) {
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
				success: function(res){
					ajaxSuccess(res);
					if(new_todo === ""){
						$("#"+k).parent().parent().remove();
						// update the todo-ids
						// otherwise it may fail when creating new todo
						// because of the todo-idx in todo-ids
			/*Fail, bacause the todo-id-* in $(".todo").contentEditable() don't change
						$(".todo-text").each(function(index) {
							$(this).attr("id", "todo-id-" + index);
						});
						$(".done_div").each(function(index) {
							$(this).attr("id", "check-todo-id-" + index);
						});
			*/	
						window.setTimeout(function(){
												location.reload();
											}, 500);
					}
				},
				//error: ajaxFail,
			});
		};
	}

	function updateCheck (obj) {
		console.log(obj);
		var id = obj.target.id;
		tgt = $("#" + id);
		console.log(tgt);
		if (tgt.hasClass("todo-done")) {
			tgt.removeClass("todo-done");
		} else {
			tgt.addClass("todo-done");
		};
		var tid = $("div.todo").attr("tid");
		var td_idx = id.match(/\d+/g)[0];
		var checked = tgt.hasClass("todo-done") ? "y" : "n";
		var todo_id = id.replace(/check-/g, "", id)
		$.ajax({
			type: "POST",
			url: "/update",
			data: {
				tid: tid,
				td_idx: td_idx,
				new_todo: $('#'+todo_id).html(),
				checked: checked,
			},
			success: ajaxSuccess,
			//error: ajaxFail,
		});	
	}

	$(".todo").contentEditable().change(updateTODO);

	$(".done_div").click(updateCheck);

	$("#add-todo-div .btn").click(function () {
		var li_html = '	<li class="list-group-item"> \
							<div class="list-item-wrapper"> \
								<div id="p1" class="done_div"></div> \
								<div id="p2" class="todo-text" contenteditable="true"></div> \
							</div> \
						</li>';
		var newNode = $('<div/>').html(li_html);
		var last_id = $('.todo-text :last').attr('id');
		var mat = last_id.match(/\d+/g);
		var num = parseInt(mat[0], 10);
		newNode.find('#p2').attr('id', 'todo-id-'+ (num+1));
		newNode.find('#p1').attr('id', 'check-todo-id-'+ (num+1));
		$(".todo ul").append(newNode.child);
		newNode.find('li :first').insertAfter($('.todo .list-group-item :last'))
		$(".todo li :last").contentEditable().change(updateTODO);
		$(".done_div :last").click(updateCheck);
	});

	$("#logo").click(function () {
		window.location.href = "/";
	})
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

