from election_results import results
import matplotlib.pyplot as plt
import numpy as np

class Election:
    def __init__(self, district, dem_votes, rep_votes):
        self.district = district
        self.dem_votes = int(dem_votes)
        self.rep_votes = int(rep_votes)
    

def the_gap(year, state):
    dem_rep = []
    districts = []
    r = []
    d = []
    for district in results[year][state]:
        districts.append(district.district)
        local = 0
        wasted_rep = 0
        wasted_dem = 0
        local += int(district.rep_votes + district.dem_votes)
        if district.dem_votes > district.rep_votes:
                wasted_rep += district.rep_votes
                wasted_dem += (district.dem_votes - (local/2))
        if district.rep_votes > district.dem_votes:
                wasted_dem += district.dem_votes
                wasted_rep += (district.rep_votes - (local/2))
        dem_rep.append([wasted_dem, wasted_rep])
        d.append(wasted_dem)
        r.append(wasted_rep)
    
        print(d)
        print(r)
        
      
    # districts, dem_rep

    my_x = (dist for dist in districts)
    wasted_votes = {
        'Wasted Democratic Votes': (d),
        'Wasted Republicain Votes': (r),
    }

    
        
    x = np.arange(len(districts))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in wasted_votes.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Wasted Votes')
    ax.set_xlabel("Districts")
    ax.set_title('Wasted Votes by Voting District')
    ax.set_xticks(x + width, my_x)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 200000)

    plt.savefig("Election_Picture.png")
    plt.show()

year = str(input("What year would you like results from?: "))
state = str(input("What State would you like results from?: "))

#make 2 lists, one 2d of the wasted reps and dems, one of just the district codes.

the_gap(year, state)

# data from https://allisonhorst.github.io/palmerpenguins/

