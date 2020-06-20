import bs4

exampleFile = open('C:\\Users\\Anna\\PycharmProjects\\sandBox\\python_practice\\AutomateBoringStuff\\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
