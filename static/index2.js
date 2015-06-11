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
var isLogin = false;

var ptwebqq ;
var username='2081374195'


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

    $('#bt_get_friends').click(function(){
        get_friends()
    });

    $('#img_smscode').click(function(){
        get_captcha()
    });

    $('#bt_poll2').click(function(){
        poll2()
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

var vcode ;
var salt;

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

                        vcode = json.vcode;
                        salt = json.salt;
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

    salt = get_salt_from_js(salt)

    var result = $.Encryption.getEncryption('gguuss',salt,vcode)

    //转化为json形式
    var data = JSON.stringify({'vcode':get_vcode(),'encrypt_pwd':result});

    var success_callback = function(json){

        console.log('success_callback')
        console.log(json)

        if(json.resp_code == 0){

            //$("#bt_get_friends").css("display","block");
            isLogin = true;
            ptwebqq = json.ptwebqq
            alert(json.resp_msg)
        } else {
            alert('failer')
        }
    }
    req_post('login',data,success_callback)
}

/**
 * TODO : 用户名先写死
 */
function get_friends(){
    if(!isLogin){
        alert('please first login !')
        return;
    }

    var success_callback = function(json){
        console.log("get_friends()  success_callback")
        console.log(json)

        alert('ok')
    }

    var hash = u(username,ptwebqq)
    var data = JSON.stringify({'hash':hash});

    req_post('get_user_friends2',data,success_callback)
}


/**
 * 轮询获取消息
 */
function poll2(){

    if(!isLogin){
        alert('please first login !')
        return;
    }

    var success_callback = function(json){
        console.log(json)
    }
    var data = JSON.stringify({'req':''});
    req_post('poll2',data,success_callback)
}

function test_get(){
    var success_callback = function(json){
        console.log(json)
    }

    $.ajax({
            url: 'test',
            type: 'get',
            data:'vvv=ddd',
            success: success_callback,
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}


function test_get_2(){
    var success_callback = function(json){
        console.log(json)
    }

    $.ajax({
            url: 'test',
            type: 'get',
            data:'vvv=444',
            success: success_callback,
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}


function test_post(){
    var success_callback = function(json){
        console.log(json)
        //alert(json)
    }

    var data = JSON.stringify({'vcode':'v2ex'});

    $.ajax({
            url: 'test',
            type: 'post',
            data:data,
            success: success_callback,
            complete: function( xhr, status ) {
                console.log('complete');
            }
    });
}

