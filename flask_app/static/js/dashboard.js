
function inProcess(message_id){
    console.log(message_id);
    
    let form = new FormData()
    form.append('in_process', 1)

    fetch(`/api/admin/message/${message_id}/update`, {
        method: 'post',
        body: form
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.status === 200){
            window.location.reload()
        }
    })
}