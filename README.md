# Vision Checker - A Medhacks2020 Project

## Inspiration
Given the current circumstances surrounding COVID-19, we were inspired to provide people with the quality of care that they had become accustomed to before the pandemic.

## What it does
Our website has an eye chart embedded into it to test patients on their eyesight. Patients can take the exam as many times as they would like and their scores will be calculated through interpreting audio with Google's Speech-to-Text API. This allows patients to keep track of their eye health at home, allowing people to be more involved in their own healthcare and facilitating greater communication between doctors and their patients.

## How we built it
For the front-end of our website, we used HTML5, CSS, and JavaScript to create a simple, yet thorough website with instructions on how to use it to perform the eye exam. We used Python to interface with the Google Cloud API and storage system. Flask was used to connect our front-end with our back-end functions. In addition, we utilized Google's Speech-to-Text API to detect audio from the user and compare that with the actual letters on the eye chart provided on the website. A scoring function based on Snellen's All About Vision was used to provide an accurate score for users.

## Challenges we ran into
A challenge we faced was our limited knowledge of Flask and Google Cloud, both of which we learned as we went along. Also, one of the aspects of our project involved alerting the user about when to move on to the next letter. This was quite challenging to implement because of synchronizing it with the audio recording. 

## Accomplishments that we're proud of
We are proud of both our back-end and front-end. We were glad to have learned a lot in the process!

## What we learned
Through our project, we learned how to use Google Cloud and understand the various functionalities that are available to us. We learned how to use Flask and how to work towards creating middleware.

## What's next for Vision Checker
A future development we were considering is to include randomized charts, rather than one standard eye chart, to ensure that patients do not simply memorize it. These charts may also potentially include charts in other languages to cater towards those of different ethnical and cultural backgrounds. Lastly, we hope to implement user authentication so that patients may be able to track and monitor the change in their eyesight over time.
