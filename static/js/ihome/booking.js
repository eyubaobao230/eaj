function hrefBack() {
    history.go(-1);
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

function showErrorMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function(){
    $(".input-daterange").datepicker({
        format: "yyyy-mm-dd",
        startDate: "today",
        language: "zh-CN",
        autoclose: true
    });
    $(".input-daterange").on("changeDate", function(){
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();

        if (startDate && endDate && startDate > endDate) {
            showErrorMsg();
        } else {
            var sd = new Date(startDate);
            var ed = new Date(endDate);
            days = (ed - sd)/(1000*3600*24) + 1;
            var price = $(".house-text>p>span").html();
            var amount = days * parseFloat(price);
            $(".order-amount>span").html(amount.toFixed(2) + "(共"+ days +"晚)");
        }
    });

    var url = location.search;
    var id = url.split('=')[1];

    $.ajax({
        url:'/house/booking/' + id + '/',
        type:'GET',
        dataType:'json',
        success:function(data){
             console.log(data['house']['title']);

            $('.house-info').html('<img src="/static/images/'+ data.house.image + '">' +
             '<div class="house-text">' +
                '<h3>'+ data.house.title  + '</h3>'+
                '<p>￥<span>' + data.house.price + '</span>/晚</p></div>'
            )

            $('.submit-btn').on('click', function(e){
                e.preventDefault();
                id = data.house.id;
                var startDate = $("#start-date").val();
                var endDate = $("#end-date").val();
                create_order(id, startDate, endDate)
            })
        }
    });
})

function create_order(id, sd, ed ){

    $.ajax({
        url:'/order/create_order/',
        type:'POST',
        dataType:'json',
        data:{
            'id':id,
            'sd':sd,
            'ed':ed,
        },
        success:function(data){
            if (data.code == 200){
                location.href = '/order/my_order/'
            }

        }
    })
}

