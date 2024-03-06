from flask import Blueprint, render_template, flash, redirect, request
# from capstone_final.helpers import get_venue

from capstone_final.models import Venues, db
from capstone_final.forms import VenueForm



site = Blueprint('site', __name__, template_folder='site_templates')




@site.route('/')
def restaurants():
    # get_venue("Red Robin")
    allprods = Venues.query.all()
    return render_template('restaurants.html', restaurants=allprods)

@site.route('/restaurants/create', methods=['GET', 'POST'])
def create():
    createform = VenueForm()

    if request.method == 'POST' and createform.validate_on_submit():

        demographics_percent = createform.demographics.data / 100.0

        name = createform.name.data
        city = createform.city.data
        state = createform.state.data
        location = createform.location.data
        demographics_percent = createform.demographics.data

        venue = Venues(name, city, state, location, demographics=demographics_percent)

        db.session.add(venue)
        db.session.commit()

        flash(f"You have added a new Restaurant {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("Unable to add that Restaurant!", category='warning')
        return redirect('/restaurants/create')
    
    return render_template('create.html', form=createform)


@site.route('/restaurants/update/<id>', methods=['GET', 'POST'])
def update(id):
    venue = Venues.query.get(id)
    updateform = VenueForm()

    if request.method == 'POST' and updateform.validate_on_submit():

        demographics_percent = updateform.demographics.data / 100.0


        venue.name = updateform.name.data
        venue.city = updateform.city.data
        venue.state = updateform.state.data
        venue.location = updateform.location.data
        venue.demographics = demographics_percent

        db.session.commit()

        flash(f"You have updated your restaurant {venue.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("Unable to update your restaurant!", category='warning')
        return redirect('/')
    
    return render_template('update.html', form=updateform, venue=venue)


@site.route('/restaurants/delete/<id>')
def delete(id):

    venue = Venues.query.get(id)

    db.session.delete(venue)
    db.session.commit()

    return redirect('/')
