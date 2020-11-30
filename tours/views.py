from django.shortcuts import render
import tours.dataset as dataset
from random import seed, randint


# Create your views here.
def main_view(request):
    seed()
    tours = []
    while len(tours) != 6:
        index = randint(1, len(dataset.tours))
        if dataset.tours[index] not in tours:
            tours.append(dataset.tours[index])
    return render(request, 'tours/index.html', {
        'departures': dataset.departures,
        'tours': tours,
        'title': dataset.title,
        'subtitle': dataset.subtitle,
        'description': dataset.description,
    })


def departure_view(request, departure):
    tours = []
    price = []
    nights = []
    for i in dataset.tours:
        tour = dataset.tours[i]
        if tour['departure'] == departure:
            tours.append(tour)
            price.append(tour['price'])
            nights.append(tour['nights'])
    return render(request, 'tours/departure.html', {
        'departures': dataset.departures,
        'departure': dataset.departures[departure],
        'tours': tours,
        'tours_info': {
            'count': len(tours),
            'start_price': min(price),
            'end_price': max(price),
            'start_night': min(nights),
            'end_night': max(nights),
        }
    })


def tour_view(request, id):
    tour = dataset.tours.get(id)
    return render(request, 'tours/tour.html', {
        'departures': dataset.departures,
        'tour': tour,
        'departure': dataset.departures[tour['departure']],
    })
