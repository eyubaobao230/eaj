function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){

    $(".book-house").show();

    var url = location.search;
    var id = url.split('=')[1];

    $.ajax({
        url:'/house/detail/' + id + '/',
        type:'GET',
        dataType:'json',
        success:function(data){
             console.log(data['house'])
            $.each(data['images'], function(index, image){

                $('.swiper-wrapp').html(
                    '<li class="swiper-slide"><img src="/static/images/' + image + '"></li>'
                )
            });
            $('#price').text(data.house.price);
            $('.landlord-pic').html(
                    '<img src="/static/images/'+  data['house']['user_avatar'] +'">'
            );
            $('#username').html(data['house']['user_name']);

            $('.house-info-list').html(data['house']['address']);
            $('#room-count').html('出租'+ data['house']['room_count'] +'间');
            $('#acreage').html('房屋面积:'+ data['house']['acreage']+'平米');
            $('#unit').html('房屋户型:'+data['house']['unit'] );
            $('#capacity').html('宜住:'+data['house']['capacity']+'人' );
            $('#beds').html(data['house']['beds'] );




        }
    })


       var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    })

})

$('.book-house').on('click', function(e){
    e.preventDefault();
    var url = location.search;
    var id = url.split('=')[1];
    location.href = '/house/booking/?id=' + id;
})