from flask import Blueprint, render_template, flash, redirect, request
# from capstone_final.helpers import get_venue

from capstone_final.models import Venues, db
from capstone_final.forms import VenueForm, UpdateForm




site = Blueprint('site', __name__, template_folder='site_templates')




@site.route('/')
def restaurants():
    # get_venue("Red Robin")
    allprods = Venues.query.all()
    counter = 0
    return render_template('shop.html', restaurants=allprods, counter=counter)

@site.route('/restaurants/create', methods=['GET', 'POST'])
def create():
    createform = VenueForm()

    if request.method == 'POST' and createform.validate_on_submit():


        name = createform.name.data
        city = createform.city.data
        state = createform.state.data
        location = createform.location.data
        male = createform.male.data
        female = createform.female.data
        other = createform.other.data
        image = createform.image.data

        venue = Venues(name, city, state, location, male,female, other, image=image)

        db.session.add(venue)
        db.session.commit()

        flash(f"You have added a new Restaurant {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("Unable to add that Restaurant!", category='warning')
        return redirect('/restaurants/create')
    
    return render_template('create.html', form=createform)


@site.route('/shop/update/<id>', methods=['GET', 'POST'])
def update(id):
    venue = Venues.query.get(id)
    updateform = UpdateForm()

    if request.method == 'POST' and updateform.validate_on_submit():

        venue.male = updateform.male.data

        venue.female = updateform.female.data

        venue.other = updateform.other.data
    


        db.session.commit()

        flash(f"You have updated your restaurant {venue.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("Unable to update your restaurant!", category='warning')
        return redirect('/')
    
    return render_template('update.html', form=updateform, venue=venue)


@site.route('/shop/delete/<id>')
def delete(id):

    venue = Venues.query.get(id)

    db.session.delete(venue)
    db.session.commit()

    return redirect('/')
