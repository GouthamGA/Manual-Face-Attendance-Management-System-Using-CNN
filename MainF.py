import streamlit as st
import csv
import os
import pandas as pd

st.title("Face Attendence Using CNN")

typee = st.selectbox( 'CHOOSE HERE ',('HOME','ADMIN', 'STUDENT','LECTURER'))

if typee=="HOME":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Home Page !!! "}</h1>', unsafe_allow_html=True)
    

if typee=="ADMIN":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Admin Page !!! "}</h1>', unsafe_allow_html=True)
    
    reg=st.button('View Register Details')
    
    st.success("Wlecome Admin!!!")
    
    
    adname=st.text_input("Enter Name","Name")
    passs=st.text_input("Enter Password","Password",type="password")
    aa=st.button("Submit")
    
    # if aa:
        
    if adname=="Admin" and passs=="12345":
        st.success("Admin Login Successfully !!!")

        st.text("Show")
        fields=['UserName']
        
        # st.write('Great!')
        import os
        import pandas as pd
        import csv
        all_files = os.listdir('All Data/')
        df1 = []
        df2 = []
        for ii in range(0,len(all_files)):
            file_name = all_files[ii]
            df = pd.read_csv('All Data/'+file_name)
            df1.append(df)
            df2.append([df['User'][0]])

        # with open(list(Req_data_c)[0]+'.csv', 'w', newline='') as csvfile: 
        with open('Full Record'+'.csv', 'w', newline='') as csvfile: 
         
            
        # creating a csv writer object 
            csvwriter2 = csv.writer(csvfile) 
            
            # writing the fields 
            csvwriter2.writerow(fields) 
                
            # writing the data rows 
            csvwriter2.writerows(df2)
        
        st.table(df2)        
        

        
    addatten=st.button('Add Attendence')
    
    st.text('Kindly add attandence for 5 periods') 
    stude_name=st.text_input('Enter Student Name')
    per_1 = st.radio( 'Choose Period1 ',('P', 'A', 'O'))
    per_2 = st.radio( 'Choose Period2 ',('P', 'A', 'O'))        
    per_3 = st.radio( 'Choose Period3 ',('P', 'A', 'O'))        
    per_4 = st.radio( 'Choose Period4 ',('P', 'A', 'O'))        
    per_5 = st.radio( 'Choose Period5 ',('P', 'A', 'O'))
    
    recc=[per_1+per_2+per_3+per_4+per_5]
    fieldss=['Period1','Period2','Period3','Period4','Period5']
    
    with open('All Atten/'+stude_name+'.csv', 'w', newline='') as csvfile: 
     
        
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fieldss) 
            
        # writing the data rows 
        csvwriter.writerows(recc)
        
    
    st.success("Attendence Added Succesfully!!!")

        
