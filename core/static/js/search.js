
const form = document.querySelector(".form");
const search = document.querySelector(".fm-inp");
const btn = document.querySelector(".btn-search");
var url = "{% url 'index' %}"


btn.addEventListener("click", function() {
    if (search.value.length > 0) {
        window.location = "../#services";
    }else {
        form.classList.toggle("actived");
        search.classList.toggle("actived");
    }
});

      
document.addEventListener('mouseup', function(e) {
    var search_close = document.getElementById('search-icon');
    var input_close = document.getElementById('input-icon');


    if (!search_close.contains(e.target) && input_close.value === ""){ 

      search_close.classList.remove("actived");
      input_close.classList.remove("actived");


      }
  });
