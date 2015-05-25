function sayHi(){
    console.log('sayHi0-----()')
    //console.log('iii= '+iii)

    if(window.localStorage){
        console.log('This browser supports localStorage');
    }else{
        console.log('This browser does NOT support localStorage');
    }
}

sayHi();
phantom.exit();
