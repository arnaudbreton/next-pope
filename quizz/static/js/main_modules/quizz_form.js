require.config({
    paths: {
        'jquery': 'http://code.jquery.com/jquery-1.9.1.min',
        'bootstrap': '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min'
    },
    shim: {
        "bootstrap": ["jquery"]
    },
    baseUrl: window.staticUrl + 'js'
});

define('quizzForm',
    [
        'components/flight/lib/component',
        'jquery'
    ],
    function (defineComponent) {
        return defineComponent(quizzForm);

        function quizzForm() {
            this.defaultAttrs({
                overlay: $('#overlay'),
                container: '.form',
                containerMan: '#container_man',
                containerCatholic: '#container_catholic',
                containerMarried: '#container_married',
                containerCelibate: '#container_celibate',
                formText: '.form_text',
                prevButton: '.prev_button',
                postForm: 'form',
                formIsBound: '#form_is_bound',
                results: '#results',
                tweeterButton: '.twitter-share-button',
                tryAgain: '.try-again'
            });

            this.after('initialize', function () {
                if(this.select('formIsBound').val() === 'True') {
                    this.attr.overlay.show().find('.loading').show();
                    this.select('postForm').submit();
                }

                this.select('formText').find('a').click($.proxy(this.submitHandler, this));
                this.select('prevButton').click($.proxy(this.backHandler, this));
                this.select('tryAgain').click($.proxy(this.tryAgain, this));

                this.select('containerMan').show();
            });

            this.pushAnalytics = function(eventName) {
                window._gaq.push(['_trackEvent', 'Buddies', 'start', eventName]);
            }

            this.ajaxSend = function (url, method, data, success_handler, error_handler) {
                $.ajax({
                    url: url,
                    type: method,
                    dataType: 'json',
                    data: data,
                    success: success_handler,
                    error: error_handler,
                    beforeSend: function (xhr, settings) {
                        function getCookie(name) {
                            var cookieValue = null;
                            if (document.cookie && document.cookie != '') {
                                var cookies = document.cookie.split(';');
                                for (var i = 0; i < cookies.length; i++) {
                                    var cookie = jQuery.trim(cookies[i]);
                                    // Does this cookie string begin with the name we want?
                                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                        break;
                                    }
                                }
                            }
                            return cookieValue;
                        }

                        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                            // Only send the token to relative URLs i.e. locally.
                            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                        }
                    }
                });
            }

            this.submitHandler = function (event) {
                var target = $(event.target).closest('.form_text'),
                    data = target.data('value'),
                    form = this.select('postForm');

                if(this.select('containerMan').find(target).length) {
                    form.find('#id_is_man').prop('checked', data);
                }
                else if(this.select('containerCatholic').find(target).length) {
                    form.find('#id_is_catholic').prop('checked', data);
                }
                else if(this.select('containerMarried').find(target).length) {
                    form.find('#id_is_married').prop('checked', data);
                }
                else if(this.select('containerCelibate').find(target).length) {
                    form.find('#id_is_celibate').prop('checked', data);
                }

                var $currentForm = target.closest('.form'), $nextForm= $currentForm.next('.form');

                if($nextForm.length) {
                    $currentForm.fadeOut(500, function () { $nextForm.show(); });
                }
                else {
                    this.ajaxSend('/','POST', form.serialize(), $.proxy(this.successHandler, this));
                }
            }

            this.successHandler = function (data) {
                if(data && 'score' in data) {
                    var $results = this.select('results'), $resultsText = $results.find('h2'), $tweeterButton = this.select('tweeterButton');
                    this.select('container').hide();
                    if(data.score < 60) {
                        $resultsText.text("Damn! You definitely can't be the next pope :(.. Keep workin'");
                        $tweeterButton.data('text',"Damn! You definitely can't be the next pope :(.. Keep workin'");
                    }
                    else if(data.score < 80) {
                        $resultsText.text("Continue! You are definitely on the right track");
                        $tweeterButton.data('text',"Continue! You are definitely on the right track");
                    }
                    else {
                        $resultsText.text("Man! You definitely could be the next pope!");
                        $tweeterButton.data('text', "Man! You definitely could be the next pope!");
                    }
                    $results.show();
                }
            }

            this.backHandler = function (event) {
                var target = $(event.target),
                    $currentForm = target.closest('.form'), $prevForm= $currentForm.prev('.form');

                if($prevForm.length) {
                    $currentForm.fadeOut(500, function () { $prevForm.show(); });
                }

                this.pushAnalytics($currentForm.attr('id') + '_prev_button')
            }

            this.tryAgain = function () {
                this.select('results').hide();
                this.select('containerMan').show();
            }
        }
    });

require(
    [
        'quizzForm',
        'jquery',
        'bootstrap'
    ],
    function(QuizzForm) {
        QuizzForm.attachTo('#container');
    });