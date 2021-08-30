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
card.mount("#card-element");

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

