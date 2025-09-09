const num = document.getElementById('Num');
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
   localStorage.setItem('friend', Number(num.textContent))
   window.location.href='http://127.0.0.1:5000/intro_p2'
});

window.onload = function() {
      console.log(localStorage.getItem('friend'))
};
