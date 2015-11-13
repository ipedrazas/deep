var DEPDEPHOST = "http://deep-api.ipedrazas.k8s.co.uk:5000"

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

app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    }
]);
