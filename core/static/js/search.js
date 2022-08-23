
document.addEventListener('mouseup', function(e) {
    var search_close = document.getElementById('search-icon');
    var input_close = document.getElementById('input-icon');


    if (!search_close.contains(e.target) && input_close.value === ""){ 

      search_close.classList.remove("actived");
      input_close.classList.remove("actived");


      }
  });
