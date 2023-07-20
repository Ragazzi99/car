const loader = document.querySelector('.loader-con');

window.addEventListener('load', function(){
    this.setTimeout(myLoad, 1000)
})
function myLoad(){
    loader.style.display = "none";
    document.body.style.overflow = "auto";
}