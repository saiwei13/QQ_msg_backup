console.log('project : ｑｑ消息備份　。　Hello, world   from hello.js !');

function show_time(){
    console.log('show_time')
    //document.getElementById('showbox').innerHTML = new Date();
    //setTimeout('show_time()',1000);
    window.status="Page is loaded"
}

function outer() {
    var x = 1;
    console.log('outer')
    inner()
    function inner() {
        console.log("Hi");
    }
}

var isclick = false;

function sayhi(){
    isclick = true;
    alert("OK");

    isClick();
}

function isClick(){
    console.log("isclick()");
    //document.getElementById('test_alert').textContent = '有点击'

    document.getElementById('test_alert').value = "有点击"

    //if(isclick){
    //    document.getElementById('test_alert').innerHTML = "有点击"
    //} else {　
    //    document.getElementById('test_alert').innerHTML　= "没点击"
    //}

}

function get_result(){
    return 'chenwei'
}

/*$.Encryption = function() {

    function md5(){
        console.log('md5');
    }

    function getEncryption(password){
        console.log('getEncryption : '+password);

        return 'what'
    }

    function getRSAEncryption(){
        console.log('getRSAEncryption');
    }

    return {
        getEncryption: getEncryption,
        getRSAEncryption: getRSAEncryption,
        md5: md5
    }
}();

function sayHi(){
    console.log('sayHi()')
    var result  = $.Encryption.getEncryption('6377508')

    console.log('result = '+result)
}*/


//(function() {
//    alert("OK");
//})();

function test_add(){
    console.log('test_add()')
    document.getElementById('myform').submit();
    //console.log('test_file()')
}

function test_ajax(){
    console.log('test_ajax()')
    //var u = document.getElementById('u')
    //// $("#mytable").val()
    //var p = document.getElementById('p').textContent
    var u = $("#username").val()
    var p = $("#password").val()
    var data={ "u" : u,'p':p };
    $.ajax({url: "/set_encrypt_pwd", type: "POST", dataType: "text",data: data});
}


var xmlhttp;

function loadXMLDoc(url,cfunc){
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=cfunc;
    xmlhttp.open('GET',url,true);
    xmlhttp.send();
}

function test_ajax_get(){
    var xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function(){
        if(xmlhttp.readyState==4 && xmlhttp.status == 200){
            document.getElementById('mydiv').innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET",'login',true);
    xmlhttp.send();

}

function test_ajax_post(){
    var xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST",'login',true);
    xmlhttp.send()
}

function test_ajax_callback(){
    loadXMLDoc('login', function () {
        if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
            document.getElementById('mydiv').innerHTML = "callback [[["+xmlhttp.responseText;
        }
    })
}