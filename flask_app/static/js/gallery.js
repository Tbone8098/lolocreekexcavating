var coverPhotoDelete = document.querySelectorAll('.cover-photo-delete')

for (const btn of coverPhotoDelete) {
    btn.addEventListener('click', function () {
        deleteCoverPhoto(this)
    })
}

async function deleteCoverPhoto(btn) {
    let parent = btn.parentElement
    let albumId = btn.getAttribute('album_id')
    parent.innerHTML = `
        <input class="cover-update" type="file" name="cover_image" id="cover_image"
                                url="/api/album/${albumId}/update">
        `

    // parent.children[0].addEventListener('change', function () {
    //     updateCover(parent.children[0])
    // })

    let form = new FormData()
    form.append('cover_image_url', '')

    resp = await fetch(`/api/album/${albumId}/update`, {
        method: 'post',
        body: form
    })
    if (resp){
        window.location.reload()
    }

}

var coverUpdate = document.querySelectorAll('.cover-update')

for (const el of coverUpdate) {
    el.addEventListener('change', async function () {
        console.log("*****");
        let resp = await updateCover(el)
        console.log("&&&&");
        console.log(resp.status);
        if (resp.status == 200) {
            window.location.reload()
            // console.log(el);
            // el.innerHTML = `
            // <img src="${resp.url}" alt="cover image" width="100px">
            // <span class="cover-photo-delete cursor-pointer" album_id="${resp.id}">❌</span>
            // `

            // el.children[0].addEventListener('click', function(){
            //     deleteCoverPhoto(el.children[0])
            // })
        }
    })
}

async function updateCover(el) {
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
    let resp = await updateDb(url, form)
    return resp
}