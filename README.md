# NFL_QBR
Analysis of Travel Distance on NFL Quarterback performance in the 2022 season

Player performance is almost always measured with stats in the scorebook. But what if there were unseen factors at play that affect those stats?. Factors such as weather, injuries, etc. However one factor unfrequently considered is travel. The distance traveled by a visiting team and the uneasy nature of traveling as an athlete is what this project aims to analyze. Many professional athletes are creatures of habit, maybe non moreso than NFL Quarterbacks, so lets take a simple look at how these creatures deal with traveling. 

This project analyzes a small dataset collected by myself from a few different web sources that was integrated into a two excel workbooks-one for team performance and one for quarterback performance- that I then performed tranformations and visualizations on. These web sources include wegrynenterprises.com for accurate travel distances for NFL teams, and NFL.com and pro-football_reference.com for team and player stats. This dataset is specifically pertaining to the 2022 NFL season and the quarterbacks with over 300 pass attempts (30). Each distance listed in the workbook is the distance from city to city, not actually stadium to stadium to keep the distances uniform. There are a few disclaimers for travel distance as well. There were 5 international NFL games played in countries other than the United States and they are as follows: Week 11 SF @ AZ in Mexico City, Week 10 SEA @ TB in Munich, Germany, and 3 contests in London- Week 4 MIN @ NO, Week 5 NYG @ GB, and Week 8 DEN @ JAX. Note that AZ quarterback Kyler Murray did not play in the Mexico City game, so his longest travel distance is reflected in a stateside game. Two other disclaimers: Week 11 CLE @ BUF was not played in Buffalo, NY but rather at a nuetral site in Detroit, MI due to inclement weather in Buffalo and Week 17 BUF @ CIN was canceled after 10 minutes due to the cardiac arrest of BUF cornerback Damar Hamlin so this game is not reflected in BUF quarterback Josh Allen's distances while the Week 11 game in Detroit is his shortest travel distance (~284 miles) even though it was a home game for Buffalo. This Week 11 neutral site game is also reflected in CLE quarterback Jacoby Brissett's shortest travel distance (~90 miles). 

I began with team performance, since NFL games are played with 11 players on the field at once not just a quarterback. My workbook includes the winning percentage for the season, road winning percentage, divisional winning percentage, total distance traveled for divisional games, total distance traveled for all games, and total international distance traveled, if applicable. I ran two simple regression plots on this dataset below. One for distance traveled vs yearly winning percentage and distance traveled vs yearly divisional winning percentage.  


![NFL Total Distance Traveled vs Yearly Winning Percentages](https://github.com/user-attachments/assets/1a29596b-6370-4fd1-85ff-57f419dd0770)

![NFL Total Divisional Distance Traveled vs Yearly Divisional Winning Percentages](https://github.com/user-attachments/assets/73eeca5c-91a5-4313-bbbc-4e4e2f1f659f)


We can see the line of best fit for the first plot is almost flat right down the middle meaning there is no linear relationship between distance traveled and team winning percentage. There may be a different relationship but this project is only concerned with a linear relationship. There is a slightly higher amount of relation between distance traveled and divisional winning percentage; this could be skewed however due to certain divisional games being played internationally. 

The quarterback specific analysis gives us a slighty better understanding of how distance effects performance. I have created a bar chart showing quarterback performance during the games they travel the shortest distance and the games they travel the longest. The 0 value on the y-axis is the average quarterback rating (QBR) for the player for the whole season, and each colored bar is the variation from that average in those games. 

![NFL QB Performance in Long vs Short Travel](https://github.com/user-attachments/assets/a8f17774-b2f6-4d5d-97de-2f948243198e)

We can see just over half (18/30) quarterbacks had a higher qbr than their yearly average in their shortest travel game. Another major thing to note is that when quarterbacks underperform in relation to their average qbr, they REALLY underperform regardless of the distance. 
Another way we can visualize player performance is via a scatterplot, which I have attached below. 


![NFL QBR change vs Travel Distance](https://github.com/user-attachments/assets/9c0fc363-124e-4623-8709-9b1b3b3f6504)

Again, there is a lot of variation both above and below the average qbr line and no real conclusion to be found from either of these plots. ESPNs quarterback rating (QBR) stat I used is an inclusive stat that includes many other factors other than just the quarteback himself. It accounts for game situation and clutch plays, as well as the strenght of the opponent. QBR may not be the best indicator of true performance for this exact analysis, but it is the most all encompassing stat for the position the public has access to. There are still so many intangible factors that can effect performance on the field that there could be no analysis that accurately defines player performance. So from this analysis one can not definitively say that travel distance has any effects on player performance. 


