from django.shortcuts import render, Http404

# Create your views here.
news_items = [
                 {
                     "id":1,
                     "title": "KK",
                     "image": "https://pierwszytrener.pl/wp-content/uploads/2014/03/kolko-i-krzyzyk.jpg",

                 },
                 {
                    "id":2,
                     "title": "Snake",
                     "image": "https://www.nhm.ac.uk/content/dam/nhm-www/discover/giant-snakes/reticulated-python-longest-snake-full-width.jpg",
                     "iframe": 'snake/index.html'
                 },
                 {
                    "id":3,
                     "title": "Tetris",
                     "image": "https://st2.depositphotos.com/1439706/5679/v/450/depositphotos_56794325-stock-illustration-dark-flat-tetris-background.jpg",
                      "iframe": 'tetris/index.html'
                 },
             ]


def index(request):
    context = {"news_items": news_items}

    return render(request, 'index.html', context)


def details(request, id):
    try:
        item = news_items[id - 1]
    except IndexError:
        raise Http404("Nie znaleziono wpisu.")

    context = {"item": item}
    return render(request, 'details.html', context)