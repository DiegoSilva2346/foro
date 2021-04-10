$(document).ready(function(){           
    $("#responder").click( function(){              
        $('#respuesta').css("display","block")
        
    })  
    $("#cancelar").click(function(){        
        $("#respuesta").css("display","none");
    })
})