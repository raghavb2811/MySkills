import streamlit as st
import datetime
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.title("Enter the Skills Learnt over the course of your Career")

# 1. Ask for the number of entries
n = st.number_input("How many entries do you want to add?", min_value=1, max_value=20, value=2, step=1)

# 2. Create the form
with st.form("dynamic_form"):
    st.write(f"Enter details for {n} Skills:")
    
    # Store inputs in a list to process later
    entries = []
    
    for i in range(n):
        st.subheader(f"Skill {i+1}")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Using unique keys based on index 'i'
            name = st.text_input("Skill/Technology", key=f"name_{i}")
        with col2:
            dob = st.date_input("Started Using ", key=f"dob_{i}", 
                                min_value=datetime.date(1900, 1, 1),
                                max_value=datetime.date.today())
        with col3:
            dobl = st.date_input("Last Used ", key=f"dobl_{i}", 
                                min_value=datetime.date(1900, 1, 1),
                                max_value=datetime.date.today())       
        entries.append({"Skill/Technology": name, "From": dob, "Till": dobl})
        
    # 3. Submit button
    submit = st.form_submit_button("Submit Data")

# 4. Process data after submission
if submit:
    st.success("Data submitted!")
    # Convert to DataFrame for better display
    df = pd.DataFrame(entries)
    df['Start'] = pd.to_datetime(df['From'])
    df['End'] = pd.to_datetime(df['Till'])
    df['Years Of Experience'] = df['Till'] - df['From']
    pd_df = df.sort_values(['Years Of Experience'],ascending=False).reset_index(drop=True)
    # st.dataframe(pd_df)
    st.dataframe(df, column_order=("Skill/Technology", "Years Of Experience"))      
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5))

    # Use Matplotlib's barh for ranges (left=start, width=duration)
    ax.barh(pd_df['Skill/Technology'], pd_df['Years Of Experience'], left=pd_df['Start'], color=sns.color_palette("viridis", len(pd_df)))

    # 3. Formatting
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    plt.xlabel("Year")
    plt.ylabel("Skill")
    plt.title("My Learning Curve/Experience")
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

    

   



    # Optional: Display as raw data
    # st.write(entries)
