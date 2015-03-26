
App = Ember.Application.create({
    // LOG_TRANSITIONS: true,
//     LOG_TRANSITIONS_INTERNAL: true
});

App.Router.map(function() {
 //   this.resource("dating", function(){
 //
 //  });
 //  this.resource("user", function(){
 //
 // });
   this.route('index', { path: '/' });
//   this.route("edit", { path: "/edit/:id" });
   this.resource("category",{ path: '/categories'});
   this.resource("page",{ path: '/pages' });
   this.resource("comment",{ path: '/comment' });

});

//App.ApplicationAdapter = DS.FixtureAdapter.extend();

App.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
  host: '/api'
});
App.ApplicationSerializer = DS.DjangoRESTSerializer.extend({
    
});

//App.ApplicationAdapter = DS.RESTAdapter.extend({
//    host: '/api',
//   defaultSerializer: 'django'
//});

App.IndexController = Ember.ArrayController.extend({
    //filteredContent
    //arrangedContent
    sortProperties: ["login,about"],
    sortAscending: false,
    
    filter:'',

    actions: {
   sort: function(property) {

       this.set('sortProperties', [property]);
        this.set('sortAscending', true);
       this.set('sortAscending', !this.get('sortAscending'));

      }
   },
//  Onfilter: function() {
//      console.log(this.get("user").get('arrangedContent'))
//      if(this.get('filter') === ''){
//       return this.get('arrangedContent');
//      }
//      else{
//            
//            data =  this.get('arrangedContent').filterBy('login',this.get('filter'));
//            console.log(data);
//            return data;
//      }
//   }.property('filter','sortProperties')

});



App.IndexRoute = Ember.Route.extend({

model: function() {
    // var user =  this.store.findAll('user');
    // var  markers =  this.store.findAll('dating');
    return this.store.find('comment').then(function(data){
        return data;
    });
        
     
    
//      return this.store.find('dating',{
//  limit: 10,
//  offset: 0
//});


   },
//   setupController: function(controller, model) {
//    // You can use model.post to get post, etc
//    // Since the model is a plain object you can just use setProperties
//    controller.setProperties(model);
//  }
});



App.EditRoute = Ember.Route.extend({
  isAgree:false,
  isFlag:false,
   actions: {

    edit :function(){
       this.toggleProperty('isAgree');
    },
     show: function() {
       // alert('work');

      this.controller.set('isAgree',true);
     // this.transitionTo('index');
    }
},
  model: function(params) {
     return this.store.find('news',params.id);
   }
});


