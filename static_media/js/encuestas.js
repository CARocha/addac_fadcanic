(function ($) {
	$.after_inline = function () {
        var functions = {};
        var register = function (fn_name, fn_callback) {
            functions[fn_name] = fn_callback;
        };

        var run = function (inline_prefix, row) {
            for (var fn_name in functions) {
                functions[fn_name](inline_prefix, row);
            }
        };

        return {
            register: register,
            run: run
        };
    }();
  $(function () {
  	
      $(".select2").select2();
      $('.add-row a').on('click',function(e, nose) {
	    	console.log($(nose));

	    	if (inline_prefix == 'seguridadsaf_set') {
	    		alert("hola putitaaa");
            	practicasIm += 1
            $('#seguridadsaf_set-'+practicasIm+'-tipo_practica').select2();
        };
		});
 
  });
  
}(jQuery));