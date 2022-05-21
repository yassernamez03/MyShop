const btn = document.querySelector('#btn')
const bin = document.querySelectorAll('.bin')
btn.addEventListener('click', () => {
    alert('are u sure')
})
bin.forEach(e => {
    e.addEventListener('click', () => {
        console.log('hello');
    })
})