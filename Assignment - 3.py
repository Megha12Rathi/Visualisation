#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


d1 = pd.read_csv('HRDataset_v14.csv')


# In[3]:


d2 = pd.read_csv('Airbnb Dataset 19.csv')


# In[4]:


d1.head()


# In[5]:


d2.head()


# In[6]:


d1.shape


# In[7]:


d2.shape


# In[8]:


d1.dtypes


# In[9]:


d2.dtypes


# In[10]:


d1.describe()


# In[11]:


d2.describe()


# In[12]:


categorical = d1.dtypes[d1.dtypes=='object'].index
print(categorical)

d1[categorical].describe()


# In[13]:


categorical = d2.dtypes[d2.dtypes=='object'].index
print(categorical)

d2[categorical].describe()


# In[14]:


# filling a null values using fillna() 

d1["ManagerID"].fillna(35, inplace = True)


# In[15]:


d1["ManagerID"].isnull().sum()


# In[16]:


d1.drop(columns = ['MaritalStatusID','MarriedID','Zip'],inplace = True)


# In[17]:


d2["reviews_per_month"].fillna(d2["reviews_per_month"].mean(),inplace=True)    # filling null values with mean


# In[18]:


d2["reviews_per_month"].isnull().sum()


# In[19]:


import datetime


# In[20]:


#. This will fill all the missing values in the date_column with the next available date in the column.

d2['last_review'].fillna(method='bfill', inplace=True) 


# In[21]:


d2['last_review'].isnull().sum()


# In[22]:


d2.drop(columns = ['host_name','latitude','longitude'],inplace = True)


# In[23]:


d1.head()


# In[24]:


d2.head()


# In[25]:


d1.to_csv('HRDataset.csv')


# In[26]:


d2.to_csv('Airbnb Dataset.csv')


# In[27]:


d1.to_excel('HRDataset.xlsx', index=False)


# In[28]:


d2.to_excel('Airbnb Dataset.xlsx', index=False)


# #### Visualisation - 1
# 

# In[29]:


# . Use the Pandas groupby() method to group the data by marital_status and count the number of employees in each group.
status_count = d1.groupby('MaritalDesc')['EmpID'].count()

# . Create a bar chart using Matplotlib to visualize the counts of employees in each marital status group.
plt.bar(status_count.index, status_count.values)
plt.title('Marital Status by Employee ID')
plt.xlabel('Marital Status')
plt.ylabel('Number of Employees')

#. Display the chart using the show() function.
plt.show()

#. This will create a bar chart that displays the number of employees in each marital status group. The x-axis will show the different marital statuses and the y-axis will show the corresponding counts. The title of the graph will be "Marital Status by Employee ID".


# #### Visualisation - 2

# In[30]:


status_count = d1.groupby('Department')['EmpID'].count()

#. Use the px.box() function in Plotly Express to create a box plot. Set the x parameter to the department column and the y parameter to the num_employees column.
fig = px.box(d1, x='Department', y='EmpID')

#. The boxmode parameter is used to set the mode of the box plot to "group", which groups the boxes by department. The boxgap parameter is used to adjust the width of the boxes and the boxgroupgap parameter is used to adjust the space between the boxes.
fig.update_layout(title='Number of Employees by Department',
                   xaxis_title='Department',
                   yaxis_title='Number of Employees',
                   boxmode='group', boxgap=0.2, boxgroupgap=0.1)

#. This will create a box plot that displays the number of employees in each department. The x-axis will show the different departments and the y-axis will show the corresponding counts. The title of the graph will be "Number of Employees by Department".


# ##### Visualisation - 3

# In[31]:


import plotly.express as px

#. Use the px.histogram() function in Plotly Express to create a histogram plot. Set the x parameter to the id column and the y parameter to the count. 
fig = px.histogram(d2,x='id',color='room_type',nbins = 50)
fig.update_layout(
    title = 'Histogram of id per room_type',
    xaxis_title='id',
    yaxis_title='Count',)

#. Display the chart using the show() function.
fig.show()

#. This code will produce a histogram of room_type levels with the x-axis labeled "id", the y-axis labeled "Count", and a title of "Histogram of id per room_type". The histogram will be divided into 50 bins based on the range of employee satisfaction levels, and will display the count of employees in each bin.


# #### Visualisation - 4

# In[32]:


#. Use the px.pie() function in Plotly Express to create a pie chart. Set the names parameter to the PerformanceScore column and the values parameter to the EmpID column.
fig = px.pie(d1, names='PerformanceScore', values='EmpID')

#. Display the chart using the show() function.
fig.show()


# #### Visualisation - 5

# In[33]:


import plotly.graph_objects as go

