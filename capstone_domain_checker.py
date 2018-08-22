import urllib.request
from termcolor import colored
import ssl
ssl.match_hostname = lambda cert, hostname: True

domain = "cscapstone.us"
system_subdomains = [
    'web',
    'gitea',
    'ci',
    'registry'
]
student_subdomains = [
    'callout',
    'refugees',
    'thailandcld',
    'thailandmh',
    'vfront',
    'drm',
    'biofuels',
    'cc',
    'linkup'
]


def check_status(url):
    try:
        code = urllib.request.urlopen(url).getcode()
        if code == 200:
            return colored(code, 'green', attrs=['bold'])
        elif code == 404:
            return colored(code, 'red', attrs=['bold'])
        elif code == 502:
            return colored(code, 'red', attrs=['bold', 'reverse'])
        else:
            return colored(code, 'red', attrs=['bold'])
    except Exception as e:
        return colored(e, 'yellow', attrs=['bold'])

print("Checking domain status codes for: Student Applications")
print("======================================================")

for stud_subdomain in student_subdomains:
    print('-----> {:<15}'.format(stud_subdomain),
          '{:>30}'.format(check_status('https://' + stud_subdomain + '.' + domain)))

print("\n\nChecking domain status codes for: System Applications")
print("======================================================")
for sys_subdomain in system_subdomains:
    print('-----> {:<15}'.format(sys_subdomain),
          '{:>30}'.format(check_status('https://' + sys_subdomain + '.' + domain)))
