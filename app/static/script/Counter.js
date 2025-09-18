const num = document.getElementById('Num');
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem('friend') != null && localStorage.getItem('close') != null){
        window.location.href='http://127.0.0.1:5000/index'
}});
document.getElementById('upArrow').addEventListener('click', function() {
    let num_content = num.textContent
    let number = Number(num_content)
    let n = number + 1
    let store = localStorage.getItem('friend')
    if (store != null){
        if (n > store) {
        n = store
    }}
    num.textContent = n
});

document.getElementById('downArrow').addEventListener('click', function() {
    let num_content = num.textContent
    let number = Number(num_content)
    let n = number - 1
    if (n < 0) {
        n = 0
    }
    num.textContent = n
});
document.getElementById('submit').addEventListener('click', function() {
   if (localStorage.getItem('friend') == null){
     localStorage.setItem('friend', Number(num.textContent))
     window.location.href='http://127.0.0.1:5000/intro_p2'}
   else {
     localStorage.setItem('close', Number(num.textContent))
     window.location.href='http://127.0.0.1:5000/index'
   }
});

window.onload = function() {
      if (localStorage.getItem('friend') != null && localStorage.getItem('close') == null && window.location.href != "http://127.0.0.1:5000/intro_p2"){
        window.location.href="http://127.0.0.1:5000/intro_p2"
      }
      else if (localStorage.getItem('friend') != null && localStorage.getItem('close') != null) {
        window.location.href="http://127.0.0.1:5000/index"
      }
};
