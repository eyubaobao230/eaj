function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
   $('#form-avatar').submit(function(e){
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/user/up_avatar/',
            dataType: 'json',
            type: 'PATCH',
            success: function(data){
                if(data.code == '200'){
                    $('#user-avatar').attr('src', '/static/media/' + data.avatar)
                }
            },
        })
   })


    $('#form-name').submit(function(e){
        e.preventDefault();
        var username = $('#user-name').val()
        $.ajax({
            url: '/user/up_username/',
            data: {'username': username},
            dataType: 'json',
            type: 'PATCH',
            success: function(data){
                if(data.code == '200'){
                    alert('成功')
                }else if(data.code == '2001'){
                    $('.error-msg').html(data.msg)
                    $('.error-msg').show()
                }
            },
            error: function(data){
                alert('failed')
            },
        })
    })
})
