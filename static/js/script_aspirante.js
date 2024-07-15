const pattern_rfc=/^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
const pattern_tel=/^[0-9]{10}?$/;
const emailPattern =/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

let valida_aspirante = () =>{
    let js_rfc=getTextInputById("f_rfc");
    let js_nom=getTextInputById("f_nombre");
	  let js_pat=getTextInputById("f_paterno");
	  let js_mat=getTextInputById("f_materno");
    let js_tel=getTextInputById("f_telefono");
	  let js_emp=getTextInputById("f_empresa");
	  let js_ema=getTextInputById("f_email");
	  let js_cur=getTextInputById("f_curso");

    //console.log(js_rfc,js_nom,js_pat, js_mat, js_tel, js_emp, js_ema, js_cur);

    if (js_rfc.length==0){
      mensaje('error','Error en RFC','El dato RFC no puede is vacío!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    else if (!pattern_rfc.test(js_rfc)){
      mensaje('error','Error en RFC','El dato RFC no cumple el formato! ejemplo:PETD741512R45','<a href="https://www.sat.gob.mx/home">Necesita ayuda?</a>');
      return false;
    }
    if (js_nom.length==0){
      mensaje('error','Error en nombre','El dato nombre no puede is vacío!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    else if (js_nom.length<3){
      mensaje('error','Error en Nombre','El dato Nombre no cumple el formato, pocos caracteres!','<a href="">Necesita ayuda?</a>');
      return false;
    }    
    if (js_pat.length==0){
      mensaje('error','Error en paterno','El dato paterno no puede is vacío!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    else if (js_pat.length<3){
      mensaje('error','Error en Paterno','El dato Paterno no cumple el formato, pocos caracteres!','<a href="">Necesita ayuda?</a>');
      return false;
    } 
    if (js_mat.length==0){
      mensaje('error','Error en materno','El dato materno no puede is vacío! En caso de no contar con Apellido Materno rellene con una X','<a href="">Necesita ayuda?</a>');
      return false;
    }
    if (js_tel.length==0){
      mensaje('error','Error en teléfono','El dato teléfono no puede is vacío!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    else if (!pattern_tel.test(js_tel)){
      mensaje('error','Error en Telefono','Telefono solo acepta números! ejemplo:8442722698',null);
      return false;
    }
    if (js_emp==0){
      mensaje('error','Error en empresa','Seleccione una empresa!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    if (js_ema.length==0){
      mensaje('error','Error en email','El dato email no puede is vacío!','<a href="">Necesita ayuda?</a>');
      return false;
    }
    else if(!emailPattern.test(js_ema)){
      mensaje('error','Error en email','email no cumple el formato, ejemplo:algo@dominio.edu.mx',null);
      return false;    
    }
    if (js_cur==0){
      mensaje('error','Error en curso','Seleccione un curso!','<a href="">Necesita ayuda?</a>');
      return false;
    }

    
}

let getTextInputById = (id) => {
    return document.getElementById(id).value.trim();
  }

  let mensaje = (tipo,titulo,texto,liga) =>{
    Swal.fire({
      icon: tipo,
      title: titulo,
      text: texto,
      footer: liga
    });
  }