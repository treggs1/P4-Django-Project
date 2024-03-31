from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the shopping cart """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a product with quantity to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
        else:
            bag[item_id]['items_by_size'][size] = quantity
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}

    request.session['bag'] = bag
    return redirect(redirect_url)