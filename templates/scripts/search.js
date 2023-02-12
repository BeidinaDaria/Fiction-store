function searchInfo(){
    let info=document.getElementById("search").value;
    let acc=JSON.stringify(info);
    let request;
    if(window.XMLHttpRequest){
        request = new XMLHttpRequest();
    }
    else{
        request = new ActiveXObject("Microsoft.XMLHTTP");
    };
    request.open("POST", "server.php");
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    request.onreadystatechange = function(){
    if(request.readyState === 4 && request.status == 200){
        let product = request.response;
        localStorage.setItem("product",product);
        }
    }
    request.send(acc);
}

searchSubmit.addEventListener('click',searchInfo());