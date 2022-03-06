site_name = "http//daum.com"
no_http = site_name.replace("http//", "")
no_dot = no_http[:no_http.index(".")]
final = no_dot[0:3] + str(len(no_dot)) + str(no_dot.count("e")) + "!"
print("{}의 비밀번호는 {}입니다".format(site_name, final))






