''' # to run this open terminal and type 
# streamlit run ui/demo1.py '''

# to run the below text use 'CTRL' + 'J'
# st. used to display at screen

import streamlit as st

st.title("Streamlit Demo")
st.header("Stream lit is awesome")
st.subheader('Its easy to use')
st.text("this is a simple test example")
st.write("This is a magical function")
st.markdown("This is a example of **markdown **")
st.success("this is a success message")
st.info("this is a info message")
st.warning("this is a waring message")
st.error("this is a error message")
st.exception("this is exception message")   #textual feature/elements all 

#media elements 

st.image(r"https://www.google.com/search?q=image+sample&sxsrf=ALiCzsaTlpaebzOTQ1E1UV0NIdqknyh45Q:1659103010023&tbm=isch&source=iu&ictx=1&vet=1&fir=NZ6unGWQe6yEPM%252CQCmqd078keo0SM%252C_%253Ba8pl6_8r1SwlJM%252C3ybpJYt8RDb4SM%252C_%253Bpkl4o0uOisserM%252CAie65lC8ZA-NcM%252C_%253BzsxWnq3vNVEB7M%252CCvgrVEnJX5o2_M%252C_%253BctwlIOP3tOQB7M%252CZszwutWw5USngM%252C_%253B_kSqz5WbqU1pXM%252C__UABpouvi3a8M%252C_%253BZU-ga0p1ddn7iM%252CKe1g04_Q-Hc_mM%252C_%253BlDILizkoMTqWqM%252Cxi8p_gUTxRIu0M%252C_%253BSygWekdULxI0FM%252CmFAc4MhHhMHJNM%252C_%253BFL3ragUd_EIHiM%252CZszwutWw5USngM%252C_%253BsYL9vtB8CQ6UTM%252CqhmIZtFj6T8bIM%252C_%253BiBj3_ZxgJa_HKM%252CmHT4vpZrOW_OzM%252C_%253B26v4UQtNAvkrTM%252CgRwCQNJ-T04fbM%252C_%253BXT4BQcGwT2fTqM%252C3ybpJYt8RDb4SM%252C_&usg=AI4_-kQmh1AbmxOSsrQp4usEa9YcdfuKBw&sa=X&ved=2ahUKEwixibusoJ75AhXA0HMBHZ9fDjYQ9QF6BAgGEAE")
st.video("https://www.youtube.com/watch?v=NW8Aa9AfpR0")
st.image(r"C:\Users\Somya Shrivastava\Downloads\votercard_front2.jpg")

#widgets
name=st.text_input("Enter the username")
cost=st.number_input("Your gross salary")
comment=st.text_area("Enter remark")
status=st.checkbox("save this area")
gender=st.radio("Gender",["Male","Female","others"])
querylist=('how to use streamlit?',
            'is it free or paid',
            'is it gonna rain now?')
query=st.selectbox("what is your query",querylist)
rating=st.slider("Select your raiting ",1,5)
btn=st.button("Submit the response")
# if button is pressed
if btn:
    st.write("username",name)
    st.write("Salary",cost)
    st.write("Comment",comment)
    st.write("Status",status)
    st.write("Gender",gender)
    st.write("query:",query)
    st.write("Rating",rating)
