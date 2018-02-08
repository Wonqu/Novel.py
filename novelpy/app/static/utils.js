function resize(){
    $("body").height((window.innerHeight
                    || document.documentElement.clientHeight
                    || document.body.clientHeight) - 60);
    var bodyH = (window.innerHeight
                    || document.documentElement.clientHeight
                    || document.body.clientHeight);
    if (document.getElementById("id_description") !== null){
        var xs = document.getElementsByClassName("jqte_editor");
        $(xs.item(0)).height((bodyH * 0.9 - 250));
        var children = xs.item(0).childNodes;
        for(var i=0; i < children.length; i+=1) {
            $(children[i]).css('height', 'auto');
        }
    }
}

$(document).ready(function(){

    $('[data-toggle="popover"]').popover({
        trigger : 'hover',
        html : 'true'
    });

    $("[data-toggle='info-popover']").each(function(index, element) {
        var contentElementId = $(element).data().target;
        var contentHtml = $(contentElementId).html();
        $(element).popover({
            content: contentHtml
        });
    });

    if(document.getElementById("id_description") !== null){
        $("#id_description").jqte(
            {
                "source":false
            }
        );
    }

    resize();
});

$(window).resize(function(event){
    resize();
});

$(window).bind("DOMSubtreeModified",function(){
  resize();
});

