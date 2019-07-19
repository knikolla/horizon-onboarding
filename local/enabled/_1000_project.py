# The slug of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'project'

# A dictionary of exception classes to be added to HORIZON['exceptions'].
ADD_EXCEPTIONS = {}
# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = ['openstack_dashboard.dashboards.project']

ADD_ANGULAR_MODULES = [
    'horizon.dashboard.project',
]

AUTO_DISCOVER_STATIC_FILES = True

ADD_JS_FILES = []

ADD_JS_SPEC_FILES = []

DEFAULT = True