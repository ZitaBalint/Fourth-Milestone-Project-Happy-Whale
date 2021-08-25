$(document).on('click', '#add-button', function (e ) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url cart:cart_add %}',
        data: {
            itemid: $('#add_button').val(),
            itemsize: $('#select-size option:selected').val(),
            itemquantity: $('#select-quantity option:selected').val(),
            csrftoken: "{{csrf_token}}",
            action: 'post'
        },
        success: function (cart) {
            document.getElementById(cart-size).innerHTML = json.size
            document.getElementById(cart-quantity).innerHTML = json.quantity
        },
        error: function (xhr, errmsg, err) {}
    });
})