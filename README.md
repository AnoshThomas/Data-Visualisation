# Data-Visualisation

This folder contains the HTML documents index.html and index_1.html (first draft) and 15 csv files (for performance statistics for the years 2003-2017). Also a python script for generating the 15 csv files is supplied.


## Summary 

This visualisation aims to explore the on time performances of various american carriers through the years 2003-2017. 
In addition on selecting a specific year and carrier a second chart illustrates the distribution for that specific carrier (delayed, on time, cancelled) , the individual csv files were generated in a preprocessing step using a python script (preProcessAirlinePerfo.py)
to separate the data for each year. The ontime performance was calculated using teh formula onTimePerfo=1-delayed/arrivals. 

### Main Findings
On an average the on time performance of all aircraft lie within 80% with delays just over 15%.  The percentage of cancelled flights is less than 5%.

From the years 2003 to 2006 Skywest Airlines (OO) reported the best performances with the highest value of 89% in the year 2003.
Since 2008 Alaska Airlines (AS) consistently reported best performance figures in a consistent manner.
A strange pattern could be observed for Pinnacle Airlines (9E) which reported performance figures only for select years (2007 to 2010 and 2013). 
Furthermore it is interesting to note that in the initial years more airlines reported performance figures than the in most recent years (2016 and 2017). 

Looking at the development over time it seems there was a booming market from 2003 to ~2009 with an increasing variety of American carriers. After that it seems that that a few carriers established themselves and the rest got outperformed.



## Design

The main aim was to create an illustration showing the comparison of on time performances of various american carriers for the years 2003-2007. For this I chose to use bar charts with the values displayed on top of the bar chart. In addition i used a drop down widget for enabling the user to select the desired year.  

My initial design (index_1.html)  contained only the bar chart graph and after obtaining feedback I chose to include a second chart 
(pie-chart) which illustrated the statistics for a specific carrier in a given year. While hovering with the mouse on a bar would reflect the changes in the pie-chart. I added a legend and changed the color code to google style which was a bit more pleasing. 



## Feedback 

### user 1:Alvi Vincent (index_1.html)
  
•	  What do you notice in the visualization?

I can see the on time performance of various American carriers and their values for various years 

•	What questions do you have about the data?

How is the on time performance defined?  How was the data collection process performed? Did all Airlines report the statistics in a similar way?

•	What relationships do you notice?

I have the impression that the performance of the airlines has improved over the years but some airlines also have disappeared from the market 

•	What do you think is the main takeaway from this visualization?

It is possible to compare the on time performances of various carriers throughout the span of 15 years 

•	Is there something you don’t understand in the graphic?

Not really, The visualisation is quite self-explaining but I would recommend a second chart which illustrates some key characteristics for a specific carrier


### User 2: Filip Biedziak
•	What do you notice in the visualization?

I’m not 100% sure what you exactly mean by that. Do you mean what information I see? Well, that would be the performance of different American carriers measured by some number (above the bars) and categorizing deliveries by “on time”, “delayed” and “cancelled” over time.

•	What questions do you have about the data?

What do the numbers above the bars say? Has the amount of carriers decreased or increased? What about the amount of deliveries? How big is the market share of each carrier? This information would be helpful to interpret the data.

•	What relationships do you notice?

The number above the bars seems to correlate with the percentage of on-time deliveries. So I guess it is a measure for the performance (maybe customer satisfaction).

•	What do you think is the main takeaway from this visualization?

I would say that the overall performance is on time for all carriers. Looking at the development over time I would say that it was a booming market from 2003 to ~2009 with an increasing variety of American carriers. After that it seems that that a few carriers established themselves and the rest got outperformed. The overall performance does not change much, at least at first glance. Maybe a little increase over time, but usually around ~0.8.

•	Is there something you don’t understand in the graphic?

Not really. It is pretty straightforward. 


### User 3: Florian Blanc

Would you mind answering these questions?

•	What do you notice in the visualization?

[BLANC, Florian]  It is interactive and rather self-explaining, easy to enter. I like it 

•	What questions do you have about the data?

[BLANC, Florian] Was interested in seeing how performance has changed over the year but this is not really straightforward to explore as such.

•	What relationships do you notice?

[BLANC, Florian] The main performance degradation is related to delays in the operations and cancellations seems low in general.

•	What do you think is the main takeaway from this visualization?

[BLANC, Florian] Overall performance is about 0.8 with little deviations.

•	Is there something you don’t understand in the graphic?

[BLANC, Florian] In don’t clearly understand the link between the figures on top of the bar graph and the figures on the pie graph.

### Review 1 Feedback
During the previous review I receievd the feedback to include the summary on top of the project page which was realised here.
To avoid overlapping  of the pie chart labels I decided to place labels on the slices only if the values were greater than a certain 
threshold value as sugegsted in the review. Also for the airline codes I placed now each carrier in a separate line. 

### Review 2 Feedback
The main feedback was to include a separate title for the pie chart and also include the airline names in the x-axis of the 
bar charts. Initially the pei chart was also showing somewaht the information as the barchart but not making them comparable. 
Therefore I chose to show the actua flight distributions in the pie chart (with actual numbers) to give additional quantitative 
information about an airline (how many flights arrived on time that year, how many delayed). There was also a problem of overlapping
pie chart labels and now I placed them outside the pie chart. 

### Review 3 Feedback:
 Some labels were overlapping in the bar charts for Express Jet Airlines. The root cause was that there were multiple airline codes (XE/EV/RU) assigned to the same airline which was already in the RITA data set. I fixed this by updating the CSV's with one identifier
which I thought to be legitimate since we are dealing with the same airline. So now 15 new CSV's are provided and the pythons script to generate it. This should be solved by now. 

I rounded the bar chart labels and included a % sign as recommended. In addition I updated the pie chart title and the formatting of the numbers on the pie chart legend. 

Regarding bar order and consistency I chose to leave this as it is. The reason was that in my pre-processing step I generate specific files for each year and some airlines do not appear in all the years so I need 
to account this already in my pre-processing step and generate the data differently. 
Also the total number of unique airlines over the years is 28 and fitting them all in the bar chart would in my opinion make the chart more congested. 

## Resources: 

discussion on the udacity forum - Huge support from Myles !

google on usage of javascript and d3.js libraries 
