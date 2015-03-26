//controller and route
var book = angular.module("Book",['ngRoute']);
book.config(['$routeProvider',function($routeProvider){
    $routeProvider.when('/',{
        controller:'Home',
        templateUrl:'template/home.html'
    }).when('/contact',{
        controller:'Contact',
        templateUrl:'template/contact.html'
    }).when('/details',{
        controller:'Details',
        templateUrl:'template/details.html'
    }).otherwise({
        redirectTo : '/'
    });
    
}]);
book.factory('DataServ',function(){
   var  data ;
   return {
       getData : function(){
           return data ;
       },
       setData : function (val){
           data = val;
       },
       findData:function(){
           
       }
   };
    
});
book.directive('myTags',function(){
    return {
        templateUrl:'info.html',
        replace:true
    }
});
book.directive('myTags2',function(){
    return function(scope,element,attrs){
       element.html("<span>"+attrs.myTags2+"</span>"); 
    }
});
// second lesson
book.controller('Home',function($scope){
    $scope.hello = "Hello";
    $scope.vals = [1,2,3,4];
    $scope.title = {'head':"Welcome Angular"};
    $scope.showBox = function(flag){
        if(flag == 1) {
            $scope.flag=true;
            return true;
        }
        else 
        {
            $scope.flag=false;
            return false;
        }
    }
    $scope.css ='border:solid 1px black;';
    
});

book.controller('Details',['$scope','DataServ',function($scope,DataServ){
    
     $scope.$on('doSomething',function(event){
       
        var data = DataServ.getData();
        $scope.data = data.first_name;
    });
    $scope.title="Details";
    $scope.data = "Not data" ;
   
}]);

book.controller('Contact',["$scope","$http","$rootScope",'DataServ',function($scope,$http,$rootScope,DataServ){
    $scope.title = "Hello";
    
    $http.get('users.json').success(function(data){
    
    });
    
  DataServ.setData({firt_name:'None'}) ;
     $scope.name =DataServ.getData();;
    
    $scope.GetUser =function(){
         $rootScope.$broadcast('doSomething');
         
     }  ; 
}]);


