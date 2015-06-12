import os,datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'three_megawatt_project.settings')

import django
django.setup()

from demo.models import Site, SiteDetail


def populate():
    demo_site = add_site('Demo Site')

    add_site_details(site=demo_site,
        date=datetime.datetime(2015,2,1),
        a_value=12,
        b_value=16)

    add_site_details(site=demo_site,
        date=datetime.datetime(2015,2,3),
        a_value=20,
        b_value=100)

    add_site_details(site=demo_site,
        date=datetime.datetime(2015,2,10),
        a_value=20,
        b_value=80)

    abc_site = add_site("ABC Site")

    add_site_details(site=abc_site,
        date=datetime.datetime(2015,2,3),
        a_value=5,
        b_value=5)

    xyz_site = add_site("XYZ Site")

    add_site_details(site=xyz_site,
        date=datetime.datetime(2015,2,15),
        a_value=5,
        b_value=15)

    add_site_details(site=xyz_site,
        date=datetime.datetime(2015,2,25),
        a_value=5,
        b_value=15)


    # Print out what we have added to the database.
    for s in Site.objects.all():
        for sd in SiteDetail.objects.filter(site=s):
            print "- {0} - {1}".format(str(s), str(sd))

def add_site_details(site, date, a_value=0, b_value=0):
    sd = SiteDetail.objects.get_or_create(site=site,date=date,a_value=a_value,b_value=b_value)[0]
    return sd

def add_site(name):
    s = Site.objects.get_or_create(name=name)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Demo population script..."
    populate()