let clickCopy = document.getElementById('more-more');
let h1Copy = document.getElementById('aler_noter')
function btn_prew(){
    alert(h1Copy.innerText)
}

clickCopy.addEventListener('click',function(){
    btn_prew();
    h1Copy.style.display='none';
})