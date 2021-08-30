<p align="center">
  <img src="/static/readme/logo.png" 
alt="logo"/>
</p>

## Code Institute - Milestone Project 4

![Image containing example of responsiveness within several screens](/static/readme/responsive.png)

This project was created for the last (fourth) Milestone Project of the Full Stack Software Development Diploma at Code Institute. The main requirements were to produce "a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service. This will be achieved using HTML, CSS, JavaScript, Python+Django, MySQL or Postgres, Stripe and any additional libraries and external APIs.

It was also a requirement to add payment facilities and this was achieved through using Stripe.

The live site can be found [here](https://k9kit.herokuapp.com/)

**For testing purposes, please use the following credit card details:**

`Card number:` 4242 4242 4242 4242
`Exp:` any date in the future (please use MM/YY format)
`CSV:` any 3 numbers, for example 424


## Table of Contents:  <a name="home"></a>

- [Introduction](#introduction)
- [User Experience](#ux)
  - [User Stories](#user-stories)
  - [Visual Identity](#visual-identity)
    - [Logo and branding](#logo)
    - [Colour scheme](#colours)
    - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
  - [Languages and Frameworks](#languages-and-frameworks)
  - [Tools and resources](#tools-and-resources)
- [Features](#features)
    - [Features for future implementation](#future-feat)
- [Database Design](#database-design)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Local Hosting](#local-hosting)
  - [Live Hosting](#hosting)
  - [AWS](#aws)
- [Credits](#credits)
  - [Images](#images)
  - [Image editing](#image-editing)
  - [Coding Ideas](#coding-ideas)
- [Acknowledgements](#acknowledgements)


## **Introduction**

This project was created for the last (fourth) Milestone Project of the Full Stack Software Development Diploma at Code Institute. The aim of the site is to provide a pleasant online shopping experience in order for customers to view and purchase dog apparel. There are different types of dog clothing and accessories for sale, as well as toys. The site also features a sort of 'blog' area where periodic newsletters are posted by the site owners and also a 'tips' section where useful information for dog owners is posted every now and then.

There is also the option for customers to ad their own review on their experience when purchasing from the site.

Due to the nature of the business (clothes and accessories for dogs!) the tone of the site and design is all very light-hearted and playful, as well as the communication style.



## **User Experience**
 
### <ins>User Stories</ins>


Below are the different goals and aims of the site when viewed from the developer's perspective, the site owner's perspective and the user perspective.

**Developer:**

- As the **developer**, I want to create a website so that the business owner can show their products and mazimise sales

- As the **developer**, I want the website to be aesthetically pleasing to those who visit the website making good use of HTML, CSS and Bootstrap. 

- As the **developer**, I want the website to function in the intended ways and allowing purchasing of items using Javascript, Python and Stripe.

- As the **developer**, I want everything to be stored in a back end data network which in this case was SQLite3 during the development stage and PostgreSQL on deployment. 



**Site owner:**

- As a **site owner**, I want to be able to provide an array of clothes and accessories for dogs to potential customers and display them in the best way possible.

- As a **site owner**, I want to be able to provide real-time information on current stock available for purchase at any one time.

- As a **site owner**, I want to be able to add new products to the site.

- As a **site owner**, I want to be able to edit existing products on the site.

- As a **site owner**, I want to be able to delete existing products from the site.

- As a **site owner**, I want to be able to add a Newsletter post to the site.

- As a **site owner**, I want to be able to edit Newsletters on the site.

- As a **site owner**, I want to be able to delete Newsletters from the site

- As a **site owner**, I want to be able to add a 'Tip' post to the site.

- As a **site owner**, I want to be able to edit 'Tip' content on the site.

- As a **site owner**, I want to be able to delete 'Tip' content from the site.

- As a **site owner**, I want to be able to edit and delete reviews from the site in order to avoid malicious content being posted.

- As a **site owner**, I want to be able to take payment through the site.



**Users:** 

- As a **user**, I want the site to be easy to navigate and intuitive.

- As a **user**, I want to be able to browse the site and search by keywords.

- As a **user**, I want to be able to make a purchase without needing to register on the site. 

- As a **user**, I want to be able to register on the site and have an account. 

- As a **user**, I want to receive confirmation emails.

- As a **user**, I want to be able to log in and out of the site.

- As a **user**, I want to be able to store my default delivery information and my order history.

- As a **user**, I want to be able to view all the products available, and also filter the view by category and price.

- As a **user**, I want to be able to view more details about each product by clicking on it. 

- As a **user**, I want to be able to easily add products to my basket. 

- As a **user**, I want to be able to easily navigate to my bag and see which products I have added to it. 

- As a **user**, I want to be able to see how much the bag total amounts to and add/remove items from the bag before checkout. 

- As a **user**, I want to be able to leave a review on the website to help future customers decide.  

- As a **user**, I want to be able to view useful content such as newsletters and tips.

- As a **user**, I want to be able to leave a review with my experience for future customers.



[Back to Table of Contents](#home)

### <ins>Visual Identity</ins>

One of the main goals besides the data and functionality management for the site creator was to provide some escapism and a pleasant visual and navigational experience by making it an attractive and easy to navigate site. There are links to the relevant pages and sections in multiple places and the user experience is seamless and smooth.

A certain level of quirkiness and fun was also deliberately added to make the experience lighter.

For this reason, the branding and colours are in keeping with this fun theme.


### <ins>Logo and branding</ins>

The logo, in keeping with the general 'cute' and fun design of the rest of the site and following the dog related theme, is a cartoon-like depiction of a bone. 

It's simple, with basic and clean lines in a very neutral colour scheme which is black and blue. This blue colour is also seen in other areas of the site, to give a feeling of cohesion. Since the rest of the site is quite colourful, I felt like it was a good idea to keep the logo simple. The logo includes the name of the site which is again, playful and simple.

<p align="center">
  <img src="/static/readme/logo.png" 
alt="logo"/>
</p>

The name for the site was chosen because of its playful undertones and the abbreviation of the word 'canine' as 'K9' which is very widely known and is short. This delivers an instant and powerful brand association and recognition. It also makes it immediately clear what the intended audience for the shop products is.

The logo is encased in the site header, which is white. The fonts are black and the same blue as the logo for cohesion.

Since this shop sells dog clothing and accessories it felt important to use images to draw users in, and therefore a homepage was created with two big images featuring a clothed dog from the front and behind. I felt that this was suited to the theme.

### <ins>Colour scheme</ins> <a name="colour"></a>

Because of the nature of the website and the intended audience (dog owners with a sense of humour and an inclination for fun) the colours have been kept lively and bright. I did want to avoid over saturation and excess though, so not many colours were deliberately used and the same few were kept throughout the site. For certain things, the colour base was kept the same but a different opacity level was used.

A mix of the same colours was therefore used throughout the whole site, with mild variations whilst keeping with the hue and theme. I also chose images that complemented these colours in order to pull the theme together and a white background was used in many areas to avoid over saturation.

Below is a list of the colours which were used as the main features of the site:

- black: "black"
- pink: #dd26a073
- blue: #00ffffe6
- blue: #4c7db3
- blue: #6f98c5
- hot pink: #dd26a0

The colour wheel with the tonalities for the base colour scheme can be found below:

![image of main colours](/static/readme/colours.png)



### <ins>Wireframes</ins>

All the wireframes were created with [Microsoft Paint](https://jspaint.app/).

I created a wireframe for each page, and the wireframes can be found here:

[All wireframes for MS4 K9-KIT](https://github.com/maxnyla/k9kit/tree/master/static/readme/wireframes/)

It is also worth nothing that, for the purpose of improving user experience, I have compressed the images used for this project using [tinypng.com](https://tinypng.com/) 




[Back to Table of Contents](#home)

## **Technologies Used**

### <ins>Languages and Frameworks</ins>

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - This was used for the site structure.

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - This was used for the styling throughout the site.

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - This was used to help the site be interactive.

- [Python](https://www.python.org/) - This was used to write the logic that underpins the site.

- [Django](https://www.djangoproject.com/) - This web framework was used for a structured and modular site to be created.

- [Font-Awesome](https://fontawesome.com/icons?d=gallery) - These icons used on this site were for buttons, headers, footer and social buttons.

- [Google fonts](https://fonts.google.com/) - These fonts were used for the site.

- [Bootstrap](https://getbootstrap.com/) - This was used for its responsive grid framework, toasts, cards, navbar and buttons.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django Crispy Forms were used to style the Django forms used throughout the site.

- [SQLite](https://docs.djangoproject.com/en/3.2/ref/databases/#sqlite-notes) - Django's built-in SQLite3 database was used during the creation, and data added through the admin panel in Django when logged in as a superuser.

- [PostgresSQL](https://www.heroku.com/postgres) - A Postgres database offered by Heroku was used for deployment. The same data was then added again through the Django admin panel, following the same process from the creation on the SQLite 3 db.

- [Gunicorn](https://gunicorn.org/) - The Python WSGI (Web Server Gateway Interface) HTTP Server used in deployment to Heroku.

- [Psycopg2](https://pypi.org/project/psycopg2/) - Psycopg2 was used to adapt Python to the PostgreSQL database.

- [Gitpod](https://www.gitpod.io/) - This was used as IDE used for code editing.

- [Git Version Control](https://git-scm.com/) - Git was used for Version Control to track and record changes to the code.

- [GitHub](https://github.com/) - GitHub was used as the remote repository, to push to and store the commited changes to the app from Git.

- [Heroku](https://www.heroku.com/home) - This hosting platform was used to deploy the live version of the website.


### <ins>Tools and resources</ins>

- [Stripe](https://stripe.com/gb) - This ecommerce payment system was used for the site payment facilities.

- [Code Institute Course Content Boutique Ado](https://www.codeinstitute.net/) – This website was based on the Code Institute Boutiqe Ado project: the main structure and model was taken from there.

- The Code Institute **SLACK Community** - General resource.

- [Stack Overflow](https://stackoverflow.com/) – General resource.

- [W3C Schools](https://www.w3schools.com/) - General resource.

- [CSS-Tricks](https://css-tricks.com/) - General resource

- [Techsini](https://techsini.com/multi-mockup/index.php) - Responsive website mockup image generator.

- [Gauger](https://gauger.io/fonticon/) - This was used to create the favicon for the website.


[Back to Table of Contents](#home)
## **Features**





### <ins>Features for future implementation</ins>







[Back to Table of Contents](#home)
## **Database Design**








[Back to Table of Contents](#home)


## **Testing**

The full testing breakdown can be found [here](https://github.com/

The below tools were used for code validation:

- [W3C Markup Validation Service](https://validator.w3.org/) - This was used to check for errors in the HTML and CSS code (More detail in the Testing section).

- [JSHint](https://jshint.com/) - This was used to check for errors in the JavaScript and jQuery code (More detail in the Testing section).

- [PEP8 online](http://pep8online.com/) -This was used to check that the Python code complied with formatting standards. 





[Back to Table of Contents](#home)


## **Deployment**

### <ins>Local hosting</ins>




### <ins>Live Hosting</ins>





### <ins>AWS</ins>





[Back to Table of Contents](#home)


## **Credits**

The shop displayed on this website is purely fictional and created by myself.

### <ins>images</ins>

The images used for this project are a mix. Some are my own photos and others were taken from:

- [Unsplash] (https://unsplash.com/)

- [Shutterstock] (https://shutterstock.com/)






[Back to Table of Contents](#home)
## **Acknowledgements**


