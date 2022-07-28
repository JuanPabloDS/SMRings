const form = document.querySelector(".form");
const search = document.querySelector(".fm-inp");
const btn = document.querySelector(".btn-search");
var url = "{% url 'index' %}"


btn.addEventListener("click", function() {
    if (search.value.length > 0) {
        window.location = " " + url + "#services";
    }else {
        form.classList.toggle("actived");
        search.classList.toggle("actived");
    }
});
