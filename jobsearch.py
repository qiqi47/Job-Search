import webbrowser


def search_on_job_sites(keywords):
    job_sites = {
        # in Indeed ，fromage=1 represents jobs published in last one day
        "Indeed": "https://www.indeed.com/jobs?q={}&fromage=1",
        # in LinkedIn中，r86400 represents jobs published in last one day
        "LinkedIn": "https://www.linkedin.com/jobs/search/?keywords={}&f_TPR=r86400",
        # in Glassdoor ，fromAge=1d represents jobs published in last one day
        "Glassdoor": "https://www.glassdoor.com/Job/jobs.htm?sc.keyword={}&fromAge=1d"
    }

    for keyword in keywords:
        for site, url in job_sites.items():
            search_url = url.format(keyword)
            webbrowser.open(search_url)


if __name__ == "__main__":
    # edit keywords here
    keywords = ["ux 2024", "product designer 2024",
                "ux engineer 2024", "front-end engineer 2024"]
    search_on_job_sites(keywords)

##############################################################################################################
# to run the code, press control+ ` to open a terminal, and input python jobsearch.py or python3 jobsearch.py
##############################################################################################################
