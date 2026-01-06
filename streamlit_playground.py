import streamlit as st
import datetime


st.markdown("# Markdown display")
st.markdown("## Markdown display")
st.markdown("### Markdown display")

st.header("This is main header")
st.subheader("This is subheader")
st.text("This is a text")
st.caption("This is a caption")

# Display code
code_snippet = """
def greet(name):
    return f"Hello, {name}!"
"""
st.code(code_snippet)
# Display latex
# Latex Input: Render mathematical expressions
st.latex(r"""
a^2 + b^2 = c^2
""")
st.latex(r"""y = m*X + c""")

my_list = [1, 3, 5]
st.write(my_list)

car_manufacturer = ['Ford', 'Lexus', 'Toyota', 'VW', 'Audi']
selected_car = st.selectbox(label='Car manufacturer',
                            options=car_manufacturer,
                            key='ui',
                            index=3,
                            help='Select car brand',
                            placeholder='Select your car of choice',
                            label_visibility='visible')

my_favs = st.multiselect(label='Select favorites',
                         options=car_manufacturer,
                         max_selections=3, 
                         label_visibility='visible')

# Basic slider
basic_slider = st.slider(label='Basic label',
                         min_value=1,
                         max_value=100,
                         value=50)
st.write("Selected number: {}".format(basic_slider))

# Range slider
range_slider = st.slider(label='Range label',
                         min_value=1,
                         max_value=100,
                         value=(50, 85))
st.write("Selected number: {}".format(basic_slider))

float_slider = st.slider(min_value=1.0,
                         max_value=5.0,
                         value=2.5,
                         label='float slider',
                         step=0.1)

# Date slider
date_slider = st.slider(label='Select a date',
                         min_value=datetime.date(2023, 1, 1),
                         max_value=datetime.date(2026, 1, 6),
                         value=datetime.date(2025, 1, 6),
                         format="MM/DD/YYYY")
st.write("Selected date: {}".format(date_slider))

# Number input
number_input = st.number_input(
    label="Enter a number",
    min_value=0,
    max_value=100,
    value=50,
    step=5,
    help="Use this widget to input a number.",
    label_visibility="visible"
)
st.write("Number input {}".format(number_input))

sidebar_number_input = st.sidebar.number_input(label="Enter a number",
                                               min_value=0,
                                               max_value=25,
                                               value=5,
                                               step=1)


# Add forms in streamlit
form = st.form(key="form1",
                clear_on_submit=False,
                enter_to_submit=True,
                border=True
                )

state_of_origin = form.selectbox(label='Current State',
               options=['TX', 'NM', 'KL'])
submit = form.form_submit_button(label='Submit details')

if submit:
    print("Submit button value: ", submit)
    print("State of Origin: ", state_of_origin)


second_form = st.sidebar.form(key='sidebar_form', )
value_entered = second_form.number_input(label='Age',
                                         min_value=1,
                                         max_value=99,
                                         )
submit_second_form = second_form.form_submit_button(label="Submit")
if submit_second_form:
    print("Submitted: ", submit_second_form)


tab1, tab2, tab3 = st.tabs(['Home', 'Sales', 'Reviews'])

with tab1:
    st.header("Welcome to HOME!")

with tab2:
    st.header("Welcome to SALES!")

with tab3:
    st.header("Welcome to REVIEWS!")


col1, col2, col3 = st.columns(3, gap='medium', vertical_alignment='top') # instead of 3, you can have [1,3,6] <- relative sizes

with col1:
    st.header('Column 1')

with col2:
    st.header('Column 2')

with col3:
    st.header('Column 3')
    # st.image('image.png')
