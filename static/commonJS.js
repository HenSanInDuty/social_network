$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})

//Fix link can't link
var dropDownLinkList = document.querySelectorAll('a.dropdown-item')
dropDownLinkList.forEach((link) => {
    link.addEventListener('click', () => {
        window.location.replace(link.href)
    })
})


//Image preview
const validImageTypes = ['image/gif', 'image/jpeg', 'image/png'];
var inputFiles = document.getElementById('image-post')
inputFiles.addEventListener('change', (value) => {
    document.querySelectorAll('.preview-img').forEach((value) => {
        value.remove()
    })
    let files = value.target.files
    let count = 0
    let parent = document.querySelector('.post-bottom')
    for (i = 0; i < files.length; i++) {
        value = files[i]
        if (count < 5) {
            if (validImageTypes.includes(value['type'])) {
                let imageElement = document.createElement('img')
                imageElement.src = URL.createObjectURL(value)
                imageElement.classList = 'rounded-circle img-fluid p-2 ms-2 preview-img'
                imageElement.alt = 'preview-img'
                parent.append(imageElement)
                count++
            }
        } else {
            break
        }
    }
})

//Delete post
var deleteButton = document.querySelectorAll('.delete-post-button')
deleteButton.forEach((value) => {
    value.addEventListener('click', () => {
        let id = value.id.substring(5)
        let deleteBtnConfirm = document.getElementById('btn-delte-post-sub')
        deleteBtnConfirm.value = id
    })
})

//Like post
var likeBtn = document.querySelectorAll('.like-js')
likeBtn.forEach((value) => {
    value.addEventListener('click', () => {
        let id = value.id.substring(10)
        var url = window.location.origin + `/likePost/${id}/`
        $.post(url)
            .done(() => {
                console.log("noan")
            })
    })
})