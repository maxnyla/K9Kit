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

Items that would be interesting for future development are:

- Allow users to add more fields to their profile: Full name, email, etc.

- Allow users to add products to their 'favourites' so they can access liked items later on and purchase these.

- Allow users to like reviews

- Allow users to create and add items to a wishlist or 'save for later' list ready for purchase later on.

- Allow users to upload an image when leaving a review as well as their text.

- Allow users to select a specific date for delivery. 



[Back to Table of Contents](#home)



## **Database Design**


Throughout the development stage of the project, SQLite3 was used as this is the default database which is included with Django. On deployment, you are given the option to utilise PostgreSQL as this is included with Heroku which is the route I went down. 
Whenever a model change was made on the local development IDE, the database had to be manually pushed to the new Heroku database by running the migrations again.

Django Allauth, specifically `django.contrib.auth.models` provided the **User** model that is used in the Profile App.

**Code Insitiute - Boutique Ado** was used as a template for the majority of the project. Additional models were created with the names of **Reviews**, **Newsletters** and **Tips** to supplement the project and meet the pass criteria.


### **Products** App

### Category Model

| Name          | Database Key  | Field Type | Type Validation |
| ------------- | ------------- | ---------- | --------------- |
| Name          | name          | CharField  | max_length=254  |
| Friendly Name | friendly_name | CharField  | max_length=254  |


### Product Model

| Name        | Database Key | Field Type    | Type Validation                                              |
| ----------- | ------------ | ------------- | ------------------------------------------------------------ |
| Category    | category     | ForeignKey    | "Category", null=True, blank=True, on_delete=models.SET_NULL |
| SKU         | sku          | CharField     | max_length=254, null=True, blank=True                        |
| Name        | name         | CharField     | max_length=254                                               |  |
| Description | description  | TextField     |                                                              |
| Has_sizes   | has_sizes    | Boolean       | null=True, blank=True                                        |
| Price       | price        | DecimalField  | max_digits=6, decimal_places=2                               |
| Rating      | rating       | Decmial Field | max_digits=6, decimal_places=0, null=True, blank=True        |
| Image_URL   | imge_url     | URLField      | max_length=1024, null=True, blank=True                       |
| Image       | image        | ImageField    | null=True, blank=True                                        |



### **Profiles** App

### UserProfile Model

| Name                    | Database Key            | Field Type    | Type Validation                              |
| ----------------------- | ----------------------- | ------------- | -------------------------------------------- |
| User                    | user                    | OneToOneField | User, on_delete=models.CASCADE               |
| Default Phone Number    | default_phone_number    | CharField     | max_length=20, null=True, blank=True         |
| Default Street Address1 | default_street_address1 | CharField     | max_length=80, null=True, blank=True         |
| Default Street Address2 | default_street_address2 | CharField     | max_length=80, null=True, blank=True         |
| Default Town or City    | default_town_or_city    | CharField     | max_length=40, null=True, blank=True         |
| Default County          | default_county          | CharField     | max_length=80, null=True, blank=True         |
| Default Country         | default_country         | CountryField  | blank_label="Country", null=True, blank=True |
| Default Postcode        | default_postcode        | CharField     | max_length=20, null=True, blank=True         |



### **Reviews** App

### Review Model

| Name        | Database Key | Field Type    | Type Validation                       |
| ----------- | ------------ | ------------- | ------------------------------------- |
| User        | user         | ForeignKey    | UserProfile, on_delete=models.CASCADE |
| Review Title| review_title | CharField     | max_length=254                        |
| Review Body | review_body  | TextField     | null=True, blank=True                 |
| Review By   | review_by    | CharField     | max_length=254                        |



### **Newsletters** App

### Newsletter Model

| Name            | Database Key     | Field Type    | Type Validation  
| -----------     | ---------------  | ------------- | -------------------------- |                                         
| Newsletter Title| newsletter_title | CharField     | max_length=254             |
| Newsletter Body | newsletter_body  | TextField     | null=True, blank=True      |
| Newsletter By   | newsletter_by    | CharField     | max_length=254             |
| Newsletter Date | Newsletter_date  | DateTimeField | auto_now_add=True          |



### **Tips** App

### Tip Model

| Name        | Database Key  | Field Type    | Type Validation  
| ----------- | ------------- | ------------- | -------------------------- |                                         
| Tip Title   | tip_title     | CharField     | max_length=254             |
| Tip Body    | tip_body      | TextField     | null=True, blank=True      |
| Tip By      | tip_by        | CharField     | max_length=254             |



### **Checkout** App

### Order Model


| Name            | Database Key    | Field Type                      | Type Validation                                                                      |
| --------------- | --------------- | ------------------------------- | ------------------------------------------------------------------------------------ |
| Order Number    | order_number    | CharField                       | max_length=32, null=False, editable=False                                            |
| User Profile    | user_profile    | ForeignKey                      | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| Full Name       | full_name       | CharField                       | max_length=50, null=False, blank=False                                               |
| Email           | email           | EmailField                      | max_length=254, null=False, blank=False                                              |
| Phone Number    | phone_number    | CharField                       | max_length=20, null=False, blank=False                                               |
| Country         | country         | CountryField                    | blank_label='Country\*', null=False, blank=False                                     |
| Postcode        | postcode        | CharField                       | max_length=20, null=True, blank=True                                                 |
| Town or City    | town_or_city    | CharField                       | max_length=40, null=False, blank=False                                               |
| Street Address1 | street_address1 | CharField                       | max_length=80, null=False, blank=False                                               |
| Street Address2 | street_address2 | CharField                       | max_length=80, null=False, blank=False                                               |
| County          | county          | CharField                       | max_length=80, null=True, blank=True                                                 |
| Date            | date            | DateTimeField auto_now_add=True |                                                                                      |
| Delivery Cost   | delivery_cost   | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |
| Order Total     | order_total     | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |
| Grand Total     | grand_total     | DecimalField                    | max_digits=6, decimal_places=2, null=False, default=0                                |
| Original bag    | original_bag    | TextField                       | null=True, blank=True                              |
| Stripe pid      | stripe_pid      | CharField                       | max_length=254                                 |


### OrderLine Model


| Name           | Database Key   | Field Type   | Type Validation                                                                    |
| -------------- | -------------- | ------------ | ---------------------------------------------------------------------------------- |
| Order          | order          | ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product        | product        | ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size   | product_size   | CharField    | max_length=2, null=True, blank=True                                                |
| Quantity       | quantity       | IntegerField | null=False, blank=False, default=0                                                 |
| Lineitem Total | lineitem_total | DecimalField | max_digits=6, decmial_places=2, null=False, blank=False, editable=False            |






[Back to Table of Contents](#home)


## **Testing**

The full testing breakdown can be found [here](https://github.com/maxnyla/K9Kit/blob/master/TESTING.md)

The below tools were used for code validation:

- [W3C Markup Validation Service](https://validator.w3.org/) - This was used to check for errors in the HTML and CSS code (More detail in the Testing section).

- [JSHint](https://jshint.com/) - This was used to check for errors in the JavaScript and jQuery code (More detail in the Testing section).

- [PEP8 online](http://pep8online.com/) -This was used to check that the Python code complied with formatting standards. 





[Back to Table of Contents](#home)



## **Deployment**

### <ins>Hosting</ins>

The site is hoseted on [Heroku](https://www.heroku.com/home).

Deployment of the site was achieved by following the steps below:

- Created a new repository in GitHub.

- Opened repository in my IDE, Gitpod - by cloning the repo from GitHub.

- Created a requirements.txt file by typing `pip3 freeze > requirements.txt` in the terminal. This tells Heroku what dependencies are required.

- Created a Procfile and added `web: gunicorn k9kit.wsgi:application` to the file.

- Checked the Procfile to make sure there is no extra line after the first line as this can confuse Heroku.

- Push the requirements.txt and Procfile to GitHub.

- Logged into Heroku and selected "Create New App".

- Selected the input field "App Name" and gave app a unique name using dashes instead of spaces.

- Selected the region closest to my location and free to use!

- Clicked "Create App".

- Clicked "Resources" and typed in Postgres in the Add-ons search bar.

- Selected Heroku Postgres and provisioned a free Hobby Dev database.

- Retrieved the Database URL from the hidden Config Vars in "Settings".

- Pasted the Database URL in the database path in settings.py and removed the local settings.

- Ran migrations to build the database in Postgres.

- Loaded the JSON files - Categories, Counties, Products with `python manage.py loaddata <JSON filename>`.

- Created a superuser with `python manage.py createsuperuser` and followed the instructions in the terminal.

- Removed the Postgres Database URL so it didn't end up in version control.

- Typed `heroku config:set DISABLE_COLLECTSTATIC=1` in the terminal to stop Heroku collecting the static files.

- Pushed all changes to GitHub.

- Typed `git push heroku master` to push everything to Heroku.

- Selected "Deploy" from the Heroku App menu.

- Selected "GitHub" from the "Deployment Method" section of the page.

- Ensured my GitHub profile name was showing in the "Connect to GitHub" section and inserted my GitHub repo name in the input field and clicked "Search".

- Once Heroku had found my repo, I clicked "Connect" to complete the link.

- Selected "Settings" from the Heroku App menu.

- Selected "Reveal Config Vars" and inputed the relevant key/value information for the following:


| Config Var            | Key                                                                               |
| --------------------- | --------------------------------------------------------------------------------- |
| AWS_SECRET_KEY_ID     | obtained when you set up AWS                                                      |
| AWS_SECRET_ACCESS_KEY | obtained when you set up AWS                                                      |
| DATABASE_URL          | created when you provisioned Postgres                                             |
| EMAIL_HOST_PASS       | obtained from your email provider                                                 |
| EMAIL_HOST_USER       | your email address                                                                |
| SECRET_KEY            | obtained from [miniwebtool](https://miniwebtool.com/django-secret-key-generator/) |
| STRIPE_PUBIC_KEY      | obtained from STRIPE                                                              |
| STRIPE_SECRET_KEY     | obtained from STRIPE                                                              |
| STRIPE_WH_SECRET      | obtained from STRIPE                                                              |
| USE_AWS               | True                                                                              |

- Selected "Deploy" from the Heroku App menu.

- Scrolled down the page and selected "Enable Automatic Deployment".

- Selected Master Branch under "Branch Selected".

- Clicked "Deploy Branch"

- Once site was deployed, clicked "View" to launch the app and be able to view it within the browser.

- Heroku now updates every time you push to GitHub.



### <ins>AWS</ins>

For the static css, js and media files to be stored and useable with Heroku, you need an AWS account.

- Go to [AWS](aws.amazon.com) and either log in or create an account.

- Search for S3.

- Create a new bucket and ensure that the `Block All Public Access` tickbox is unchecked and click 'Create Bucket`.

- Click on the Properties tab and enable `Static Website Hosting`. This will allow AWS to host our static files.

- Input `index.html` and `error.html` in the appropriate fields and hit save.

- Click on the Properties tab and click CORS configuration and add the below before hitting save:

  ```
  [
  {
  "AllowedHeaders": [
  "Authorization"
  ],
  "AllowedMethods": [
  "GET"
  ],
  "AllowedOrigins": [
  "*"
  ],
  "ExposeHeaders": []
  }
  ]
  ```

- Click the Policy Tab and select Policy Generator which creates a security policy for the bucket.

- The policy type is S3 Bucket Policy and the Action will be `get object`.

- Copy the ARN (Amazon Resource Name) from the bucket and paste it in the ARN field.

- Click `Add Statement` and then `Generate Policy`.

- Copy the generated policy in to the Bucket Policy Editor.

- Add `/*` at the end of the resource key as this will allow access to all resources in the bucket.

- Click Save.

- Click the Access Control tab and set the list object permission to everyone under the Public Access section.

- Open IAM from the service menu.

- Create a group for your user to belong to.

- Create an access policy for you the group which gives access to the S3 bucket.

- Click the JSON tab and select import managed policy, search for S3 and select S3 Full Access Policy.

- Create a user, give them programmatic access and attach it to the group.

- Download the CSV file that is generated as this contains the keys required to use AWS.

- Install boto3 and django-storages using `pip3 install`.

- Add the keys to the Config Vars in Django.

- Create a custom_storage file.

- Run `python manage.py collectstatic` and transfers the static info to AWS.




[Back to Table of Contents](#home)


###  LOCAL HOSTING

If you wish to clone a copy of my project you will need to:

- Navigate to my GitHub [repository](https://github.com/maxnyla/K9Kit).

- Click the `Code` button next to the Green Gitpod button.

- Either, download the zip file or clone the repo using `gh repo clone maxnyla/k9kit` in the terminal.

- Install the modules listed in the requirements.txt file using `python -m pip -r requirements.txt` in the terminal.

- Install the JSON files using `python manage.py loaddata categories`,  and `python manage.py loaddata products` in this order as "products" relies on the previous two.

- Create a SuperUser by using `python manage.py createsuperuser` and following the onscreen instructions.

- Run migrations to create your database by using `python manage.py migrate`

- Create an env.py file in your application folder and add the following:

  ```
  import os

  os.environ.setdefault(
  "SECRET_KEY", "ADD YOUR SECRET KEY HERE"
  )
  os.environ.setdefault(
  "STRIPE_PUBLIC_KEY",
  "ADD YOUR STRIPE PUBLIC KEY HERE,
  )
  os.environ.setdefault(
  "STRIPE_SECRET_KEY",
  "ADD YOUR STRIPE SECRET KEY HERE",
  )
  os.environ.setdefault("STRIPE_WH_SECRET", "ADD YOUR STRIPE WEBHOOK SECRET HERE")

  os.environ.setdefault("EMAIL_HOST_PASS", "ADD YOUR EMAIL HOST PASSWORD HERE")

  os.environ.setdefault("EMAIL_HOST_USER", "ADD YOUR EMAIL HOST USERNAME HERE")

  ```

- The app can now be run locally by typing python manage.py runserver. When your project is run locally, add '/admin' to the locally deployed project's URL.


## **Credits**

The shop displayed on this website is purely fictional and created by myself.

### <ins>images</ins>

The images used for this project are a mix. Some are my own photos and the rest were taken from:

- [Unsplash] (https://unsplash.com/)

- [Shutterstock] (https://shutterstock.com/)



[Back to Table of Contents](#home)
## **Acknowledgements**

Inspiration for this project was taken from the Code Institute Mini-project, Boutique Ado. This was used as a base and then adapted to build this site on.

I would like to mention all the different resources and sites that are out there, with their respective communities, which have been a huge help for me. 
Some of them are:

-Stack Overload

-Freecodecamp

-The CI Slack community, always so supportive and informative!

-Google (for all the things that I've looked up during this project, which have led me to all these amazing sites)

-Of course I must mention my fantastic mentor Felipe Souza Alarcon for all his patience, help and ideas during this project, and his flexibility and availability. 
Always much appreciated.

-Big thanks to my new colleague Jo who so kindly took the time to take a look at my project and come up with some fantastic ideas and suggestions. So unexpected and fantastic!

And lastly, I could not leave out the Code Institute team: the other students on Slack, the tutor support and all the mentors who are always welcoming and trying to help.

Special mention to my 'May 2020' channel buddies for the constant chat, help and support. You guys are an amazing little group! Eespecially Ian, Emma, Chloe, Adam, Kamil..you guys are amazing and it's been such a blast sharing this course with you!  

Many thanks as well to the assessors who will spend many long hours reading through all these files. 

:house:[ Back to Table of Contents](#home)
