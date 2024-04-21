# Clarity - Accelerating the medical checkup process

## Tech Stack 
Google Gemini, Reflex, Python, Flask, Google Cloud, Figma

## Inspiration

In the past, one of our group members have suffered injuries of varying severities. He was immediately faced with a pressing dilemma-seek a primary care physician, the ER, or just wait it out? The problem with this situation is that it runs the risk of a wrong choice possibly leading to either wasted time or an increased severity of an untreated ailment. 

On top of this, we realized the issue of wasted time is a larger issue in the healthcare field than we initially thought-nearly every primary care physician consultation takes countless extra minutes to ask the patient basic questions, leading to long wait times and overcrowded facilities.

## What it does

Clarity solves these issues by accelerating the medical checkup process, allowing patients to receive consultation within minutes. In turn, medical facility wait times decrease and doctors are able to speak to more patients in the same timeframe.

It works by providing users with a set of questions specifically catered towards their situation. Our program may also prompt users for an image or video of their ailment. All of this information will be sent in a neatly formatted file to their local primary care physician who can then provide the patient with immediate guidance. Patients will then either no longer need to travel to their doctor, make a more informed decision to go to their doctor, or be advised to go immediately to the ER.

In turn, patients save travel time and come to the doctor with their information already provided, leading to more efficient doctor visits. This enables doctors to consult with more patients during their work day. 

## How we built it

We used a combination of elements to build our product. Before building out our product, we mapped out the visuals and user experience through Figma. We then used Reflex's framework to construct our pages complete with a webcam and text responses. Gemini AI's LLM was then used in two unique ways in our product. Firstly, through training our model with Google Cloud, we were able to create a unique user experience by providing users with diagnostic questions specific to their situation. Secondly, we used the LLM to fill in the gaps in our speech-to-text functionality (eg "my leg in pain" --> "my leg [is] in pain").
