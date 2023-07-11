$(document).ready(function () {
    $('#upload-form').on('submit', function(e) {
        e.preventDefault();
        $('#loading').show();
        $('#result').empty();
        var formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);
        formData.append('k', $('#k').val());
        $.ajax({
            url: '/query',
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function(data) {
                $('#loading').hide();

                var createSection = function(title, time, results) {
                    var section = $('<div class="result-section col-lg-4 col-md-6 col-sm-12 mb-4"></div>');
                    var titleElement = $('<h2 class="section-title">' + title + '</h2>');
                    var timeElement = $('<h4>TE: ' + time.toFixed(3) + ' ms</h4>');
                    section.append(titleElement);
                    section.append(timeElement);
                    results.forEach(function(item, index) {
                        var itemWrapper = $('<div class="item-wrapper"></div>');
                        var img = $('<img />', { src: item, alt: 'Result Image ' + (index + 1), class: 'img-thumbnail' });
                        itemWrapper.append('<p><b>Ranking: ' + (index + 1) + '</b></p>');
                        itemWrapper.append(img);
                        section.append(itemWrapper);
                    });
                    return section;
                }

                $('#result').append(createSection('Resultados Rtree', data.time_rtree, data.result_rtree));
                $('#result').append(createSection('Resultados Secuenciales', data.time_sequential, data.result_sequential));
                $('#result').append(createSection('Resultados KDTree', data.time_kdtree, data.result_kdtree));
            }
        });
    });
});
