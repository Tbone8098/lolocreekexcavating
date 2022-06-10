// $(document).ready(function () {
//     $('#summernote').summernote();
//     $('#summernote').on('focusout', function(){
//         console.log('testing');
//     })
// });

$(document).ready(function () {
    $('#summernote').summernote({
        height: 300,
        lineWrapping: true,
        toolbar: [
            ['style', ['style']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['font', ['bold', 'underline', 'clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link']],
        ]
    });
});