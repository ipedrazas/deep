app.factory("api", function($q, $http) {

  var getDeploys = function(){
    return $http.get( DEPDEPHOST + '/deploys')
  };

    var getDependencies = function(){
    return $http.get( DEPDEPHOST + '/dependencies')
  };


  return {
    getDeploys: getDeploys,
    getDependencies: getDependencies,

  };
});
