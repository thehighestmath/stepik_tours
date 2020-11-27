from django.shortcuts import render
import tours.dataset as dataset
from random import seed, randint


# Create your views here.
def main_view(request):
    tours = []
    while len(tours) != 6:
        index = randint(1, len(dataset.tours))
        if dataset.tours[index] not in tours:
            tours.append(dataset.tours[index])
    return render(request, 'tours/index.html', {
        'departures': dataset.departures,
        'tours': tours,
    })


def departure_view(request, departure):
    return render(request, 'tours/departure.html', {
        'departures': dataset.departures
    })


def tour_view(request, id):
    tour = dataset.tours.get(id)
    print(tour)
    tour['stars'] = '★' * int(tour['stars'])
    return render(request, 'tours/tour.html', {
        'departures': dataset.departures,
        'tour': tour
    })
