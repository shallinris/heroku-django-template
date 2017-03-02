/**
 * Created by itc_user1 on 2/15/2017.
 */
var billboard = {};

$(document).ready(function() {
    $("#hide_on_page_load").hide();
});

$("#add-btn").one("click", function(){
    $(".initial_no_message").hide();
});

$("#add-btn").click(function(){
    $(this).parent().hide();
});

$("#add-btn").click(function(){
    $(".hide_on_page_load").show();
});

