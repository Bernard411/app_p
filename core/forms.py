from django import forms

class PlantDiagnosisForm(forms.Form):
    LEAF_COLORS = [
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('brown', 'Brown'),
        ('black', 'Black'),
        ('purple', 'Purple'),
    ]

    LEAF_SHAPES = [
        ('oval', 'Oval'),
        ('heart', 'Heart'),
        ('lance', 'Lance'),
        ('round', 'Round'),
    ]

    STEM_CONDITIONS = [
        ('healthy', 'Healthy'),
        ('soft', 'Soft'),
        ('brittle', 'Brittle'),
        ('discolored', 'Discolored'),
    ]

    SOIL_TYPES = [
        ('clay', 'Clay'),
        ('sandy', 'Sandy'),
        ('silty', 'Silty'),
        ('peaty', 'Peaty'),
        ('chalky', 'Chalky'),
        ('loamy', 'Loamy'),
    ]

    WEATHER_CONDITIONS = [
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
        ('rainy', 'Rainy'),
        ('windy', 'Windy'),
    ]

    WATERING_FREQUENCY = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly'),
    ]

    leaf_color = forms.ChoiceField(choices=LEAF_COLORS, required=True, label='Leaf Color')
    leaf_shape = forms.ChoiceField(choices=LEAF_SHAPES, required=True, label='Leaf Shape')
    spots_on_leaves = forms.BooleanField(required=False, label='Spots on Leaves')
    wilting = forms.BooleanField(required=False, label='Wilting')
    mold_growth = forms.BooleanField(required=False, label='Mold Growth')
    stem_condition = forms.ChoiceField(choices=STEM_CONDITIONS, required=False, label='Stem Condition')
    soil_type = forms.ChoiceField(choices=SOIL_TYPES, required=True, label='Soil Type')
    weather_conditions = forms.ChoiceField(choices=WEATHER_CONDITIONS, required=True, label='Weather Conditions')
    watering_frequency = forms.ChoiceField(choices=WATERING_FREQUENCY, required=True, label='Watering Frequency')
    pest_presence = forms.BooleanField(required=False, label='Pest Presence')
    fertilizer_use = forms.CharField(max_length=100, required=False, label='Fertilizer Use')
    # Add more fields as necessary
