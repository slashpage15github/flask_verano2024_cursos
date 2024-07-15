$(document).ready(function() {

    $('#login').on('submit', function(e){
      e.preventDefault();
      var js_us=document.getElementById("f_user").value.trim();
      var js_pw=document.getElementById("f_pwd").value.trim();
      var reresponse = grecaptcha.getResponse();
      //alert(js_us+' -  '+js_pw);
      if (js_us.length==0 || js_pw.length==0){
          Swal.fire({
                icon: 'error',
                title: 'Usuario y password',
                text: 'El usuario y password no debe ir vacios'
              }); 
          return  false;
      }
      else if(js_us.length<2 || js_pw.length<2){
          Swal.fire({
                icon: 'error',
                title: 'Usuario y password',
                text: 'El usuario y password deben contener al menos 8 caracteres'
              }); 
          return  false;
  
      }
      else if (reresponse.length == 0){
        Swal.fire({
        type: 'error',
        title: 'Error: Marque la casilla de verificacion de seguridad, no puede ir vacía, verifique.',
        text: '¡Verificar, por favor!'});
        return false;
    }
      else{
          $.ajax({  
              url:'/valida_usuario',  
              method:'POST',  
              data:{js_us:js_us,js_pw:js_pw},
              /*dataType: "json",*/
              success:function(response){
                      //alert(response);
                      //console.log(response);
                      if (response==0){
                          Swal.fire({
                              icon: 'error',
                              title: 'Error de acceso',
                              text: 'El usuario y password no se encuentran registrados'
                            });                            
                      }else{
                          $.ajax({  
                              url:'/sesion_usuario',  
                              method:'POST',  
                              data:{js_us:js_us,js_pw:js_pw},
                              dataType: "json",
                              success:function(response){
                                  //console.log(response);
                                  Swal.fire({
                                      icon: 'success',
                                      title: 'Bienvenido:'+response.id,
                                      text: 'Nombre:'+response.nombre
                                    }).then(function() {
                                      window.location = "profile";
                                      });                                },
                             error : function(request, status, error) {
              
                                     var val = request.responseText;
                                     alert("error"+val);
                             }  
                         });  
                      }
              },
             error : function(request, status, error) {

                     var val = request.responseText;
                     alert("error"+val);
             }  
         });  
      }
    });



});