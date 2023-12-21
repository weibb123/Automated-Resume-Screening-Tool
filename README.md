# Automated-Resume-Screening-Tool
![image](https://github.com/weibb123/Automated-Resume-Screening-Tool/assets/84426364/779ea42d-d892-404f-8296-c14f9569d793)

tech stack used: langchain, openai, streamlit, scikit-learn, chromadb, tiktoken, PyPDF2. You can find versions in <b> requirements.txt </b>


## Steps to run this repo
git clone this repo
stream run app.py

## Motivation
As I am doing my own job search, sometimes the job description leaves me confuse or not knowing if I am qualify for the postition. Hence, it leaves me the motivation to imeplment a LLM system to understand 
my qualifiation with my resume. <b>Here is a flowchart of the pipepline. </b>
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0f68b445-c614-4869-9b6e-26712255f069/b2c408c1-cc4e-4515-b6e2-19893d4bf9fa/Untitled.png)

<ul> Description should identify candidates key skills, experience levels, job role suitability </ul>

<ul> What candidate good at, lack experience on </ul>





## Evaluation
Achieved average of 59% similarity between resumes and job descriptions

better metric: How likely recruiters decision match with GPT's prediction.


## Lesson learned
I think make use of GPT4 and this system. One) Recruiters have a better understanding of the candidates quicky(saving time). Canadidates can use it to understand what they lack experience on and tailor their resume.
