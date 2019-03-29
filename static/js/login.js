$(function(){
    var name_error=false;
    var pwd_error=false;
    $('.user_name').blur(function() {
		userName();
    });
    $('.pwd').blur(function(){
        pwd();
    })
    // verify()
});

function userName(){  //用户验证
    var name_val =  $('.user_name').val();
    if(name_val.length===0){
        $('.user_name').next().html('请填写用户名').show();
        name_error = false;
    }else{
        $('.user_name').next().hide();
        name_error = true;
    }
}

function pwd(){  //密码验证
    var pwd_val =  $('.pwd').val();
    if(pwd_val.length===0){
        $('.pwd').next().html('请填写密码').show();
        pwd_error = false;
    }else{
        $('.pwd').next().hide();
        pwd_error = true;
    }
}


$('form').submit(function(e){
    userName();
    pwd();
    if(name_error&&pwd_error){
        return true;
    }else{
        return false;
    }
})