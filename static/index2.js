/**
 * Created by chenwei on 15-6-1.
 */

/**
 * 是否需要验证码
 * @type {boolean}
 */
var isNeedVerifyCode = false;
var TYPE_GET='get'
var TYPE_POST='post'
var DATATYPE_JSON='json'

var ischeck = false;


$(document).ready(function(){
    $('#bt_check').click(function(){
        check_vc();
    });

    $('#bt_smscode').click(function(){
        get_captcha()
    });

    $('#bt_login').click(function(){
        login()
    });
})

/**
 * get 请求服务器
 * @param url
 * @param data
 * @param success_callback
 */
function req_get(url,data,success_callback){
    req(url,TYPE_GET,data,DATATYPE_JSON,success_callback,null);
}

/**
 * post 请求服务器
 * @param url
 * @param data
 * @param success_callback
 */
function req_post(url,data,success_callback){
    req(url,TYPE_POST,data,DATATYPE_JSON,success_callback,null);
}

/**
 * 请求服务器　（提取共有方法）
 * @param url
 * @param type
 * @param data
 * @param dataType
 * @param success_callback
 * @param error_calllback
 */
function req(url,type,data,dataType,success_callback,error_calllback){

    if(error_calllback == null){
        error_calllback = function(error) {
                console.log('error',error.responseText);
        }
    }

    $.ajax({
            url: url,
            type: type,
            dataType : dataType,
            data:data,
            success: success_callback,
            error:error_calllback,
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}

/**
 * 显示验证码
 */
function show_sms_code(){
    console.log('show_sms_code()')
}

/**
 * 获取控件上的验证码的值
 * @returns {*|jQuery}
 */
function get_vcode(){
    var vcode = $("#vcode").val()
    if(!isNeedVerifyCode){
        vcode='';
    }
    return vcode;
}


/**
 * 账号检查 (与后台交互)
 */
function check_vc(){

    var success_callback = function( json ) {
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

                    ischeck = true;

                } else {
                    alert(json);
                }
            }

    req_get('check','',success_callback);
}

/**
 * 获取验证码图片　（与后台交互）
 */
function get_captcha(){

    var success_callback = function(json){
        console.log('get_captcha()')
        if(json.resp_code == 0){
            //与前段做交互
            //alert();
            //显示验证码
            var tmp = (new Date().getTime())
            $("#img_smscode").attr("src","/static/img/pic.jpg"+"?"+tmp);
        } else {
            alert('获取验证码 error :'+json.resp_msg)
        }
    }
    req_get('getimage','',success_callback);
}

/**
 * TODO: 接口整合，　将 "login/vcode" , "login/encrypt_pwd","login/first" 统一成一个接口
 * {
 *      'vcode':'', 'encrypt_pwd':''
 * }
 * 登录　(与后台交互)
 */
function login(){


    if(!ischeck){
        alert('please first check !')
        return;
    }

    //转化为json形式
    var data = JSON.stringify({'vcode':get_vcode(),'encrypt_pwd':''});

    var success_callback = function(json){
        console.log(json)

        if(json.resp_code == 0){
            alert('ok')
        } else {
            alert('failer')
        }
    }

    req_post('login',data,success_callback)
}


function test_post(){

    salt = '\x00\x00\x00\x00\x7c\x0f\x3f\xf3'
    var arr = new Array(salt.length)
    var s=''
    for(var i=0;i<salt.length;i++){
            //console.log(json.charAt(i))
            arr[i] = salt.charCodeAt(i)
            //arr.join(salt.charCodeAt(i))
        s+=String.fromCharCode(salt.charCodeAt(i))
        console.log(s)
    }

    console.log('result='+s)

    console.log(arr)
    console.log('game over')
    return;

    var success_callback = function(json){
        console.log(json)

        json = String(json)
        //req_get('test',json,null)

        console.log(json.length)
        for(var i=0;i<json.length;i++){
            //console.log(json.charAt(i))
            console.log(json.charCodeAt(i))
        }
    }

    var js_salt = '\x00\x00\x00\x00\x7c\x0f\x3f\xf3'

    console.log(js_salt);
    $.ajax({
            url: 'test',
            type: 'post',
            data:js_salt,
            //data:'r:{"ptwebqq"="1111","clientid"=53999199,"psessionid"="","status"="online"}',
            success: success_callback,
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}

