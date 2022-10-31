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