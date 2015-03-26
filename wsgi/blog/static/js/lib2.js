var blogcms = angular.module('Cms',['ng.django.forms','ui.bootstrap']);

//,'ui.bootstrap' 'ngRoute'
// blogcms.config(['$routeProvider',function($routeProvider){
    // $routeProvider.when('/index',{
        // controller:'Home',
        // templateUrl:'blog/index.html'
    // }).when('/view',{
        // controller:'View',
        // templateUrl:'blog/view.html'
    // }).when('/gallery',{
        // controller:'Gallery',
        // templateUrl:'template/gallery.html'
    // }).when('/video',{
        // controller:'Video',
        // templateUrl:'template/video.html'
    // }).otherwise({
        // redirectTo : '/'
    // });
//     
// }]);
blogcms.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
// blogcms.config(function($interpolateProvider) {
    // $interpolateProvider.startSymbol('{$');
    // $interpolateProvider.endSymbol('$}');
// });

blogcms.controller('Home',function($scope){
	$scope.say="Angular work";
	
	
});

blogcms.controller('Menu',['$scope','$http',function($scope,$http){
	
	$http.get('/blog/menu').success(function(data){
		$scope.links = data;
	});
	
}]);
	

$('.bfoto').fancybox();

$.getJSON('/blog/menu',function(data){
	 var t="";
	 var items = [];
  $.each( data, function( key, val ) {
    
    if(val.fields.title.toString() == "Root"){
    	t="";
    }
    else{
    	t =val.fields.title;
    	$(".m-menu").append('<li ><a href="/index?category='+val.fields.item_url+'">'+t+'</a></li>');
}
  });
 });



 

	
