$(function()
{
    $(".create_article, .create_rubric").on('click',function()
    {
       var id_ = $(".rubric_main").attr("id");
       var old_this = this;
       var class_ = $(this).attr("class");
       //console.log(class_)
       $.get('createchetotam/'+id_, {'class':class_}, function(data)
       {
           if ($(".lmao").length)
           {
               $(".lmao").siblings(".create_article, .create_rubric").show()
               $(".lmao").remove();
           }
           $(old_this).attr('ff','123');
           console.log($(old_this).ff);
           $(old_this).hide();
           $(old_this.parentNode).append(data);
       });
    });


});


    /*$(".r_element, .art_element").on('mouseenter',function()
    {
        $(this).animate({backgroundColor:'#4E1402'}, 300);
    })
    $(".r_element, .art_element").on('mouseenter',function()
    {
        console.log($(this).css('background-color'));
    })*/
//})

/*$(function(){$(document)}
$(document).keyup(function(e) {
     if (e.key === "Escape") { // escape key maps to keycode '27'
        // <DO YOUR WORK HERE>
    }
});
$(function(){
   // console.log('FFF')
   //var objects = document.getElementsByClassName(value)
    for(var obj in $(".create_article"))
    {
        //console.log($(".create_article"))
       // obj.prop1 = 'fff';
    }
//    console.log($(".create_article")
})*/