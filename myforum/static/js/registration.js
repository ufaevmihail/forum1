var requirments = {'user_name':[(text)=>check_length(text,4)],'email':[is_email],
'password':[(text)=>check_length(text,8),has_A,has_9],'password_confirm':[is_password_same]}
var back_requirments= {'user_name':[is_login_already_exists,],'email':[is_email_already_exists,],
'password':[],'password_confirm':[]}

$(function()
{
   //var current_input_tbody = null;
   //var error_list = [];

   /*$('input').on('focus',function()
      {
        current_input_tbody = $(this.parentNode.parentNode.parentNode);
        var div_errors = current_input_tbody.next().find('.errors');
        add_errors($(this),div_errors);
       });*/
    $('.errors').html("<span style='display:none;'>Заполните это поле<span>");
    var reg_button = $("input[value='register']")
    reg_button.hide()
    $('input').on('paste input focus',function()
    {
        current_input_tbody = $(this.parentNode.parentNode.parentNode);
        var div_errors = current_input_tbody.next().find('.errors');
        add_errors($(this),div_errors);

        var delay = async (ms) => await new Promise(resolve => setTimeout(resolve, ms));
        delay(300).then(function()
        {
        if ($('.errors').text()=='')
        {
            reg_button.show()
        }
        else
        {
            reg_button.hide()
        }
        })
    });
    });
function add_errors(input,div_errors)
{
    div_errors.html("");
    var errors = get_errors(input);

        for(var er in errors)
        {
            div_errors.append(errors[er]);
        }
    if(errors.length == 0)
        {
            back_req_funcs_list = back_requirments[input.attr('name')]
            for (var i in back_req_funcs_list)
                {
                    back_req_funcs_list[i](input,div_errors);
                }
        }
}
function get_errors(input)
{
    text = input.val();
    if (text=="")
        return ['Заполните это поле']
    req_func_list = requirments[input.attr('name')];
    errors=[]
    for(var i in req_func_list)
    {
        res =req_func_list[i](text);
        if (res != true)
            {
                errors.push(res)
            }
    }
    /*if (errors.length==0)
    {
        back_req_funcs_list = back_requirments[input.attr('name')]
        for(var i in back_req_funcs_list)
            {
                res=back_req_funcs_list[i](text);
                if (res != true)
                    {
                        errors.push(res)
                    }
            }
    }*/
    return errors
}

function check_length(text,req_length)
{
    if (text.length >= req_length)
        return true;
    else
        return '<li>слишком мало символов</li><br>'
}

function has_A(text)
{
    var found = text.match('[A-Z]')
    var found1 = text.match('[a-z]')
    if (found != null && found1 != null)
        return true;
    else
        return '<li>должна быть большая буква и малая буква</li><br>'
}
function has_9(text)
{
    var found = text.match('[0-9]')
    if (found != null)
        return true;
    else
        return '<li>должно быть число</li><br>'
}
function is_email(text)
{
        var re = /\S+@\S+\.\S+/;
        if (re.test(text)==true)
            return true
        else
            return "<li>Введите валидный емэил</li><br>"

}
function is_password_same(text)
{
    var text1=$("input[name='password']").val();
    if (text == text1)
        return true
    else
        return "Пароли не совпадают"
}
function is_login_already_exists(input,div_errors)
{
    $.get('check_l/',{'login':text},function(data)
    {

        if (data == 'false')
            {
                var html = div_errors.html();
                div_errors.html(html+'<span>такой логин уже существует</span>')
            }
    })
}
function is_email_already_exists(input,div_errors)
{
    $.get('check_e/',{'email':text},function(data)
    {

        if (data == 'false')
            {
                var html = div_errors.html();
                div_errors.html(html+'<span>такой емэил уже существует</span>')
            }
    })
}
/*$(function()
{
    $.get('test/',function(data)
    {
        console.log(data);
    });
});*/