$(function(){

    $('.user_name').blur(function() {
		userName();
    });
    $('.pwd').blur(function(){
        pwd();
    })
    $('.rpwd').blur(function(){
        repeatPwd();
    })
    $('.email').blur(function(){
        email();
    })
    var error_name = false;
    var error_password = false;
    var error_repeat_password = false;
    var error_email = false;
});

function userName(){ //用户名验证
    var name_val = $('.user_name').val()
    if(name_val.length<3||name_val.length>15){
        $(".user_name").next().html('请输入3-20个字符的用户名').show();
    }else{
        $.get('/user/registerisname?uname='+name_val,function(data){
            if(data.count > 0){
                $(".user_name").next().html('用户名已被占用').show();
                error_name = false;
            }else{
                $(".user_name").next().hide();
                error_name = true;
            }
        })
    }
}

function pwd(){  //密码验证
    var pwd_val =  $('.pwd').val();
    var pwd_num = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/;
    if(pwd_val.length<8 || pwd_val.length>20||pwd_num.test(pwd_val) === false){
        $('.pwd').next().html('请输入至少8位数字和字母混合密码').show();
        error_password = false;
    }else{
        $('.pwd').next().hide();
        error_password = true;
    }
}

function repeatPwd(){
    var pwd_val =  $('.pwd').val();
    var repeat_pwd_val =  $('.rpwd').val();
    if(pwd_val !== repeat_pwd_val){
        $('.rpwd').next().html('两次输入的密码不一致').show();
        error_repeat_password = false;
    }else{
        $('.rpwd').next().hide();
        error_repeat_password = true;
    }
}

function email(){//邮箱验证
    var email = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
    var email_val =  $('.email').val();
    if(email.test(email_val) === false){
		$('.email').next().html('你输入的邮箱格式不正确').show();
        error_email = false;
    }else{
        $('.email').next().hide();
        error_email = true;
    }
}


$('form').submit(function(e){//如果上面验证不通过 不能提交
    userName();
    pwd();
    repeatPwd();
    email();
    if(error_nam&& error_password&& error_repeat_password&& error_email)
    {
        return true;
    }else{
        return false;
    }
    
})
