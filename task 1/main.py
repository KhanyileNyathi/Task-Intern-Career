from bs4 import BeautifulSoup
import requests as r
import time

print('Enter a skills that you want filtered out below')
Unwanted_skill = input("Enter : ")  # accept input
print(f'filtering out {Unwanted_skill}.....')


def find_a_job():
    # request data
    url = r.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=')
    soup = BeautifulSoup(url.text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        date = job.find('span', class_="sim-posted").span.text  # clean

        if 'few' in date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('', '')
            skill_sets = job.find('span', class_='srp-skills').text.replace('', '')  # process and clean the data
            for_more_info = job.header.h2.a['href']

            if Unwanted_skill not in skill_sets:  # filter unwanted skill
                with open('results/(index).txt', 'w') as f:  # save file
                    f.write(f'Date: {date}\n')
                    f.write(f'Company name: {company_name.strip()}\n')
                    f.write(f'Skills: {skill_sets.strip()} \n ')  # organise the data
                    f.write(f'For more info visit: {for_more_info}')
                print(f'file saved : {index}')


# if__name__=='__main__':
# automate, make the code run again after 10mins
while True:
    find_a_job()
    time_wait = 10
    print(f'waiting {time_wait} minutes')
    time.sleep(time_wait * 30)
