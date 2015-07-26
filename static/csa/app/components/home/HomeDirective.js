angular.module('HomeControllers').directive('homedirective', function() {
    var directive = {};

    directive.restrict = 'E'; /* restrict this directive to elements and attribute*/

    directive.template = "You are the best";

    return directive;
});