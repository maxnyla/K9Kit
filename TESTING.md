<p align="center">
  <img src="/static/readme/logo.png" 
alt="logo"/>
</p>

## Code Institute - Milestone Project 4 - TESTING

![Image containing example of responsiveness within several screens](/static/readme/responsive.png)

This is the Testing section for K9-Kit, the last (fourth) Milestone Project of the Full Stack Software Development Diploma at Code Institute.


The main Readme file can be found [here](https://github.com/maxnyla/K9Kit#readme)



## Table of Contents :house: <a name="home"></a>

- [Introduction](#introduction)

- [Responsiveness and Speed](#responsiveness)

- [Browser Compatibility](#browsercomp)

- [Code Validation](#codeval)

- [Defensive Design](#defensived)

- [Testing User Stories](#testing)

-  [Bugs and Enhancements](#bugs)



:house:[ Back to README file](README.md).



## Introduction <a name="introduction"></a>

This section will go over the various methods that I have used to perform my testing for this project.



## Responsiveness and Speed<a name="responsiveness"></a>

Responsiveness and speed as well as general usability was tested manually.

Chrome Developer Tools were used to test responsiveness on all screen sizes. This was done whilst the project was being built on, 
to ensure at all times that the build was going well and that there would be no surprises later on. I made changes to the css stylesheet
via media queries for smaller screens at any time when I noticed an issue with responsiveness.

Several functions or sections were edited through media queries.

I also tested this via my mobile devices and asked other people to test it and provide feedback as well.



## Browser Compatibility <a name="browsercomp"></a>

This site has been tested through all the browsers that I have access to:

- Google Chrome

- Mozilla Firefox

- Microsoft Edge

- Opera

- Mobile chrome via Android phone and tablet

- Mobile Samsung browser via Android phone and tablet


It has appeared to behave correctly on all these platforms and no issues were observed.



## Code validation <a name="codeval"></a>

I ran all my code through the various relevant validators.

-The [CSS Validation Service](https://jigsaw.w3.org/css-validator) for the CSS code.


The CSS validator resulted in one error to do with a font size, which I corrected, and multiple warnings which could be ignored as they were due to elements having the same colour for the border and other areas.


![css validation results](/static/readme/validation/css_val.png)



-The [PEP8 Validation](http://pep8online.com/) was used for the Python code.

The PEP8 code validator gave me a few indentation errors and lines that were too long so I fixed all these before saving the files again and the code passed 
this time, after the changes.


![app.py validation results](/static/readme/validation/pep8_val.png)



-The [W3C Markup Validation Service](https://validator.w3.org) was used for the HTML code.

The HTML validation was a bit difficult, since the checks threw multiple errors due to the use of Jinja templating. The checks point to the lack of proper headers 
on the templates and also multiple errors are caused by the use of the } symbols in the Jinja templates. For this reason I decided to ignore the errors, since
I am not aware of a way to bypass these.

Since the HTML code is so extensive as there are a number of files, instead of posting each link here I have decided to post a link to the
directory where all the results for the HTML validation can be found:


[Link to all HTML validator results](/static/readme/validation)


I have also used the Chrome Developer Tools extensively throughout the project at every step. They have been very useful for each change that I made, 
and to double-check my ideas before implementing and committing them. I have made multiple colour and formatting changes due to using these which
would have taken a long time otherwise.



:house:[ Back to Table of Contents](#home)



## Defensive Design <a name="defensived"></a>

This project includes defensive design, which has been implemented via two routes: 

- first:
  on the html templates themselves via minimum requirements when completing the forms, and 
  
- secondly:
 via the Python code in the apps.py files, to request database checks before certain actions are completed.

For example, if the session user does not match the username of a superuser, they will not be able to access restricted areas to add, delete or edit content because 
the system will redirect them to another page.

This design is also applied to the html code affecting navigation, by preventing users from seeing linkes to pages that they are not supposed to see.

For example, a user who is not logged in will not be able to see the links to add reviews or to their account and so on.

By doubling up on the front end and back end defensive design, the system becomes harder to manipulate and more secure.


## Testing User Stories <a name="testing"></a>

***Testing process***

A manual testing process has been followed for this project in order to assess user experience and usability, functionality data processing and responsiveness. I followed a route to route process to ensure that every feature was checked.

**User Stories:**
  All the user stories were tested to make sure the aims of the project were met and all users are able to achieve the goals of the site.

- All pages:
  All pages were tested to check if users are able to view all the pages that they should have accecss to view and if they are unable of accessing pages that they do not have permission to see, based on whether they are signed in or not.

- All forms: 
  Checked if all the forms are working as intended and if data which is inputted properly validated at the front end before it is passed to the database. Also, checked that users are not able to bypass the required fields and submit an empty or partially empty form.

- All links: 
  Tested all the links and buttons on all pages to make sure that they direct to the correct destination.


- Testing the login and registration page:

  I tried logging in with duplicated username and also with incorrect password to check that all the error messages and warnings were displaying the way they were meant to
  All the relevant flash messages were also checked for accuracy and I ensured everything was working properly before moving on


- Testing the add/ edit/ delete products form as a superuser

  I added, edited and deleted different products to ensure everything was working correctly.


- Testing the add review form as a regular user

  I added reviews to ensure everything was working correctly.


- Testing the edit/delete review form as a superuser

  I edited and deleted reviews to ensure everything was working correctly.


- Testing the add/ edit/ delete newsletter form as a superuser

  I added, edited and deleted newsletters to ensure everything was working correctly.


- Testing the add/ edit/ delete tips form as a superuser

  I added, edited and deleted newsletters to ensure everything was working correctly.









***Challenges building the site***


Whilst working on this project I encountered a series of issues that I needed to overcome. Please see below for details.
