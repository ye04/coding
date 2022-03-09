document.addEventListener("DOMContentLoaded",
    function(e){
        let keydown=document.querySelector("#keydown")
        keydown.addEventListener("keydown",
            function(e){
                console.log(e.target.value)
            }
        )
        
        let change=document.querySelector("#change")
        change.addEventListener("change",
            function(e){
                console.log(e.target.value)
            }
        )

        let input=document.querySelector("#input")
        input.addEventListener("input",
            function(e){
                console.log(e.target.value)
            }
        )

        let input2=document.querySelector("#input2")
        input2.addEventListener("click",
            function(e){
                e.target.setAttribute("type","text")
            }
        )
        input2.addEventListener("change",
            function(e){
                e.target.setAttribute("type","button")
            }
        )
    }
)

function red(e){
    e.target.style.backgroundColor = "red"
}
function blue(e){
    e.target.style.backgroundColor = "blue"
}

