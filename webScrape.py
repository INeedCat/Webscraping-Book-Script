import requests
from bs4 import BeautifulSoup

"""first url if first is different than equation for rest"""

first = []

"""url list"""
url = ["https://novel12.com/written-in-red/page-"+str(i)+"-"+str(2034913+i)+".htm" for i in range(1, 165)]

targetFile = r'TheOthers\WrittenInRed.html'

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


writetofile = open(targetFile, "wb")

"""Writes heading of HTML file encoded to UTF-8"""
writetofile.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Written In Red</title>
</head>

<style>
	body{
		width: 100vw;
		height: 100vh;
		background-color: black;

		overflow: hidden;
	}

	.container{
		position:absolute;
		left: 10vw;
		height: 95vh;
		min-width: 1100px;
	}

	.book{
		position: absolute;
		padding-top: 2vh;
		padding-bottom: 2vh;
		background-color: black;
		color: white;
		font-size: 1.2em;

		column-count: 2;
		column-gap: 5vw;
		column-width: 40%;
		height: inherit;
	}

	.cover{
		position: fixed;
		width: 20vw;
		height: 120vh;
		left: 93vw;
		top: -10vh;
		background-color: black;
	}

	.frontcover{
		position: fixed;
		width: 20vw;
		height: 120vh;
		left: -13vw;
		top: -10vh;
		z-index: 1;
		background-color: black;
	}

	.endblock{
		position: relative;
		width: 10px;
		height: 200vh;
		background-color: black;
	}
</style>

<body>
	<div class="frontcover"></div>

	<div class="container">
		<div class="book">
""".encode('utf-8'))

"""Writes all <p> tags from page encoded to UTF-8"""
for i in range(len(url)):
	r = requests.get(url[i])
	soup = BeautifulSoup(r.content, 'html5lib')
	soup = soup.findAll('p')

	for s in range(len(soup)-3):
		writetofile.write(soup[s].encode('utf-8'))
""" 
    x = input("Next Page") 
"""

"""Writes footer and JavaScript encoded to UTF-8"""
writetofile.write("""

			<div class="endblock"></div>
		</div>
	</div>

	<div class="cover"></div>

</body>

<script>
let page = document.querySelector('html');
let dist = 1167.9;/*1167.9 or 1168.3*/

//window.alert(document.querySelector('body').offsetWidth);

if(localStorage.pageNum > 0){

    for(let i = 1; i < Number(localStorage.pageNum); i++){
        page.style.left = parseFloat(page.style.left || 0) - dist + 'px'; 
        page.style.right = parseFloat(page.style.right || 0) + dist + 'px';
    }

} else {
    localStorage.pageNum = 1;
}

document.addEventListener('keydown', (e) => {
    if (e.keyCode == 39){
        e.preventDefault();

        window.scrollBy(dist, 0);

        localStorage.pageNum = Number(localStorage.pageNum) + 1;
    }
    else if (e.keyCode == 37){
        e.preventDefault();
        
        window.scrollBy(-dist, 0);

        localStorage.pageNum = Number(localStorage.pageNum) - 1;
    } 
    else if (e.keyCode == 38){
        e.preventDefault();

        if(dist != 1167.9){
            dist = 1167.9;
        } else {
            dist = 1168.3
        }
    }
});
</script>
</html>
""".encode('utf-8'))


writetofile.close()
