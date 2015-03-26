$(document).ready(function(){

$( 'textarea' ).ckeditor();

$('#my-affix').affix({
    offset: {
      top: 100
    , bottom: function () {
        return (this.bottom = $('.footer').outerHeight(true));
      }
    }
 });

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

$('#myTab a:first').tab('show');

 $(".bfoto").fancybox();
 $(".win").fancybox({
		maxWidth	: 800,
		maxHeight	: 600,
		fitToView	: false,
		width		: '70%',
		height		: '70%',
		autoSize	: false,
		closeClick	: false,
		openEffect	: 'none',
		closeEffect	: 'none'
	});
  
  $(".tagm").click(function(){
  	var text = $(this).text();
  	var el ="<span class=' pbadge  glyphicon glyphicon-minus'><em class='badge'>"+text+"</em></span>";
  	
	$(".filter").append(el);
	$(this).unbind();
	return false;
});

$(".filter").click(function(event){
	$(this).find('.pbadge').remove();
	
	});
	var site="https://www.googleapis.com/youtube/v3/search";
	var search ="?q=php";
	var fields="&fields=items(snippet)"
	var url =site+search+"&part=snippet"+fields;
	$.getJSON(url,{
		format: "json",
		type : 'playlist',
		key : 'AIzaSyCD3LOuGY8YL_XvOpe5rGLohySWTjdRa-M',
		
	},function(data){
		
		$.each(data.items,function(k,v){
			$.each(v,function(key,value){
				console.log(value);
				// $('.video').append("<span><p>"+value.channelId+"</p></span>");
			});
			 
			 
		});
		
		
	 
	});
	
});


	
