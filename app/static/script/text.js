let friend = localStorage.getItem('friend')
let close_f= localStorage.getItem('close')
let result = null
if (friend != 0 && close != 0){
    result = `${Math.round((close_f/friend)*100)}%, an amount if nothing else.`
}
else {
    result = 'concering is it not'
}
document.getElementById('Text').textContent = `You claimed to have ${friend} friends, of which ${close_f} were considered close, ${result}` // Very efficient code usage