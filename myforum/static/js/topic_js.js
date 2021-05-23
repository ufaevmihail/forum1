$(function(){
    //console.log('ff');
    var containers = $('.comments_container');
    for (var i=0;i<containers.length;i++)
    {
        container = $(containers[i]);

        //console.log(css(container));
        var container_divs =container.children('div');
        if (container_divs.length > 4)
        {

            container_divs.slice(2).hide();
            container.append("<span class='button show_next' status='show'> показать еще </span>");
            bind_func($(container.children('.show_next')));
        }
    }
});


$(function(){
    $(".comment").click(function()
    {
       var id_ = $(this.parentNode).attr("id");
       var class_ = $(this.parentNode).attr("class");
       var old_this = this;
       $.get('commentform', {'id':id_,'class':class_},function(data)
       {
           if ($(".lmao").length)
           {
               $(".lmao").siblings(".comment").show();
               $(".lmao").remove();
           }
           $(old_this).hide();
           $(old_this.parentNode).append(data);
       });
    });
    $('.show_next').click(function()
    {
        self = $(this);
        if (self.attr('status')=='show')
        {
            self.attr('status','hide');
            self.html('скрыть ветвь');
            self.siblings('div').show();
        }
        else
        {
            self.attr('status','show');
            self.html('показать еще');
            self.siblings('div').slice(2).hide();
        }

    });

});

/*function css(a) {
    var sheets = document.styleSheets, o = {};
    for (var i in sheets) {
        var rules = sheets[i].rules || sheets[i].cssRules;
        for (var r in rules) {
            if (a.is(rules[r].selectorText)) {
                o = $.extend(o, css2json(rules[r].style), css2json(a.attr('style')));
            }
        }
    }
    return o;
}
function css2json(css) {
    var s = {};
    if (!css) return s;
    if (css instanceof CSSStyleDeclaration) {
        for (var i in css) {
            if ((css[i]).toLowerCase) {
                s[(css[i]).toLowerCase()] = (css[css[i]]);
            }
        }
    } else if (typeof css == "string") {
        css = css.split("; ");
        for (var i in css) {
            var l = css[i].split(": ");
            s[l[0].toLowerCase()] = (l[1]);
        }
    }
    return s;
}*/