document.addEventListener("DOMContentLoaded",
    function(e){
        let nameEditButton=document.querySelector("#nameEditButton")
        let editNameField=document.querySelector("#editNameField")
        let nameHere=document.querySelector("#nameHere")
        let newname=document.querySelector("#newname")
        let okButton=document.querySelector("#okButton")

        nameEditButton.addEventListener("click",
            function(e){
                editNameField.style.display = "block"
                nameEditButton.style.display = "none"
            }
        )
        okButton.addEventListener("click",
            function(e){
                nameHere.textContent = newname.value
                editNameField.style.display = "none"
                nameEditButton.style.display = "inline"
            }
        )
    }

)