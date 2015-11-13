function makeid()
{
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 5; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}



app.controller('MainCtrl', function($scope, $location, api) {



    api.getDependencies().success(function(data){
        console.log(data._items);
        $scope.dependencies = data;
    });


    api.getDeploys().success(function(data){
        console.log(data._items);
        $scope.deploys = data._items;
    });

});
