(function() {

  var count = 0;
  var interval = 5000;
  var maxTries = 24;

  // Call our main endpoint via ajax
  // This kicks off the call to eSec
  $.ajax({
    dataType: 'json',
    method: 'POST',
    data: {
      auth_code: $('input[name="auth_code"]').val()
    },
    url: '/confirming-mortagage-deed-call',
    timeout: interval * maxTries, // Make it wait for the full duration
    success: function(data) {
      if(data.error) {
        window.location = data.redirect;
      }
    }
  });

  // Function to check the status of the request periodically
  function check() {

    count++;

    // Call our checking endpoint via ajax
    $.ajax({
      dataType: 'json',
      method: 'GET',
      url: '/confirming-mortagage-deed-check',
      success: function(data) {

        // If it's ready, redirect, otherwise go round again
        if(data.result) {
          window.location = data.redirect;
        }

      }
    });

    if(count < maxTries) {
      setTimeout(check, interval);
    } else {
      window.location = '/service-unavailable/deed-not-confirmed';
    }
  }

  // Every 5 seconds
  setTimeout(check, interval);

})();
