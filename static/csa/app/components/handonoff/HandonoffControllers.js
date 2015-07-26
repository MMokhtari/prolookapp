    var HandonoffControllers = angular.module('HandonoffControllers');

    HandonoffControllers.$inject = ['$location', '$scope'];
    /*Register Controller
     */
    HandonoffControllers.controller('RegisterController', function($scope, $location, HandonoffServices) {
        $("#register").hide();
        jQuery.fn.center = function() {
            this.css("position", "absolute");
            this.css("top", Math.max(0, (($(window).height() - $(this).outerHeight()) / 2) +
                $(window).scrollTop()) + "px");
            this.css("left", Math.max(0, (($(window).width() - $(this).outerWidth()) / 2) +
                $(window).scrollLeft()) + "px");
            return this;
        }
        $scope.enterpriseclick = function() {
            $("#enterprise").toggleClass('hvr-pop', 'True');
            setTimeout(function() {
                $('#enterprise').removeClass('hvr-pop');
            }, 500);
            setTimeout(function() {
                $("#free").toggleClass("animated bounceOut");
                setTimeout(function() {

                    $("#professional").toggleClass("animated bounceOut");
                    setTimeout(function() {
                        $("#enterprise").toggleClass("lefttomiddle");
                        setTimeout(function() {
                            $("#enterprise").hide();
                            $("#register").show();
                            $("#register").toggleClass("animated zoomIn");
                        }, 1000);
                    }, 200);
                }, 200);
            }, 500);
        };
        $scope.professionalclick = function() {

            $("#professional").toggleClass('hvr-pop', 'True');
            setTimeout(function() {
                $('#professional').removeClass('hvr-pop');
            }, 500);
            setTimeout(function() {
                $("#free").toggleClass('animated bounceOut', 'True');
                setTimeout(function() {

                    $("#enterprise").toggleClass('animated bounceOut', 'True');
                    setTimeout(function() {

                        //$("#professional").toggleClass("lefttomiddle");
                        setTimeout(function() {
                            $("#professional").hide();
                            $("#register").show();
                            $("#register").toggleClass("animated zoomIn");
                        }, 1000);
                    }, 200);
                }, 200);
            }, 500);
        };
        $scope.freeclick = function() {
            $("#free").toggleClass('hvr-pop', 'True');
            setTimeout(function() {
                $('#free').removeClass('hvr-pop');
            }, 500);
            setTimeout(function() {
                $("#professional").toggleClass('animated bounceOut', 'True');
                setTimeout(function() {

                    $("#enterprise").toggleClass('animated bounceOut', 'True');
                    setTimeout(function() {
                        $("#free").toggleClass("righttomiddle");
                        setTimeout(function() {
                            $("#free").hide();
                            $("#register").show();
                            $("#register").toggleClass("animated zoomIn");
                        }, 1000);

                    }, 200);
                }, 200);
            }, 500);
            // $("#enterprise").toggleClass('hvr-pop', 'False');
            //$("#login").toggleClass('outout', 'True');


        };
        /*    window.onpopstate = function(event) {
                if ($location.url() == '/signup/') {
                    $("#login").toggleClass('inin', 'False');
                    $("#login").toggleClass('outout', 'True');
                    $("#register").toggleClass('outout', 'False');
                    $("#register").toggleClass('inin', 'True');
                } else {
                    $("#register").toggleClass('inin', 'False');
                    $("#register").toggleClass('outout', 'True');
                    $("#login").toggleClass('outout', 'False');
                    $("#login").toggleClass('inin', 'True');
                }
            };*/
        comp_error_time = function(time, comp) {
            $(comp).toggleClass('errorInput', 'True');
            setTimeout(function() {
                $(comp).removeClass('errorInput');
            }, time);
        };
        $scope.register = function() {
            HandonoffServices.register($scope.newuser.email, $scope.newuser.username, $scope.newuser.password).then(function(promise) {
                console.log('promise');
                console.log(promise);
                console.log(promise.data.status);
                console.log(promise.data.content);
                if (promise.data.status == 'INVALID_INFO') {
                    var errors = promise.data.content;
                    for (var error in errors) {
                        //console.log(errors[error][0])
                        comp = "#reg_" + error + "_id";
                        comp_error_time(4000, comp);
                    }
                    // $("#username_id").focus();

                }
            });
        };
        /*
         *change the view from register view to signin view
         */
        $scope.tosignin = function() {
            //   window.history.pushState("", "", "../login/");
            $("#register").toggleClass("animated zoomIn", 'False');
            $("#register").toggleClass("animated zoomOut");

            setTimeout(function() {
                window.location = '/login/';
            }, 200);

            /* $("#register").toggleClass('inin', 'False');
             $("#register").toggleClass('outout', 'True');
             $("#login").toggleClass('outout', 'False');
             $("#login").toggleClass('inin', 'True');*/
        };
    });
    /*SignIn Controller 
     */
    HandonoffControllers.controller('SigninController', function($scope, $location, HandonoffServices) {
        /* window.onpopstate = function(event) {
             if ($location.url() == '/signup/') {
                 $("#login").toggleClass('inin', 'False');
                 $("#login").toggleClass('outout', 'True');
                 $("#register").toggleClass('outout', 'False');
                 $("#register").toggleClass('inin', 'True');
             } else {
                 $("#register").toggleClass('inin', 'False');
                 $("#register").toggleClass('outout', 'True');
                 $("#login").toggleClass('outout', 'False');
                 $("#login").toggleClass('inin', 'True');
             }
         };*/
        $scope.signin = function() {
            HandonoffServices.signin($scope.user.username, $scope.user.password).then(function(data) {
                if (data.data.status == 'INVALID_LOGIN') {
                    $("#username_id").focus();
                    $("#username_id").toggleClass('errorInput', 'True');
                    setTimeout(function() {
                        $("#username_id").removeClass('errorInput');
                    }, 2000);
                }
            });
        };
        /*
         *change the view from signin view to register view
         */
        $scope.toregister = function() {
            /*  $('#login').hide(); 
              $('#register').show();*/
            window.location = '/signup/';
            /* window.history.pushState("", "", "../signup/");
             $("#login").toggleClass('inin', 'False');
             $("#login").toggleClass('outout', 'True');
             $("#register").toggleClass('outout', 'False');
             $("#register").toggleClass('inin', 'True');*/
        };
    });
    /*SignOut Controller 
     */
    HandonoffControllers.controller('SignoutController', function($scope, HandonoffServices) {
        HandonoffServices.signout(this.email, this.password, this.username);
    });
