var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

//Fix link can't link
var dropDownLinkList = document.querySelectorAll('a.dropdown-item')
dropDownLinkList.forEach((link)=>{
  link.addEventListener('click',()=>{
    window.location.replace(link.href)
  })
})