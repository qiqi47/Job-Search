# Job-Search
### Run the code:
to run the code, press control+ "`" to open a terminal, and input `python jobsearch.py` or `python3 jobsearch.py`
### Change the period:
in Indeed ，`fromage=1` represents jobs published in last one day  
        `"Indeed": "https://www.indeed.com/jobs?q={}&fromage=1"`,
        
in LinkedIn，`r86400` ( means 86400 seconds ) represents jobs published in last one day  
        `"LinkedIn": "https://www.linkedin.com/jobs/search/?keywords={}&f_TPR=r86400"`,
        
in Glassdoor ，`fromAge=1d` represents jobs published in last one day  
        `"Glassdoor": "https://www.glassdoor.com/Job/jobs.htm?sc.keyword={}&fromAge=1d"`

### Change the keywords:
Change the content inside the keywords array.  
`keywords = ["back-end engineers 2024","Devops intern","software engineer intern"]`  

`keywords = ["ux 2024", "product designer 2024", "ux engineer 2024", "front-end engineer 2024"]`
    
