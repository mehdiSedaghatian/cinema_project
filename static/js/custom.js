function sendMovieComment(movieId) {
    var comment = $('#text').val();

    $.get('/movies/add-movie-comment', {
        movie_comment: comment,
        movie_id: movieId,

    }).then(res => {

        $('#comments_area').html(res);
        $('#text').val('');


        document.getElementById('content__tabs').scrollIntoView({behavior: "smooth"})


    });

}


function like(commentId, movieId) {
    $.get('/movies/like', {
        comment_id: commentId,
        movie_id: movieId
    }).then(res => {
        $('#like_and_dislike').html(res)

    })
}

function dislike(commentId, movieId) {
    $.get('/movies/dislike', {
        comment_id: commentId,
        movie_id: movieId
    }).then(res => {
        $('#like_and_dislike').html(res)

    })
}


function reviews(movieId) {
    var review_title = $('#review_title').val();
    var review_text = $('#review_text').val();
    var review_rate = $('#review_value').val();


    $.get('/movies/add-movie-review', {
        review_title:review_title ,
        review_text:review_text,
        review_rate:review_rate,
        movie_id: movieId,

    }).then(res => {

        $('#movie_reviews').html(res);
        $('#review_title').val('');
        $('#review_text').val('');


        document.getElementById('content__tabs').scrollIntoView({behavior: "smooth"})


    });

}


const value = document.querySelector("#review_value");
const input = document.querySelector("#review_input");
value.textContent = input.value;
input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});
