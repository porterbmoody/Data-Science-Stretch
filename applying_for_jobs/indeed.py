#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd



service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

query = 'data&l=colorado%20springs'
# url = f'https://www.indeed.com/jobs?q={query}'
url = 'https://secure.indeed.com/account/login?hl=en_US&amp;co=US&amp;continue=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Ddata%26l%3Dcolorado%2520springs&amp;tmpl=desktop&amp;service=mob&amp;from=gnav-util-jobsearch--indeedmobile&amp;jsContinue=https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Ddata%26l%3Dcolorado%2520springs&amp;empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&amp;'
driver.get(url)

#%%

# driver.find_element(By.CLASS_NAME, "gnav-header-1bxrjpb e71d0lh0")
element_email_input = driver.find_element(By.ID, 'ifl-InputFormField-3')

#%%
element_email_input.send_keys('porterbmoody@gmail.com')

#%%
button_continue_class = 'dd-privacy-allow css-jorj5j e8ju0x51'
element_buttons = driver.find_elements(By.CLASS_NAME, 'dd-privacy-allow')

for element in element_buttons:
    if "Continue" in element.text:
        element.click()
        break 

# data_dict = {
#     'element':element_buttons,
#     'element_text':[element_button.text for element_button in element_buttons],
# }
# data = pd.DataFrame(data_dict)
# data
# element_button.click()

#%%
driver.quit()

#%%

# Get the HTML source of the page
html_source = driver.page_source

# Specify the file path where you want to save the HTML source
file_path = "page_source.html"  # Change this to the desired file path

# Write the HTML source to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_source)

# Close the file
file.close()

# Optionally, you can print a confirmation message
print(f"Page source saved to {file_path}")




#%%

# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
# title = 'jcs-JobTitle css-jspxzf eu4oa1w0'

# jobs = soup.find_all("a", class_ = title)
# job_titles = [job.get_text().strip() for job in jobs]
# job_titles


# data = pd.DataFrame({
#     'title':job_titles
# })
# data


#%%


pd.set_option('display.max_colwidth', 75)


class WebBot:

    classes = {
        'listing':'slider_item css-kyg8or eu4oa1w0',
        'title' : 'jcs-JobTitle css-jspxzf eu4oa1w0',
        'name':'companyName',
        'location':'companyLocation',
        'salary':'metadata salary-snippet-container',
        'snippet':'job-snippet',
    }

    def __init__(self, url):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(url)

    def login(self):
        element = self.driver.find_element(By.CLASS_NAME, 'gnav-header-1bxrjpb')
        element.click()

    @staticmethod
    def extract_element(html_string, html_type, html_class):
        # soup = BeautifulSoup(html_string, 'html.parser')
        element = html_string.find(html_type, class_=html_class)
        if element:
            return element.get_text().strip()
        return None

    def extract_data(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        listings = soup.find_all("div", class_ = self.classes['listing'])

        data_dict = {
            'listing_html' : listings,
        }

        df = pd.DataFrame(data_dict)
        df['title'] = df['listing_html'].apply(self.extract_element, args=("a", self.classes['title']))
        df['name'] = df['listing_html'].apply(self.extract_element, args=("span", self.classes['name']))
        df['location'] = df['listing_html'].apply(self.extract_element, args=("div", self.classes['location']))
        df['salary'] = df['listing_html'].apply(self.extract_element, args=("div", self.classes['salary']))
        df['snippet'] = df['listing_html'].apply(self.extract_element, args=("div", self.classes['snippet']))

        return df

    def click(self):
        element = self.driver.find_element(By.ID, "link")

        element.click()

    def close(self):
        self.driver.quit()
        self.driver.close()

#%%

web_bot = WebBot(url)


#%%
web_bot.driver.find_element('link text', "Sign In")

# web_bot.extract_data()

# web_bot.click()

#%%

web_bot.close()

#%%

import sendgrid
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import os


sg = sendgrid.SendGridAPIClient(api_key=api_key)

email_template_file = 'page_source.html'
with open(email_template_file, 'r') as file:
    html_content = file.read()

html_content

message = Mail(
    from_email="portermoodymusic@gmail.com",
    to_emails="porterbmoody@gmail.com",
    subject="Hello",
    html_content=html_content
)

# attachment = Attachment()
# attachment.file_content = FileContent(open('hello.html', 'rb').read())
# attachment.file_name = FileName('hello.html')
# attachment.file_type = FileType('text/html')
# attachment.disposition = Disposition('attachment')
# message.add_attachment(attachment)

response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)


