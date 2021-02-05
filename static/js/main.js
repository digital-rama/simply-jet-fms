const fieldBox = document.querySelector('.field-box')
const fieldContainer = document.querySelector('.field-container')
const delBtns = document.querySelectorAll('.del')
const addNewFields = document.querySelector('.add-fields')



document.addEventListener('click', (e) => {
    count = document.querySelectorAll('.field-container').length - 1;
    if (e.target.tagName === "I") {
        console.log("Remove", count);
        e.target.parentElement.remove()
    }
    if (count <= 9) {
        addNewFields.style.display = "block";
    }
})



let html_fields = `<div class="field-container">
        <div class="form-field">
            <label for="name">File Name</label>
            <input type="text" name="file-name" id="file-name" placeholder="Enter a File Name" autocomplete="email">
        </div>
        <div class="form-field">
            <label for="file">Upload a File</label>
            <input type="file" name="file" id="file">
        </div>
        <i class="del fas fa-minus-circle"></i>
    </div>`




addNewFields.addEventListener('click', () => {
    count = document.querySelectorAll('.field-container').length + 1;
    console.log("Add", count);
    if (count >= 10) {
        addNewFields.style.display = "none";
    } else {
        fieldBox.insertAdjacentHTML('beforeend', html_fields)
    }
    
})