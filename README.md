# ❗CSC226 Final Project

## Instructions

❗️Exclamation Marks ❗️indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no ❗️in it!)

**Author(s)**: Puskar Chapagain and Luis Olivas 

**Google Doc Link**: https://docs.google.com/document/d/1wwVxXResdXgnSNOUyVShT_KIM4bZyGQ4qYcmgkZTc7c/edit?usp=sharing
**Repo Link**: https://github.com/Berea-College-CSC-226/p01-final-project-rockero241-puskar

---

## References 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update as you go.

CHATGPT - Helped with organizing our project into 4 different classes
---

## Milestone 1: Setup, Planning, Design

**Title**: `Ai Journal`

**Purpose**: `Building a journal that works like a diary with AI feedback.`

**Source Assignment(s)**: `It's gonna be all orignial, based on functions and classes.`

❗️**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![Don't leave me in your README!](image/crc.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")

❗️**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments: 

```
    Branch 1 name: PuskarC
    Branch 2 name: Rockero241
    Branch 3 name: New3
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    ** Initially, it's been a challenge to break down this program into smaller tasks, knowing how to divide and conquer, and where to get started. We feel a little behind, but we're getting on it.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `70%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    ** We're very confident we'll finish the project in time because we've already done most of the legwork for the AI API, all there is left is to get it working and make the GUI.**
```

---

## Milestone 4: Final Code, Presentation, Demo

### ❗User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 
    ** Basically, once the user hits the Run button, the program asks the user some questions to reflect on their mood
and their day as a Journal Entry. Once the user gives all the information, the program then asks the user if they want 
AI feedback on their reflection. If the user inputs 'NO' the program ends there but if the user inputs 'Yes' the program 
provides AI feedback based on the user's input. **

** After hitting run, the program will run immideately  **

### ❗Errors and Constraints
Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

** 
Errors and Constraints

Input Validation:
Invalid inputs like "maybe" instead of "yes/no" for AI feedback can cause the program to behave unexpectedly.

File Overwriting:
Journal files are overwritten if the program is run multiple times on the same day.

Error Messages:
API errors show generic messages instead of user-friendly ones.

Graphical User Interface:
Planned GUI for easier use was scrapped due to time constraints.

Database Integration:
Saving entries to a database was not implemented due to limited time.

API Limitations:
Occasional delays or rate limits from the OpenAI API can slow responses. 
**

### ❗Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- (For partners) How well did you work with your partner? What made it go well? What made it challenging?

** 
We selected this project because it's an interesting, and practical application that lets a user journal how their day went and get feedback from AI, which can be reassuring.
This is the type of application that you would actually see be implemented as a mobile application that users learn to use everyday as part of their routine if implemented correctly.

While our final project is missing some of the features we initially envisioned (database to keep track of journal entries, more in depth, personalized AI feedback on sentiments)
We believe that we did a decent job at building this prototype. For one, the journaling prompts are pretty comprehensive, the GUI is simple and easy to understand (it may not be the best
GUI that we could have came up with) but it's functional, and the API is working well for its intended purpose. We believe our project is complete, though not fully polished.

We learned what it takes seeing an application through from ideation to completition from scratch. We planned the project, found the best way to approach it, put it into classes, and
we dove headfirst into barebones functionality before tackling anything else. We then worked on connecting the API, which was our project's most interesting feature and something we didn't
know how to do initially, but all of the resources out there helped, and this has given us a great idea of the applications that can be built with an AI API. Lastly, we connected the GUI
and it showed us how much difference a simple GUI can make in making a project look "polished."

The hardest part was implementing the AI API, we used OPENAI's chatgpt for guidance which was trained on an earlier model. After updating and migrating to the newest OPENAI API version,
we kept running into issued and could not tell why. It took us over 5 hours of debugging and research to find out that CHATGPT is a terrible resource for implementing it's own API, and
we were able to correctly update and implement the API by looking at the OPENAI documentation.

Not relying too much on CHATGPT for implementing an API. Seeing the timeframe for the features we wanted to build (in this case we didn't have time to build the database), finding
the biggest selling features and polishing those things first when it comes to improving the project at the end. Making a nicer, more comprehensive GUI.

We worked very well as partners by collaborating over virtual meetings, keeping good communication, blocking time off to work on our project ahead of time, and delegating tasks so we both
chip away at the project. Having two people also made it easier when it came to debugging issues and improving our program. The hardest part was finding the time to work on our project
when things came up, such as illness, traveling out of state, preparing for final exams, etc. But we made it work.
**