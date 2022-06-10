var apiUpdateEls = document.querySelectorAll('.api-update')
var summernoteSubmit = document.querySelectorAll('.summernote-submit')

console.log(summernoteSubmit);

if (apiUpdateEls) {
    for (const el of apiUpdateEls) {
        el.addEventListener('change', function () {
            let content
            if (el.type === 'file') {
                content = el.files[0]
            } else {
                content = el.value
            }
            let url = el.getAttribute('url')
            let name = el.getAttribute('name')

            let form = new FormData()
            form.append(name, content)
            updateDb(url, form)
        })
    }
}

if (summernoteSubmit) {
    for (const btn of summernoteSubmit) {
        btn.addEventListener('click', async function () {
            let content = btn.previousElementSibling.children[2].lastChild.innerHTML
            let url = btn.parentElement.getAttribute('url')
            let name = btn.parentElement.getAttribute('name')

            console.log(name);

            form = new FormData()
            form.append(name, content)
            resp = await updateDb(url, form)
            console.log(resp);
        })
    }
}

async function updateDb(url, form) {
    resp = await fetch(url, {
        method: 'post',
        body: form
    })
    resp = await resp.json()
    return resp
}

async function confirmDelete(name, id, url) {
    resp = confirm(`Are you sure you want to delete the ${name}?`)
    if (resp){
        resp = await fetch(url)
        resp = await resp.json()
        console.log(resp.status);
        if (resp.status === 200){
            el = document.getElementById(`${id}-${name}`)
            el.parentElement.parentElement.remove()
        }
    }
}

href="/admin/album/{{ album.id }}/delete"