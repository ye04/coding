document.addEventListener("DOMContentLoaded",
    function(e){
        let configID = document.querySelector("#id i")
        let idText = document.querySelector("#id span")

        configID.addEventListener("click",
            function(e){
                idText.textContent = prompt("Write your new id here")
            }
        )

        let profileEditButton = document.querySelector("#profile_info button")
        let userInfo = document.querySelector("#userInfo")
        let summary = document.querySelector("#summary")
        let profileDetail = document.querySelector("#profileDetail")
        let changing = false

        profileEditButton.addEventListener("click",
            function(e){
                if(changing){
                    let _userInfo = userInfo.querySelector("input").value
                    let _summary = summary.querySelector("input").value
                    let _profileDetail = profileDetail.querySelector("input").value
                    
                    userInfo.innerHTML = _userInfo
                    summary.innerHTML = _summary
                    
                    if (_profileDetail.startsWith("http")){
                        _profileDetail = "<a href="+ _profileDetail +">"+ _profileDetail + "</a>"
                    }

                    profileDetail.innerHTML = _profileDetail
                    
                    e.target.textContent = "Edit Profile"
                    changing = false
                } else{
                    let _userInfo = userInfo.textContent
                    let _summary = summary.textContent
                    let _profileDetail = profileDetail.textContent
                    
                    userInfo.innerHTML = "<input value=" + _userInfo + "></input>"
                    summary.innerHTML = "<input value=" + _summary + "></input>"
                    profileDetail.innerHTML = "<input value=" + _profileDetail + "></input>"

                    e.target.textContent = "Finish Editing Profile"
                    changing = true
                }
            }
        )
        let profile_pic = document.querySelector("#profile_pic .circle_pic")

        profile_pic.addEventListener("mouseover",
            function(e){
                e.target.style.filter = "grayscale(50%)"
            }
        )
        profile_pic.addEventListener("mouseleave",
        function(e){
            e.target.style.filter = "grayscale(0%)"
        }
        )
        profile_pic.addEventListener("click", 
            function(e){
                let _profile_pic = prompt("Type the image url")
                console.log(_profile_pic)
                profile_pic.setAttribute("src", _profile_pic)
            }
        )

    }

)