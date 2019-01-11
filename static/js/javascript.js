  $(document).ready(function() {
      
                var intcookie = Cookies.get('int');
                   if (typeof intcookie === 'undefined') 
                 
                {
                     $('#myModal').modal('show');
                  Cookies.set('int', '1');
                     



                 }
             });







   



