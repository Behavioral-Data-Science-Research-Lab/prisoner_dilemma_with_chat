from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.0005, participation_fee=1, mturk_hit_settings=dict(title='Choose to Cooperate or Compete', description='This study is interested in how two people work together or compete to earn points. ', keywords='bonus, study', frame_height=500, minutes_allotted_per_assignment=10, expiration_hours=168, grant_qualification_id='', qualification_requirements=[{'QualificationTypeId': '00000000000000000071', 'Comparator': 'EqualTo', 'LocaleValues': [{'Country': 'US'}]}], template='global/mturk_template.html'))
SESSION_CONFIGS = [dict(name='my_session', num_demo_participants=None, app_sequence=['prisoner'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


