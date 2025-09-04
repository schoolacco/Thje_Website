const num = document.getElementById('Num');
document.getElementById('upArrow').addEventListener('click', function() {
    let num_content = num.textContent
    let number = Number(num_content)
    let n = number + 1
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
   sessionStorage.setItem('friend', Number(num.textContent))
});

document.getElementById('up2').addEventListener('click', function(){
    const store = sessionStorage.getItem('friend')
    let num_content = num.textContent
    let number = Number(num_content)
    let n = number + 1
    if (n > store) {
        n = store
    }
    num.textContent = n
});