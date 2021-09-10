// copied from offical Stripe documentation 
var stripe = Stripe('pk_test_51JUDztBeU0R6ZOy2fetXqavkBpRlGSlJuxmnKORXEpFMbxF46utDA82pXXegqVIMbNNboMyYOSP1ktpzIV23kRh800jZl34vB5')

var eleme = document.getElementById('submit');
clientsecret = eleme.getAttribute('data-secret');

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
        $('#card-errors').class('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info')
    }
})

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

var firstName = document.getElementById("firstName").value;
var lastName = document.getElementById("lastName").value;
var addressLine = document.getElementById("addressLine").value; 
var addressLine2 = document.getElementById("addressLine2").value;
var postCode = document.getElementById("postCode").value;

$.ajax({
    type: "POST",
    url: 'ordered/',
    data: {
      order_key: clientsecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
        console.log(json.success)

            stripe.confirmCardPayment(clientsecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        address: {
                            line1: addressLine,
                            line2: addressLine2,
                            postal_code: postCode
                        },
                        name: firstName + " " + lastName

                    },
            }
            }).then(function (result) {
                if (result.error) {
                    console.log('patment error')
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
        
