$(function()
{
    bind_func($('.button'))
    /*$('.art_element, .r_element').on("click",function()
    {
        var href = $(this).attr('href');
        window.location.href = href;
    });*/
    var prevElement = null;
    $('.element').on("mouseover",function()
    {
        //Hiding previously active element
        //prevElement && $(prevElement).stop().animate({backgroundColor:'#4E1402'}, 1000);
        //$(prevElement).stop().animate({backgroundColor:'#DCDCDC'},600);
        //var curElement = $(this)
        $(this).stop().animate({backgroundColor:'#EE82EE'}, 450);
        prevElement = $(this);
        $(this).css( 'cursor', 'pointer' );
    });
    $('.element').on("mouseout",function()
    {
        $(prevElement).stop().animate({backgroundColor:'#DCDCDC'},450);
        prevElement = null;
    });
    $('.element').on("click",function()
    {
        var href = $(this).attr('href');
        window.location.href = href;
    });

});


function bind_func(obj)
{
    var prevElement = null;
    obj.on("mouseover",function()
    {
        $(this).stop().animate({backgroundColor:'#696969',color:'#FFFFFF'}, 450);
        prevElement = $(this);
        $(this).css( 'cursor', 'pointer' );
    });
    obj.on("mouseout",function()
    {
        $(prevElement).stop().animate({backgroundColor:'#FFFFFF',color:'#000000'},450);
        prevElement = null;
    });
    /*$('.art_element, .r_element').on("click",function()
    {
        var href = $(this).attr('href');
        window.location.href = href;
    });*/

}