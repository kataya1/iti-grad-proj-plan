const menuBtn = document.querySelector('#menu-btn')
const links = document.querySelector('#links')
const nav = document.querySelector('nav')
menuBtn.addEventListener('click', (event)=>{
    event.stopPropagation()
    links.classList.toggle('links-visible')
})
nav.addEventListener('click',(e)=>{
    e.stopPropagation()
})
document.addEventListener('click',(event)=>{
    links.classList.remove('links-visible')
})

// .closest()
