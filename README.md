# hack4congress

## Summary
Using Topic Modeling and Natrual Language Processigng, we've developed a tool to automatically classify congresssional email, so that underpaid interns don't have to do it manually.

## Contents
* Getting Started  
* Problem  
* Proposal  

* Modeling details
* Data
* Programs  
* References

## Getting Started

1. Install packages
```
pip install --upgrade google-api-python-client
pip install gflags
```

2. Download emails to /emails folder
```
python downloader.py
```

## Problem
Communicating with the Public

Suppose you want to pass along the message to your congressperson about a particular issue (such as this one).
https://sunlightfoundation.com/usethenet/
 
Do you sign an online petition? Do you tweet at them? Do you, "call your congressperson", with a real telephone? Congressional offices are inundated with all kinds of messages from the public through various mediums, particularly the outmoded telephone. One big problem with new  21st century modes of trying to contact congress is that it requires user adoption; you have to convince both congressional offices and the general public to use a new platform, which can be challenging. Meanwhile, citizens are already trying to contact their congressperson via email and other online modes of textual communication, but being ignored or simply receiving in response a generic "thank you" message. The problem is that the communication coming in via text from the internet is too unstructured to be useful. How many of these messages are people taking the time to write versus automatically generated from a petition website? How many of these people are actually in my constituency?  What are the breadth of issues are coming in through these emails? Which ones do we read? This proposal is to provide a tool to untangle this mass of text and glean from it the meaningful messages that the public is trying to send their elected representative through various online modes of communication. Furthermore, structuring the swaths of incoming text can help make the conversation between the public and an elected representative two-way rather than one-way. 


## Proposal

Use topic modeling to help congressional offices keep a pulse on text that comes in from the public and create structured two-way channels of communication. We start with emails, but the concept can be applied to all textual mediums. We automatically categorize incoming emails so that the representative can (1) get a sense of what issues are important to the public and (2) reply to incoming communications with issue-specific responses, online polls, or ways for the people to take meaningful action on the issues they contacted the representative about. We can use NLP to take the swath of incoming communications and turn it into a sort of dashboard, outlining which emails are common or representative of a larger group of communications and showing snippets of text that are representative of all the emails coming in. Providing insights into who is trying to contact a congressional office via public channels such as email and about what can empower a congressional office to communicate with the public in a more meaningful two-way dialogue.

Submitted by : dhrumil.mehta@gmail.com


## Details

### Email Classification Categories

Each email is receives three tags:

1. form-style or personal email?  
2. what is the email about? (topic analysis)  
3. what is the email category?

* ty			Thank you
* meeting		Meeting Request
* action		Case work /Action request
* opinion		(Policy) opinion
* question		question/info request

* inter office  inter office chatter about operations



## Data



## Programs
`.py programs`
 [to do]

`/programs/explore.R`
explore datasets in R



## References
comments from:
http://www.whitehouse.gov/administration/eop/

Jeb Bush Emails - context
http://goodattheinternet.com/2014/12/30/the-jeb-bush-emails/

Jeb Bush Emails - direct link to data
https://www.dropbox.com/s/zlf087xir16nc9o/bushemails.db.zip?dl=0

