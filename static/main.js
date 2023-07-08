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

                var rtreeSection = $('<div class="result-section"></div>');
                rtreeSection.append('<h2>Resultados Rtree - Tiempo de ejecución: ' + data.time_rtree.toFixed(2) + ' segundos</h2>');
                data.result_rtree.forEach(function(item, index) {
                    var img = $('<img />', { src: item, alt: 'Result Image ' + (index + 1), class: 'img-thumbnail', width: 200, height: 200 });
                    rtreeSection.append('<p>Ranking: ' + (index + 1) + '</p>');
                    rtreeSection.append(img);
                });
                $('#result').append(rtreeSection);

                var sequentialSection = $('<div class="result-section"></div>');
                sequentialSection.append('<h2>Resultados Secuenciales - Tiempo de ejecución: ' + data.time_sequential.toFixed(2) + ' segundos</h2>');
                data.result_sequential.forEach(function(item, index) {
                    var img = $('<img />', { src: item, alt: 'Result Image ' + (index + 1), class: 'img-thumbnail', width: 200, height: 200 });
                    sequentialSection.append('<p>Ranking: ' + (index + 1) + '</p>');
                    sequentialSection.append(img);
                });
                $('#result').append(sequentialSection);
            }
        });
    });
});
