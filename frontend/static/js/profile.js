let CSRF_TOKEN = window.CSRF_TOKEN;

// ToDo: add error handler
// ToDo: add nice update row function
// ToDo: add update logic

let default_error_handler = function(xhr,errmsg,err) {
    alert('error: ' + errmsg);
}

let send_action = function(order_id, action_name, success_handler, error_handler=default_error_handler) {
    $.ajax({
        url: "api/order/" + order_id + "/" + action_name,
        data: { csrfmiddlewaretoken: CSRF_TOKEN },
        method: "POST",
        success: success_handler,
        error: error_handler,
    });
}

$(document).ready(function() {

    $('.decline-action').click( function() {
        row = $(this).closest("tr");
        let orderID = row.attr("data-orderid");
        send_action(orderID, "cancel",
            function(response) {
                if (response['success']){
                    current_status = row.find('#order_status');
                    current_status.text(response['status_update']);

                } else if (response['error']) {
                    alert(response['error']);
                }
            }
        );
    })

    $('.dispute-action').click( function() {
        row = $(this).closest("tr");
        let orderID = row.attr("data-orderid");
        send_action(orderID, "dispute",
            function(response) {
                if (response['success']){
                    current_status = row.find('#order_status');
                    current_status.text(response['status_update']);

                } else if (response['error']) {
                    alert(response['error']);
                }
            }
        );
    })

    $('.accept-action').click( function() {
        row = $(this).closest("tr");
        let orderID = row.attr("data-orderid");
        send_action(orderID, "accept",
            function(response) {
                if (response['success']){
                    current_status = row.find('#order_status');
                    current_status.text(response['status_update']);

                } else if (response['error']) {
                    alert(response['error']);
                }
            }
        );
    })

    $('.shipping-action').click( function() {
        row = $(this).closest("tr");
        let orderID = row.attr("data-orderid");
        send_action(orderID, "shipping",
            function(response) {
                if (response['success']){
                    current_status = row.find('#order_status');
                    current_status.text(response['status_update']);

                } else if (response['error']) {
                    alert(response['error']);
                }
            }
        );
    })

    $('.delivered-action').click( function() {
        row = $(this).closest("tr");
        let orderID = row.attr("data-orderid");
        send_action(orderID, "delivered",
            function(response) {
                if (response['success']){
                    current_status = row.find('#order_status');
                    current_status.text(response['status_update']);

                } else if (response['error']) {
                    alert(response['error']);
                }
            }
        );
    })

});