if typee=="STUDENT":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Student Page !!! "}</h1>', unsafe_allow_html=True)


    st.success("Welcome User!!!")    
    

    import pandas as pd
    
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    
    col1, col2 = st.columns(2)
    
    
        
    with col2:
    
        UR1 = st.text_input("Login User Name",key="username")
        psslog = st.text_input("Password",key="password",type="password")
        agree = st.checkbox('LOGIN')
        
        if agree:
            import pandas as pd
            try:
                
                df = pd.read_csv(UR1+'.csv')
                U_P1 = df['User'][0]
                
                import pickle
                with open('name.pickle', 'wb') as f:
                    pickle.dump(U_P1, f)
                    
                    
                U_P2 = df['Password'][0]
                if str(UR1) == str(U_P1) and str(psslog) == str(U_P2):
                    st.write('Successfully Login !!!')
                    
                    import pandas as pd
                    
                    def hyperlink(url):
                        return f'<a target="_blank" href="{url}">{url}</a>'
                    
                    dff = pd.DataFrame(columns=['page'])
                    dff['page'] = ['main']
                    dff['page'] = dff['page'].apply(hyperlink)
                    dff = dff.to_html(escape=False)
    
                    st.write(dff, unsafe_allow_html=True)                   
                else:
                    st.write('Login Failed!!!')
            except:
                st.write('Login Failed!!!')
                
                
          
    with col1:
        UR = st.text_input("Register User Name",key="username1")
        pss1 = st.text_input("First Password",key="password1",type="password")
        pss2 = st.text_input("Confirm Password",key="password2",type="password")
        
        
        
        if pss1 == pss2 and len(str(pss1)) > 2:
            import pandas as pd
            
    
                
            import csv 
            
            # field names 
            fields = ['User', 'Password'] 
            
            # data rows of csv file
            # a1 = df['User']
            # a2 = df['Password']
            # new_row = [a1,a2]
            old_row = [[UR,pss1]]
            # new_row.append(old_row)
            # name of csv file 
            
            # writing to csv file 
            with open(UR+'.csv', 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(fields) 
                    
                # writing the data rows 
                csvwriter.writerows(old_row)
                
                
            with open('All Data/'+UR+'.csv', 'w', newline='') as csvfile: 
         
            
        # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
            
            # writing the fields 
                csvwriter.writerow(fields) 
                
            # writing the data rows 
                csvwriter.writerows(old_row)
                
            
            st.write('Successfully Registered !!!')
        else:
            
            st.write('Registeration Failed !!!')

if typee=="LECTURER":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Lecturer Page !!! "}</h1>', unsafe_allow_html=True)
        
    st.success("Wlecome Lecturer!!!")
    
    
    adname=st.text_input("Enter Name","Name")
    passs=st.text_input("Enter Password","Password",type="password")
    aa=st.button("Submit")
    
    # if aa:
        
    if adname=="Lecturer" and passs=="12345":
        st.success("Lecturer Login Successfully !!!")
        
        
        stuname=st.text_input("Enter Student Name")
        
        import pandas as pd
        dff=pd.read_csv('All Atten/'+stuname+'.csv')
        
        st.text("---> Check the Details <---")
        
        per1=st.text_input("Check Period1",dff['Period1'][0])
        
        per2=st.text_input("Check Period2",dff['Period2'][0])
        
        per3=st.text_input("Check Period3",dff['Period3'][0])
     
        per4=st.text_input("Check Period4",dff['Period4'][0])
        
        per5=st.text_input("Check Period5",dff['Period5'][0])
        
        
        
        recc=[per1+per2+per3+per4+per5]
        fieldss=['Period1','Period2','Period3','Period4','Period5']
    
        with open('All Atten/'+stuname+'.csv', 'w', newline='') as csvfile: 
     
        
    # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
            csvwriter.writerow(fieldss) 
                
        # writing the data rows 
            csvwriter.writerows(recc)
        
    
        st.success("Checked and updated Succesfully!!!")     
        
    qq=st.button("View Monthy Report")
    
    all_files = os.listdir('All Atten/')
    df1 = []
    df2 = []
    for ii in range(0,len(all_files)):
        file_name = all_files[ii]
        df = pd.read_csv('All Atten/'+file_name)
        
        fulldata=pd.read_csv('Full Record.csv')
        
        df1.append(df)
        
        from datetime import datetime
        now = datetime.now()
    
        dtString = now.strftime("%m/%d/%Y,%H:%M:%S")
        # st.write('Attendence Date',dtString)        
        
        
        
        
        
        df22=[fulldata['UserName'][ii],df['Period1'][0],df['Period2'][0],df['Period3'][0],df['Period4'][0],df['Period5'][0],dtString]
        filed_mon=['Name','Period1','Period2','Period3','Period4','Period5','Date and Time']
        # df2.append([df['User'][0]])
        df2.append(df22)
        # with open(list(Req_data_c)[0]+'.csv', 'w', newline='') as csvfile: 
        with open('Monthly'+'.csv', 'w', newline='') as csvfile: 
         
            
        # creating a csv writer object 
            csvwriter2 = csv.writer(csvfile) 
            
            # writing the fields 
            csvwriter2.writerow(filed_mon) 
                
            # writing the data rows 
            csvwriter2.writerows(df2)
    view=pd.read_csv('Monthly.csv')
    st.table(view)
        # st.table(df2)        
        
      
      
        
        
        
        
        # st.success("Checked")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        