var POST =function(api, data, func) {
     var request =new XMLHttpRequest();
     request.onreadystatechange =function() {
       
         if(request.readyState == 4) {
             try{
                 console.log(request.responseText)
                 var resp = JSON.parse(request.response);
             } catch(e) {
                 var resp ={status: 'error',
                             data: request.responseText};
                 alert(request.responseText);
             }
             func(resp);
         }
     };
     request.open('POST', api);
     request.send(data);
     return request
}

