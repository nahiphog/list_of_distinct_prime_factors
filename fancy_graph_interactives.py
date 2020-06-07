''' (FAR from complete) and CSV and shitz
https://colab.research.google.com/drive/1tlJBMVK5gaEiEZMHBQsQL6Zrroax7kgg?usp=sharing#scrollTo=iKiPAXxUiNnZ
'''

import numpy as np

num_callers = 330 * (10 ** 0)

def generate_meeting_times():
    # Generate array of a start and end time for all people in America
    meeting_times = np.random.rand(num_callers, 2)

    # Sort the array so that the smaller number comes first
    meeting_times = np.sort(meeting_times, axis = 1)

    return meeting_times

##############

def check_overlap(person1_times, person2_times):
    person1_start = person1_times[0]
    person1_end = person1_times[1]

    person2_start = person2_times[0]
    person2_end = person2_times[1]

    return (person1_start < person2_start < person1_end) or (person2_start < person1_start < person2_end)

#####################

def overlaps_everyone(meeting_times, person_index):
    person_times = meeting_times[person_index]

    for index in [x for x in range(len(meeting_times)) if x != person_index]:
        if not (check_overlap(person_times, meeting_times[index])):
            return False
    
    return True

#####################

num_iterations = 500

all_num_intersections = np.zeros(num_iterations)

for iter_num in range(0, num_iterations):
    meet_times = generate_meeting_times()

    num_intersections = 0

    for overlap_person_index in range(0, len(meet_times)):
        if overlaps_everyone(meet_times, overlap_person_index):
            num_intersections += 1
    all_num_intersections[iter_num] = num_intersections



######################

import plotly.graph_objects as go

fig = go.Figure(data=[go.Histogram(x=all_num_intersections, histnorm='probability')])

fig.update_layout(
    title_text='Histogram of Number of Attendees Who Met Everyone', 
    xaxis_title_text='Number of Attendees Who Met Everyone', 
    yaxis_title_text='Probability of Occurrence', 
    bargap=0.2, 
)

fig.show()
