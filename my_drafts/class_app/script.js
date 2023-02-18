document.addEventListener("DOMContentLoaded",
    function(e){
        login = document.querySelector("#login")
        login.addEventListener("click",
            function(e){
                userInfo = prompt("아이디를 입력해주세요.")
                login.textContent = userInfo
            }
        )
    }
)