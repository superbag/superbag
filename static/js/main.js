"use strict";


function render_map () {
    if (typeof L != 'undefined') {
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        var map = L.map('map').setView([49, 32], 6);
    } else {
    	var map = L.map('map').setView([48.5, 31.5], 6);
    }

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	    maxZoom: 16,
	    id: 'superbag.pd90p72b',
	    accessToken: 'pk.eyJ1Ijoic3VwZXJiYWciLCJhIjoiY2lscW8xNzR4MDA1N3ZybHl2bmhpNGl1NyJ9.xRJ9IzWRQJ6QJCX1hfU3GQ'
	}).addTo(map);
	return map;
    }
};

function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}


function getCookie(name) {

    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

jQuery(document).ready(function ($) {

    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         } 
    });

	$(".btn-send").click(function(){
		var email = $(".email").val();
		var name = $(".name").val();
		var message = $(".message").val();
        $(".alert").remove();

        if (IsEmail(email) && message.length > 1) {
            console.log('here')

    		$.post('/contact/', {
    			'email': email,
    			'name': name,
    			'message': message,
                // csrfmiddlewaretoken: '{{ csrf_token }}'
            },
                function() {
                    $(".email").val('');
                    $(".name").val('');
                    $(".message").val('');
                    $(".contact-form").empty();
                    $(".contact-form").append('<div class="alert alert-success" role="alert">Дякуємо за ваше звернення</div>');
                }
            );
        } else if (!(IsEmail(email))) {
            return alert("Введіть вашу єлектронну адресу");   
        } else if (message.length < 1) {
            return alert("Введіть ваше повідомлення");
        }
	});
	var map = render_map();
    if (typeof L != 'undefined') {
        $.get('points', function(jdata){
            jdata.forEach(function(point){
                var salepoint = L.marker([point.fields.lon, point.fields.lat]).addTo(map);
                salepoint.bindPopup("<b>" + point.fields.name + "</b>"); 
            });
        });
    }

    $("#req-from-but").click(function(){
        $.fn.datepicker.defaults.format = "yyyy-mm-dd";
        $("#id_event_date").datepicker();
        $("#ReqModal input").each(function(){
            $(this).addClass('form-control');
        });
        $("#ReqModal").modal('show');
    });

    $("#req-save").unbind().click(save_request);
});

function show_alert(element_id) {
    var alert = document.getElementById(element_id);
    // alert.innerHTML = message;
    console.log(alert)
    alert.style.display = 'block';
    setTimeout(function() {
        alert.style.display = 'none';}, 10000);
}


function save_request() {
    var author = $("#id_author").val();
    var phone = $("#id_phone").val();
    var email = $("#id_email").val();
    var airport_arrival = $("#id_airport_arrival").val();
    var airport_destination = $("#id_airport_destination").val();
    var ticket_num = $("#id_ticket_num").val();
    var event_date = $("#id_event_date").val();
    var description = $("#id_description").val();
    var info = $("#id_info").val();

    $("#email-label").removeClass('error');
    $("#ReqModal input").each(function(){
        $(this).removeClass('error');
        var parrent = $(this).parent();
        var prev = $(parrent).prev();
        $(prev).removeClass('error');
        if ($(this).val().length < 3) {
            $(this).addClass('error');

            $(prev).addClass('error');
        } 
    });

    if ($(".error").length > 0) {

    } else if ((!(IsEmail(email)))) {
        $("#email-label").addClass('error');
    } else {
        $.post('/create_request/', {
            'author': author,
            'email': email,
            'phone': phone,
            'airport_arrival': airport_arrival,
            'airport_destination': airport_destination,
            'ticket_num': ticket_num,
            'event_date': event_date,
            'description': description,
            'info': info,
            }, function(jdata) {
                console.log(jdata);
                $("#ReqModal").modal('hide');
                show_alert('alert-form');
            }
        );
    }
}