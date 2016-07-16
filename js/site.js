$(document).ready(function() {
  $.ajaxSetup({ cache: true });
  $.getScript('//connect.facebook.net/en_US/sdk.js', function(){
    FB.init({
      appId: '1578722989092964',
      version: 'v2.6',
      xfbml: true
    });
  });
});