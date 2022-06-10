var photoHovers = document.querySelectorAll('.photo-hover')

if (photoHovers){
    for (const photoDiv of photoHovers) {
        let photo = photoDiv.children[0]
        let name = photoDiv.children[1].children[0]
        let description = photoDiv.children[1].children[1]
        photoDiv.addEventListener('mouseenter', function(){
            
            photo.classList.add('md:h-fit', 'object-fit')
            photo.classList.remove('md:h-52', 'h-32' , 'object-cover')
            
            description.classList.remove('hidden')
        })
        photoDiv.addEventListener('mouseleave', function(){
            
            photo.classList.remove('md:h-fit', 'object-fit')
            photo.classList.add('md:h-52', 'h-32', 'object-cover')
            
            description.classList.add('hidden')
        })
    }
}
