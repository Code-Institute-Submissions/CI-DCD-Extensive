from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from bandx.models.entities import User, Towns
from wtforms import (BooleanField, DateField, Form, FormField, FieldList, HiddenField, 
                      RadioField, SelectField, SelectMultipleField, StringField, SubmitField, TextAreaField,)

from wtforms.validators import DataRequired, Optional, Length, EqualTo, Email, URL, ValidationError
 

class SearchForm(FlaskForm):
    q = StringField("Text Query")
    origin_county = SelectMultipleField("From County", choices = [
                                ("Antrim",	"Antrim"),
                                ("Armagh",	"Armagh"),
                                ("Carlow",	"Carlow"),
                                ("Cavan",	"Cavan"),
                                ("Clare",	"Clare"),
                                ("Cork",	"Cork"),
                                ("Derry",	"L/Derry"),
                                ("Donegal",	"Donegal"),
                                ("Down",	"Down"),
                                ("Dublin",	"Dublin"),
                                ("Fermanagh", "Fermanagh"),	
                                ("Galway",	"Galway"),
                                ("Kerry",	"Kerry"),
                                ("Kildare",	"Kildare"),
                                ("Kilkenny","Kilkenny"),
                                ("Laois",	"Laois"),
                                ("Leitrim",	"Leitrim"),
                                ("Limerick","Limerick"),	
                                ("Longford","Longford"),	
                                ("Louth",	"Louth"),
                                ("Mayo",	"Mayo"),
                                ("Meath",	"Meath"),
                                ("Monaghan","Monaghan"),	
                                ("Offaly",	"Offaly"),
                                ("Roscommon","Roscommon"),
                                ("Sligo",	"Sligo"),
                                ("Tipperary", "Tipperary"),	
                                ("Tyrone",	"Tyrone"),
                                ("Waterford", "Waterford"),	
                                ("Westmeath", "Westmeath"),	
                                ("Wexford",	"Wexford"),
                                ("Wicklow",	"Wicklow")
                                ],
                                render_kw={"class": "origin-county", "size": "6"})
    andor = RadioField("", 
                        choices=[("false","any"), ("true","Match ALL")],
                        render_kw={},
                        default="false")
    genres = StringField("Musical Genres", 
                            render_kw={"id": "testInput",
                                    "style":"text-transform: lowercase;",
                                    })

        #letter