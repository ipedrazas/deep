var DEPDEPHOST = "http://deep-api-svc:5000"

var app = angular.module('dsp', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/detail', {
        templateUrl: 'detail.html',
        controller: 'MainCtrl'
      })
      .when('/', {
        templateUrl: 'main.html',
        controller: 'MainCtrl'
      })
      ;

    $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        });
}]);
