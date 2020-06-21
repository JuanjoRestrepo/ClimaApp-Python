import webbrowser
import random
count = 0

while count <= 3:
    sites = random.choice(['youtube.com', 'google.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    count += 1


