import requests
from bs4 import BeautifulSoup
 
"""first url if first is different than equation for rest"""
first = ["https://onlinereadfreenovel.com/john-flanagan/39929-rangers_apprentice_1_and_2_bindup_read.html"]

"""url list"""
url = ["https://onlinereadfreenovel.com/john-flanagan/p," + str(j) + ",39929-rangers_apprentice_1_and_2_bindup_read.html" for j in range(2, 44)]


"""Adds first to url list"""
tempurl = first
for link in url:
    tempurl.append(link)

url = tempurl


"""prints url list for checking"""
""" 
for i in url:
    print(i)
"""

writetofile = open(r"Ruins&Bridge.html", "wb")

"""Writes heading of HTML file encoded to UTF-8"""
writetofile.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruins And Bridge</title>
</head>

<style>
    *{
        background-color: black;
        color: white;
        padding-left:2px;
        margin:0px;
    }
    
    html{
		overflow: hidden;

		position: absolute;

		/*   use when full screened */
		margin-left: 4px;
		margin-right: 4px;

		min-width: 400px;
        padding-left: 5px;
        padding-right: 5px;
        padding-top: 2%;
        column-count: 2;
        column-gap: 50px;
        column-rule-width: calc(1300px * 2px);
        height: 95%;
    }
    
    body{
        width:100%;
        height:90%;
    }

    p{
        font-size: 1.3em;
    }
</style>

<body>
""".encode('utf-8'))


"""Writes all <p> tags from page encoded to UTF-8"""
for i in range(len(url)):
    r = requests.get(url[i])
    
    soup = BeautifulSoup(r.content, 'html5lib')

    soup = soup.findAll('p')

    for s in range(len(soup)):
        writetofile.write(soup[s].encode('utf-8'))
""" 
    x = input("Next Page") 
"""

"""Writes footer and JavaScript encoded to UTF-8"""
writetofile.write("""
</body>
<script>
let page = document.querySelector('html');
let dist =  1398/* 1398 if fullscreen, else 1390*/;

let pagesInBook = 600; //Eragon:294, Inheritance:515, Eldest:397, Brisingr:

if(localStorage.pageNum > 0){

    for(let i = 1; i < Number(localStorage.pageNum); i++){
        page.style.left = parseFloat(page.style.left || 0) - dist + 'px'; 
        page.style.right = parseFloat(page.style.right || 0) + dist + 'px';
    }

} else {
    localStorage.pageNum = 1;
}


document.addEventListener('keydown', (e) => {
    if (e.keyCode == 39 && Number(localStorage.pageNum) < pagesInBook){
        e.preventDefault();
        page.style.left = parseFloat(page.style.left || 0) - dist + 'px'; 
        page.style.right = parseFloat(page.style.right || 0) + dist + 'px';

        localStorage.pageNum = Number(localStorage.pageNum) + 1;
    }
    else if (e.keyCode == 37 && Number(localStorage.pageNum) > 1){
        e.preventDefault();
        page.style.left = parseFloat(page.style.left || 0) + dist + 'px'; 
        page.style.right = parseFloat(page.style.right || 0) - dist + 'px';

        localStorage.pageNum = Number(localStorage.pageNum) - 1;
    }
});
</script>
</html>
""".encode('utf-8'))
writetofile.close()
