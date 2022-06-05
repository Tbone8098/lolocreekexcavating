var contentBtns = document.querySelectorAll('.content-btn')

for (const btn of contentBtns) {
    btn.addEventListener('click', function(){
        deactivate()
        let infoSection = document.querySelector(`#${btn.getAttribute('info_section')}`)
        this.classList.add('active')
        infoSection.classList.remove('hidden')
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