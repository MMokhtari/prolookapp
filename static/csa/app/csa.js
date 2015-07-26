angular.module('csaDirectives',[]);
angular.module('HandonoffControllers', []);
angular.module('HomeControllers', []);
angular.module('WorkplaceControllers', []);
angular.module('CompanyManagerControllers', []);
angular.module('EmployeesManagerControllers', []);
angular.module('TaskManagerControllers', []);

var csa = angular.module('csa', ['ngRoute','ngResource','HandonoffControllers','HomeControllers','WorkplaceControllers','CompanyManagerControllers','EmployeesManagerControllers','TaskManagerControllers','xeditable','ngTagsInput','csaDirectives']);
csa.$inject = ['$routeProvider', '$httpProvider', '$resourceProvider', '$locationProvider'];
/*csa.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            templateUrl: '/static/csa/app/components/handonoff/partials/register.html'
        }).when('/signin', {
            controller: 'SigninController',
            templateUrl: '/static/csa/app/components/handonoff/partials/signin.html'
        }).when('/signout', {
            controller: 'SignoutController',
            templateUrl: '/static/csa/app/components/handonoff/partials/signout.html'
        }).otherwise({
            redirectTo: '/'
        });
    }
]);*/
/*
csa.config(function ($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'views/main.html',
    controllerAs: '',
    controller: ''
  })
  .otherwise({
    redirectTo: '/'
  });
});*/
csa.run(function(editableOptions,editableThemes) {
  editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
  editableOptions.buttons = 'no';
  editableThemes.bs3.inputClass = 'input-md';
  editableThemes.bs3.buttonsClass = 'btn-sm'; 
});
csa.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
csa.factory('MyInterceptor', ['$q',
    function($q) {
        return {
            // optional method
            'request': function(request) {
                // do something on success
                if (request.method == 'GET') {
                    console.log('The intercepter : GET is up');
                } else {
                    console.log('The intercepter : POST is up');
                    $('#loader').show();
                }
                return request;
            },
            // optional method
            'requestError': function(rejection) {
                // do something on error
                /*if (canRecover(rejection)) {
                    return responseOrNewPromise
                }
                return $q.reject(rejection);*/
                $('#loader').hide();
                return rejection;
            },
            // optional method
            'response': function(response) {
                // do something on success
                $('#loader').hide();
                console.log('reponse from server is back');
                return response;
            },
            // optional method
            'responseError': function(rejection) {
                // do something on error
                /*if (canRecover(rejection)) {
                    return responseOrNewPromise
                }
                return $q.reject(rejection);*/
                $('#loader').hide();
                return rejection;
            }
        };
    }
]);
csa.config(['$httpProvider',
    function($httpProvider) {
        $httpProvider.interceptors.push('MyInterceptor');
        //hacking prevention
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        //adjust the header so request.is_ajax() in django will work
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    }
]);
/*
csa.config(['$resourceProvider',
    function($resourceProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }
]);*/
csa.config(['$locationProvider',
    function($locationProvider) {
        //Enable HTML5 routing
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });
        $locationProvider.hashPrefix('!');
    }
]);
