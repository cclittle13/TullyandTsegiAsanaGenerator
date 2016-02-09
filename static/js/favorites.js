$(function (){ // this is the jquery shortcut for document.ready()

    function addToSequence(evt){

        var id = this.id; // this is the id on the button we clicked, which is the image's id

        $.post("/add-to-sequence", {'id': id}, addToSequenceSuccess);
    }

    function addToSequenceSuccess(result){

        console.log(result.status);

        var id = result.id;

        $('#' + id).css('color', 'red'); // give our user some feedback
    }

    $('.favorite-btn').click(addToSequence);

})