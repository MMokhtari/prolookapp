/*var WorkplaceControllers = angular.module('WorkplaceControllers');
WorkplaceControllers.directive('editinplace', function($timeout,WorkplaceServices) {
    return {
        restrict: 'AE',
        replace: true,
        scope: {
            URL: '@dirurl',
            NAME: '@dirvar',
        }, //isolated scope
        templateUrl: "/static/csa/app/components/workplace/partials/editinplace.html",
        link: function(scope, elem, attrs) {
            scope.editvar = scope.NAME;
            scope.showEdit = false;
      		
            $("input#input1").width($("input#input1").textWidth(scope.editvar));
            scope.textclick = function() {
                scope.showEdit = true;
                setTimeout(function() {
                    $("input#input1").focus();
                }, 10);
            }
            scope.submit = function($event) {
                // hide the edit field
                scope.showEdit = false;
                // submit form
                //send to server
                console.log('sending to ' + scope.URL)
                if (scope.editvar == '') {
                    scope.editvar = scope.NAME;
                }else{
                	//send to sevrer
                	ser = WorkplaceServices.updatename(scope.editvar,scope.URL);
                	server = true;
                	if(server){
                		scope.NAME = scope.editvar;
                	}else{
                		console.log('cant be changed');
                	}
                	
                }
                
            }
            scope.changing = function() {
                //update the width of the input
                var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                if (len > 20) {
                    $("input#input1").width(len);
                }
            }
            scope.lostfocus = function() {
            	console.log('lostfocus')
                scope.editvar = scope.NAME;
                var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                $("input#input1").width(len);
                $("input#input1").val(scope.editvar);
                scope.showEdit = false;
            }
        }
    };
});*/