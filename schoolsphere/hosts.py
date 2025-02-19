from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'apps.school.urls', name='www'),
    # Any non-www subdomain goes to the dashboard URLConf.
    host(r'(?P<subdomain>.+)', 'apps.dashboard.urls', name='dashboard'),
)