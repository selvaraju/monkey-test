// $(function() {
//     $('button').click(function() {
//         var user = $('#txtUsername').val();
//         var pass = $('#txtPassword').val();
//         $.ajax({
//             url: '/signUpUser',
//             data: $('form').serialize(),
//             type: 'POST',
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });

<script type="text/javascript">
    $(document).ready(function(){
       $("#cloud").click(function(){
        $('#result').load('cloud.html');
         //alert("Thanks for visiting!");
       }); 

       $("#hypervisor").click(function(){
        $('#result').load('hypervisor.html');
         //alert("Thanks for visiting!");
       });
     });
</script>