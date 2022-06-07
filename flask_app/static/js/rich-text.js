$(document).ready(function () {
    $('#summernote').summernote();
    $('#summernote').on('focusout', function(){
        console.log('testing');
    })
    
});