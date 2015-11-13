app.factory("api", function($q, $http) {

  var getDeploys = function(){
    return $http.get( DEPDEPHOST + '/deploys')
  };

    var getDependencies = function(){
    return $http.get( DEPDEPHOST + '/dependencies')
  };


  var getWebhooks = function(){
    return $http.get( DEPDEPHOST + '/webhooks')
  };

  return {
    getDeploys: getDeploys,
    getDependencies: getDependencies,
    getWebhooks: getWebhooks,
  };
});
