(function(){
    if (window.MyBookmarklet !== undefined){
        MyBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://d8202ab9.ngrok.io/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();
