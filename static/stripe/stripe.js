// copied from offical Stripe documentation 
var stripe = Stripe('settings.STRIPE_PUBLIC_KEY')

var eleme = document.getElementById('submit');
clientSecret = eleme.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base: {
        color: '#696969',
        lineHeight : '2.4',
        fontSize: '16px'
    }
};
var card = elements.create("card", {styel: style});
card.mount('#card-element');

// Payments errors base was used from Stripe github and  Youtube tutorial

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').lass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info')
    }
})

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

var firstName = document.getElementById("id_first_name").value;
var lastName = document.getElementById("id_last_name").value;
var emialAddress = document.getElementById("id_email_address").value;
var addressLine = document.getElementById("id_address_line1").value; 
var addressLine2 = document.getElementById("id_address_line2").value;
var townCity= document.getElementById("id_town_or_city").value;
var country= document.getElementById("id_country").value;
var postCode = document.getElementById("id_postcode").value;

$.ajax({
    type: "POST",
    url: 'ordered/',
    data: {
      order_key: clientSecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
        console.log(json.success)

        stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        address: {
                            line1: addressLine,
                            line2: addressLine2,
                            postal_code: postCode,
                            town_city: townCity,
                            country: country
                        },
                        name: firstName + " " + lastName,
                        email: emialAddress
                    },
            }
            }).then(function (result) {
                if (result.error) {
                    console.log('payment error')
                    console.log(result.error.message);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        console.log('payment proccessed')
                        window.location.replace('ordersent/')
                    }
                }
              });
        
            },
            error: function (xhr, errmsg, err) {},
          });
        
        
        
        });
        
