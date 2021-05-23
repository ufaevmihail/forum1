$(function()
{
   var current_input_tbody = null;
   var error_list = [];
   $('input').on('focus',function()
      {
        current_input_tbody = $(this.parentNode.parentNode.parentNode);
      	var current_input_errors = current_input_tbody.next().find('.errors').find('span');
    		console.log(current_input_errors.length);
        for(var i=0; i<=current_input_errors.length;i++)
        {
        error_list.push($(current_input_errors[i]).text());
        }
        error_list.pop()
//        console.log(error_list);
			});
    $('input').on('change keydown paste input',function()
    {


    })


})