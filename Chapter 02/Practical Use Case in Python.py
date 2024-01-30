import pandas as pd
import rpa as r
input_df = pd.read_excel(r"C:\Training.xlsx")
for i in range(len(input_df)):
    first_name = input_df.loc[i, "First Name"]
    last_name = input_df.loc[i, "Last Name"]
    email = input_df.loc[i, "Email"]
    course =input_df.loc[i, "Course"]
    month =input_df.loc[i, "Enrollment Month"]
    r.init()
    r.url('https://codenboxautomationlab.com/registration-form/')
    r.type('//*[@name="fname"]', first_name)
    r.type('//*[@name="lname"]', last_name)
    r.type('//*[@name="email"]', email)
    r.select('//*[@name="nf-field-22"]', course)
    r.select('//*[@name="nf-field-24"]', month)
    r.click('//*[@id="nf-field-23-6"]')
    r.click('//*[@id="nf-field-15"]')
    r.wait(10) # ensure results are fully loaded
    r.close()