# . Use the value_counts() method in Pandas to count the occurrences of each requirement source for each emp id. Create a new DataFrame with the resulting counts.
counts = d1.groupby('RecruitmentSource')['EmpID'].nunique()

#. Use the go.Pie() function in Plotly to create a pie chart. Set the labels parameter to the different requirement sources and the values parameter to the corresponding counts.
fig = go.Figure()
fig.add_trace(go.Pie(labels=counts.index, values=counts.values, hole=0.5))

#. Customize the chart by adding a title, adjusting the colors, and modifying the font size as desired.The hole parameter is used to create a donut chart with a hole size of 0.5. The colorway parameter is used to set the colors for the different slices.
fig.update_layout(title='Requirement Sources by Emp ID',
                   font=dict(size=12),
                   colorway=px.colors.qualitative.Dark2)

#. Display the chart using the show() function.
fig.show()

#. This will create a donut chart that displays the proportion of each requirement source across all emp ids. The title of the graph will be "Requirement Sources by Emp ID". 


# ##### Visualisation - 6

# In[34]:


#. Use the scatter() function from the plotly.express module to create the scatter plot. Specify the DataFrame as the first argument, and set the x, y, and color parameters to the columns you want to use for the x-axis, y-axis, and color-coding of the points.
fig = px.scatter(d1, x='EmpID', y='Salary', color='ManagerID')

#.Customize the chart by adding a title and modifying the font size and color as desired.
fig.update_layout(title='Salary by Employee ID and Manager ID', title_font_size=16, title_font_color='black')

#. Display the chart using the show() function.
fig.show()

#. This will create a scatter plot that displays the relationship between emp id, manager id, and salary. Each point in the plot represents an employee, and the x-axis shows the emp id while the y-axis shows the salary. The color of each point corresponds to the manager id. 


# ##### Visualisation - 7

# In[35]:


#. Use the groupby() method in Pandas to group the data by room_type and neighbourhood_group, and calculate the mean of price for each group.
grouped_data = d2.groupby(['room_type', 'neighbourhood_group']).mean().reset_index()

#. Create a scatter plot using the scatterplot() function in Seaborn. Set the x parameter to neighbourhood_group, the y parameter to price, and the size parameter to price. Set the hue parameter to room_type
sns.scatterplot(data=grouped_data, x='neighbourhood_group', y='price', size='price', hue='room_type', sizes=(50, 300))

#.Customize the chart by adding a title, axis labels, and modifying the font size and color as desired.

plt.title('Average Price by Room Type and Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Price')
plt.rcParams.update({'font.size': 12, 'text.color': 'black'})

#.Display the chart using the show() function.
plt.show()

#  This will create a bubble chart that displays the average price of each room type for each neighbourhood group. The size of each bubble represents the average price, and the color represents the room type. You can customize the chart further by modifying the color palette, changing the font size or color, or modifying the axes labels as needed.


# #### Visualisation - 8

# In[36]:


fig=px.scatter_matrix(d2,dimensions=['minimum_nights','number_of_reviews','reviews_per_month','calculated_host_listings_count'])
fig.show()


# #### Visualisation - 9

# In[37]:


#. Use the pointplot() function from the seaborn module to create the point plot. Specify the DataFrame as the first argument, and set the x and y parameters to the columns you want to use for the x-axis and y-axis.
sns.pointplot(x='number_of_reviews', y='reviews_per_month', data=d2)

#. Customize the chart by adding a title and modifying the font size and color as desired.
import matplotlib.pyplot as plt
plt.title('Number of Reviews vs Reviews per Month')
plt.xlabel('Number of Reviews')
plt.ylabel('Reviews per Month')

#. Display the chart using the show() function.
plt.show()

#. This will create a point plot that displays the relationship between number of reviews and reviews per month. Each point in the plot represents a data point in the dataset, and the x-axis shows the number of reviews while the y-axis shows the reviews per month.


# #### Visualisation - 10

# In[38]:



#. Use the plot() function from the matplotlib module to create the line chart. Specify the DataFrame , and set the x and y parameters to the columns you want to use for the x-axis and y-axis.
plt.plot('DeptID', 'SpecialProjectsCount', data=d1)

#. Customize the chart by adding a title and modifying the font size and color as desired.
plt.title('Special Project Count by Department ID')
plt.xlabel('Department ID')
plt.ylabel('Special Project Count')

#. Use seaborn to style the chart as desired. For example, you can use the set_style() function to set the style to white, and use the despine() function to remove the top and right spines.
sns.set_style('white')
sns.despine()

#. Display the chart using the show() function.
plt.show()

#. his will create a line chart that displays the relationship between special project count and department ID. Each point in the plot represents a data point in the dataset, and the x-axis shows the department ID while the y-axis shows the special project count.


# In[ ]:





# In[ ]:




