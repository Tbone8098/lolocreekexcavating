var contentBtns = document.querySelectorAll('.content-btn')
var closeBtn = document.querySelectorAll('.close-btn')

for (const btn of contentBtns) {
    btn.addEventListener('click', function(){
        deactivate()
        let infoSection = document.getElementById([id=`${btn.getAttribute('info_section')}`])
        this.classList.add('active')
        infoSection.classList.remove('hidden')
        infoSection.classList.remove('slide-out-left')
        infoSection.classList.add('slide-in-left')
    })
}

function deactivate(){
    let sections = document.querySelectorAll('.info-section')
    for (const btn of contentBtns) {
        btn.classList.remove('active')
    }

    for (const section of sections) {
        section.classList.add('hidden')
    }
}

for (const btn of closeBtn) {
    btn.addEventListener('click', function(){
        let grandparent = this.parentElement.parentElement
        grandparent.classList.remove('slide-in-left')
        grandparent.classList.add('slide-out-left')
    })
}