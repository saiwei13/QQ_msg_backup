/**
 * Created by chenwei on 15-6-1.
 */

/**
 * 是否需要验证码
 * @type {boolean}
 */
var isNeedVerifyCode = false;

/**
 * 显示验证码
 */
function show_sms_code(){
    console.log('show_sms_code()')
    //document.getElementsByClassName('valcode').style.display="block";
    //document.getElementsByClassName('valcode').style.display="none";

    //$(".valcode").css("display","none");
    //$(".valcode").css("display","block");
}



function check_vc(){
    //$.ajax('check',true)
    $.ajax({
            url: 'check',
            type: 'get',
            dataType : 'json',
            success: function( json ) {

                console.log('success');
                console.log(json);
                console.log(json.resp_msg);

                if(json.resp_code == 0){
                    if(json.resp_data){
                        $(".valcode").css("display","block");
                        $("#img_smscode").attr("src","/static/img/pic.jpg");
                        isNeedVerifyCode = true;
                    } else {
                        $('#tip_smscode').html("不需要验证码");
                        isNeedVerifyCode= false;
                    }
                } else {
                    alert(json);
                }
            },
            error: function(error) {
                console.log('error',error.responseText);
            },
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}


/**
 * 获取验证码
 * @returns {*|jQuery}
 */
function get_verifycode(){
    var verifycode = $("#verifycode").val()
    if(!isNeedVerifyCode){
        verifycode='';
    }
    verifycode = JSON.stringify({'verifycode':verifycode});
    return verifycode;
}

function login(){
    var verifycode = get_verifycode();
    //转化为json形式
    verifycode = JSON.stringify({'verifycode':verifycode});

    $.ajax({
            url: 'login',
            type: 'post',
            dataType : 'json',
            data:verifycode,
            success: function( json ) {
                console.log('success');
                console.log(json);
                console.log(json.resp_msg);
            },
            error: function(error) {
                console.log('error',error.responseText);
            },
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}