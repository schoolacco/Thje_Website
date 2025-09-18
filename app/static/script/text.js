let friend = localStorage.getItem('friend')
let close_f= localStorage.getItem('close')
let result = null
if (friend != 0 && close_f != 0){
    result = `${Math.round((close_f/friend)*100)}%, close friends are valuable :D appreciate them.`
}
else if (close_f == 0){
    result = `${friend} friends, yet you consider none of them as close, that's an understandable issue, there are some people you may like to talk to perhaps but would not see them as a proper friend. Perhaps one or many of them will become closer to you one day, or maybe a close friend will come from somewhere else entirely, no matter, you aren't truly alone.`
}
else {
    result = "concerning, is it not? It can be hard to get through life without anyone outside of family to help you, and some don't even have that privilege.\nIn primary school I spent quite a while with no friends, I was never a socialable person, and I don't expect that I ever will be, but even you intentionally stay alone, just know people care more for you than you might think.\nIt doesn't matter what's happened to you, there's always a way to pick up the pieces and crawl your way back up.\nYou'll find friends one day, no matter what everyone else seems to think about you, everyone is flawed no matter how well they hide it, friendship is overlooking those flaws, and confronting them, surpassing them together, one day, no matter how long it takes, you'll find someone else who can help you in your life, and you too can help them.\nStay determined, for me is no one else won't you?"
}
document.getElementById('Text').textContent = `You claimed to have ${friend} friends, of which ${close_f} were considered close, ${result}` // Very efficient code usage