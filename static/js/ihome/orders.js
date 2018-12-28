//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $(".order-comment").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-comment").attr("order-id", orderId);
    });

    $.ajax({
        url:'/order/get_my_order/',
        type:'GET',
        dataType:'json',
        success:function(data){
            $.each(data['order'], function(index, order){
                 $('.create_time').html('创建时间：' + data['order'].create_time),
                 $('.begin_date').html('入住日期：' + data.order.begin_date),
                 $('.end_date').html('离开时间：' + data.order.end_date),
                 $('.amount').html('合计金额：' + data.order.amount + '元' + '（共' +data.order.days + '晚)'),
                 $('.status').html('订单状态：' + data.order.status)
            })
        },
    })

});