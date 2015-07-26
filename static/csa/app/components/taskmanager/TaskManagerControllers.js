    
    var TaskManagerControllers = angular.module('TaskManagerControllers');

    TaskManagerControllers.$inject = ['$location', '$scope', ];
    /*Register Controller
     */
    TaskManagerControllers.controller('TaskManagerController', function($scope, $http, $q, TaskManagerServices) {
        $scope.events = [{
            id: 1,
            text: "Task A-12458",
            start_date: new Date(2015, 10, 12),
            end_date: new Date(2015, 10, 16)
        }, {
            id: 2,
            text: "Task A-83473",
            start_date: new Date(2015, 10, 22),
            end_date: new Date(2015, 10, 24)
        }];
        $scope.scheduler = {
            date: new Date(2015, 10, 1)
        };
        $scope.scheduler.mode = "week";
        $scope.tags = [
            { text: 'just' },
            { text: 'some' },
            { text: 'cool' },
            { text: 'tags' }
          ];
          $scope.loadTags = function(query) {
            return $http.get('/tags?query=' + query);
          };
       /* $scope.starting = function() {
            console.log("clicking")
            console.log(scheduler);
            scheduler.config.xml_date = "%Y-%m-%d %H:%i";
            scheduler.init('scheduler_here', new Date(2015, 19, 10), "week");
            //scheduler.load("./data/events.xml");
        };*/
        /*function initCalander() {
            scheduler.config.multi_day = true;
            var pizza_size = [{
                key: 1,
                label: 'Small'
            }, {
                key: 2,
                label: 'Medium'
            }, {
                key: 3,
                label: 'Large'
            }];

            scheduler.locale.labels.section_text = 'Text';
            scheduler.locale.labels.section_checkbox = 'Checkbox';
            scheduler.locale.labels.section_radiobutton = 'Radiobutton';
            scheduler.locale.labels.section_select = 'Select';
            scheduler.locale.labels.section_template = 'Template';

            scheduler.config.lightbox.sections = [{
                name: "text",
                height: 50,
                map_to: "text",
                type: "textarea",
                focus: true
            }, {
                name: "checkbox",
                map_to: "single_checkbox",
                type: "checkbox",
                checked_value: "registrable",
                unchecked_value: "unchecked"
            }, {
                name: "radiobutton",
                height: 58,
                options: pizza_size,
                map_to: "radiobutton_option",
                type: "radio",
                vertical: true
            }, {
                name: "select",
                height: 21,
                map_to: "type",
                type: "select",
                options: pizza_size
            }, {
                name: "template",
                height: 21,
                map_to: "text",
                type: "template"
            }, {
                name: "time",
                height: 72,
                type: "calendar_time",
                map_to: "auto"
            }, {
                name: "time",
                height: 72,
                type: "time",
                map_to: "auto"
            }];

            scheduler.config.full_day = true;

            scheduler.config.xml_date = "%Y-%m-%d %H:%i";
            scheduler.init('scheduler_here', new Date(2015, 7, 5), "week");
            scheduler.load("./data/events.xml", function() {
                scheduler.showLightbox(47);
            });

        }
        initCalander();*/
    });
