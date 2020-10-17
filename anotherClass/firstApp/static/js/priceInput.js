$(document).ready(function () {
  //called when key is pressed in textbox
  $("#minPrice").keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        //display error message
        $("#errmsg").html("숫자를 입력해주세요.").show().fadeOut("slow");
               return false;
    }
   });
   $("#maxPrice").keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        //display error message
        $("#errmsg").html("숫자를 입력해주세요.").show().fadeOut("slow");
               return false;
    }
   });
});