# CS496-A3
This is a visualization application for exploring a dataset about video games. The main feature is two scatter plots with metrics of success mapped to the y-axes. The plot on the left has sales in millions mapped to the y-axis, while the plot on the right has review score out of 100 mapped to the y-axis. 

# Instructions for Use
To run this visualization application, first make sure all files are in the same directory. Then, navigate to this directory and open a web server. We used python for this, by navigating to the directory in the terminal and running the command "python3 -m http.server". 
Once the web server is activated, open Assignment3Code.html to start the application.

Use the buttons on the bottom bar to set the variable mapped to the x-axis. Use the drop-down menus in the sidebar to filter the data. Hovering over a point displays the title of the game it represents as well as values for the x and y variables. Points can be linked by clicking on them. This highlights them and they will stay highlighted until the reset button on the sidebar is clicked. 