function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
//    房屋详细信息
   $('#form-house-info').submit(function(e){
        e.preventDefault()
        $(this).ajaxSubmit({
            url: '/house/x_house/',
            dataType: 'json',
            type: 'POST',
            success: function(data){
                if(data.code == '200'){
                    $('#form-house-info').hide()
                    $('#form-house-image').show()
                }
            },
            error: function(data){
                alert('failed')
            },
        })
    })
//    上传图片
   $('#form-house-image').submit(function(e){
        e.preventDefault()
        $(this).ajaxSubmit({
            url: '/house/h_img/',
            dataType: 'json',
            type: 'POST',
            success: function(data){
                if(data.code == '200'){
//                    $('#form-house-info').html(data.housename)
                        location.href = '/house/my_house/'
                }
            },
            error: function(data){
                alert('failed')
            },
        })
   })
})