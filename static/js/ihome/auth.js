function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}
$(document).ready(function() {
    $('#form-auth').submit(function(e){
        e.preventDefault()
        $('#real-name').focus(function(){
            $('.error-msg').hide()
        })
        $('#id-card').focus(function(){
            $('.error-msg').hide()
        })
        var real_name = $('#real-name').val()
        var id_card = $('#id-card').val()
        $.ajax({
            url: '/user/my_auth/',
            data: {'real_name': real_name, 'id_card': id_card},
            dataType: 'json',
            Type: 'post',
            success: function(data){
                alert('success')
                if(data.code == '200'){
                    $('.btn-success').hide()
                    $('.form-control').css('disabled', 'disabled')
                }
            },
            error: function(data){
                alert('failed')
            },
        })

    })

})

