function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.ajax({
        url: '/user/get_user/',
        dataType: 'json',
        type: 'GET',
        success:function(data){
            if(data.code == '200'){
//
                if(data.username){
                    $('#user-name').html(data.username)
                }else{
                    $('#user-name').html(data.phone)
                }
                $('#user-mobile').html(data.phone)
                $('#user-avatar').attr('src', '/static/media/'+ data.avat)
            }
        },
        error:function(data){
                    alert('failed')
                }
    })

})

