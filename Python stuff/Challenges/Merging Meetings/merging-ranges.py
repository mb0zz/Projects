'''
Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges.

For example, given:

	[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

	[(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. 
Here we've simplified our times down to the number of 30-minute slots past 9:00 am.
But we want the function to work even for very large numbers, like Unix timestamps.
 
In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.
'''

def condense_meeting_times(meeting_times):
	#meeting_times is a list of tuples.
	
	ordered_meetings = sorted(meeting_times)
	
	final_meetings = [(ordered_meetings[0])]
	
	for meeting in range(len(ordered_meetings)-1):

		if final_meetings[-1][1] < ordered_meetings[meeting + 1][0]:
			final_meetings.append((ordered_meetings[meeting + 1]))
		else:
			final_meetings[-1] = final_meetings[-1][0],ordered_meetings[meeting + 1][1]

	return final_meetings
	
my_list = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

final = condense_meeting_times(my_list)
print(final)
		
		
		
