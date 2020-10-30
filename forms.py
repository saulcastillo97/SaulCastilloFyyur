from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL
from wtforms.validators import Regexp
import re

state_choices = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

genres_choices = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]

class ShowForm(Form):
    artist_id = StringField(
        'artist_id', validators=[
            DataRequired(),
        ]
    )
    venue_id = StringField(
        'venue_id'
    )
    image_link = StringField(
        'image_link'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )
#-----------------
class VenueForm(Form):
    #def validate_phone(form, field):
    #    if not re.search(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", field.data):
    #        raise ValidationError("Invalid phone number.")
    #def validate_genres(form, field):
    #    genres_values = [choice[1] for choice in genres_choices]
    #    for value in field.data:
    #        if value not in genres_values:
    #            raise ValidationError('Invalid genres value.')
    name = StringField(
        'name', validators=[DataRequired()]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
    'phone', validators=[Regexp(r'^[0-9\-\+]+$')]
    )
    image_link = StringField(
    'image_link'
    #, validators=[DataRequired(), URL()]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[DataRequired(), URL()]
    )
    website = StringField(
        'website', validators=[DataRequired(), URL()]
    )
    seeking_talent = SelectField(
       'seeking_talent', validators=[DataRequired()],
       choices=[
            (True, 'Yes'),
            (False, 'No'),
        ]
    )
    seeking_description = StringField(
        'seeking_description'
    )

#-----------------
#class VenueForm(Form):
    #venue_id = StringField(
    #    'venue_id', validators=[DataRequired()]
    #)
    #name = StringField(
    #    'name', validators=[DataRequired()]
    #)
    #city = StringField(
    #    'city', validators=[DataRequired()]
    #)
    #state = SelectField(
    #    'state', validators=[DataRequired()],
    #    choices=state_choices
    #)
    #address = StringField(
    #    'address', validators=[DataRequired()]
    #)
    #phone = StringField(
    #    'phone'
    #)
    #image_link = StringField(
    #    'image_link'
    #)
    #website = StringField(
    #    'website', validators=[URL()]
    #)
    #seeking_talent = SelectField(
    #    'seeking_talent', validators=[DataRequired()],
    #    choices=[
    #        (True, 'Yes'),
    #        (False, 'No'),
    #    ],
    #    coerce=lambda x: x == 'True'
    #)
    #seeking_description = StringField(
    #    'seeking_description',
    #)
    #genres = SelectMultipleField(
    #    # TODO implement enum restriction
    #    'genres', validators=[DataRequired()],
    #    choices=genres_choices
    #)
    #facebook_link = StringField(
    #    'facebook_link', validators=[URL()]
    #)

class ArtistForm(Form):
    #artist_id = StringField(
    #    'artist_id', validators=[DataRequired()]
    #)
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=state_choices
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[Regexp(r'^[0-9\-\+]+$')]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=genres_choices
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    seeking_venue = SelectField(
        'seeking_venue', validators=[DataRequired()],
        choices=[
            (True, 'Yes'),
            (False, 'No'),
        ]
    )
    seeking_description = StringField(
        'seeking_description'
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
