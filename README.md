# Pythonic Monopoly

![San Francisco Park Reading](Images/san-francisco-park-reading.jpg)


## Background

Harold's company has just started a new Real Estate Investment division to provide customers with a broader range of portfolio options. Harold was tasked with building a prototype dashboard and he needs your help. The real estate team wants to trial this initial offering with investment opportunities for the San Francisco market. If the new service is popular, then they can start to expand to other markets.

The goal of this dashboard is to provide charts, maps, and interactive visualizations that help customers explore the data and determine if they want to invest in rental properties in San Francisco.

In this homework assignment, you will help Harold accomplish the following tasks:

1. [Complete a notebook of rental analysis](#Rental-Analysis).

2. [Create a dashboard of interactive visualizations to explore the market data](#Dashboard).

---


### Rental Analysis


#### Housing Units Per Year

Default Bar Chart

  ![unscaled-bar.png](Images/unscaled-bar.png)

Bar Chart with y-axis limits adjusted

  ![scaled-bar.png](Images/scaled-bar.png)


#### Average Housing Costs in San Francisco Per Year

Vsualize the average (mean) gross rent and average price per square foot per year and visualize it as a bar chart.

The mean `gross_rent` and `sale_price_sqr_foot` for each year.
Visualize the mean `gross_rent` and `sale_price_sqr_foot` for each year as two line charts.

  ![gross-rent.png](Images/gross-rent.png)

  ![average-sales.png](Images/average-sales.png)

#### Average Prices By Neighborhood

The first visualization is a line plot showing the trend of average price per square foot over time for each neighborhood.  
The second is a line plot showing the trend of average montly rent over time for each neighborhood.

  ![avg-price-neighborhood.png](Images/avg-price-neighborhood.png)
  
  ![gross-rent-neighborhood.png](Images/gross-rent-neighborhood.png)


#### Top 10 Most Expensive Neighborhoods

The figure shows which neighborhoods are the most expensive. 

  ![top-10-expensive-neighborhoods.png](Images/top-10-expensive-neighborhoods.png)


#### Comparing Cost to Purchase Versus Rental Income

Interactive visualization with a dropdown selector for the neighborhood. This visualization feature a side-by-side comparison of average price per square foot versus average monthly rent by year.

![rent-versus-price](Images/rent-versus-price.png)

#### Neighborhood Map

Use a scatter mapbox object from plotly express.


  ![neighborhood-map.png](Images/neighborhood-map.png)

####  Cost Analysis - Optional Challenge

Using the provided DataFrame to create the following visualizations:

Parallel Coordinates Plot.

  ![parallel-coordinates.png](Images/parallel-coordinates.png)

Parallel Categories Plot.

  ![parallel-categories.png](Images/parallel-categories.png)

Sunburst plot to show the most expensive neighborhoods in San Francisco per year.

   ![sunburst](Images/sunburst.png)
 
---

### Dashboard

Sample Dashboard:

  ![dashboard-demo.png](Images/dashboard-demo.png)

---

