# Poster Bay | E-Commerce Site for Posters 

## Index:
* <a href="#project-background">Project Background :information_desk_person:</a> 
* <a href="#ux">UX :iphone:</a> 
* <a href="#features">Features :clipboard:</a>
* <a href="#technologies">Technologies Used :wrench:</a>
* <a href="#testing">Testing :flashlight:</a>
* <a href="#deployment">Deployment :rocket:</a>
* <a href="#credits">Credits :pencil2:</a>

---
<span id="project-background"></span>
## Project Background :information_desk_person:

This is the website for House of Masala - a recipe book for Pakistani dishes. It targets anybody looking for Pakistani dishes to create at home. Through an interactive & responsive design with data-driven functionalities, users are able to view a variety of recipes, create new recipes, store them on the site to share with others & edit or delete them.

---

<span id="ux"></span>
## UX :iphone:

### 1. Who is this website for?

This website can be used by Pakistanis and non-Pakistanis interested in learning more about or cooking Pakistani food. By allowing users to create recipes, it also targets those who desire to store their recipes in one place to share with others.

### 2. First-Time User Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content most relevant to me.
* As a First Time Visitor, I want to be able to register my profile.
* As a First Time Visitor, I want to be able to access my profile.
* As a First Time Visitor, I want to be able to gather key information about each recipe to be able to create the desired recipe at home.
* As a First Time Visitor, I want to be able to add a new recipe with ease.
* As a First Time Visitor, I want to be able to access, edit or delete my created recipe.
* As a First Time Visitor, I want to be able to visit their social media pages to determine how big a following the company has & how trusted it is.

### 3. Returning Visitor Goals

* As a Returning Visitor, I want to be able to log in to my profile with the credentials that were registered.
* As a Returning Visitor, I want to be able to log out of my profile.
* As a Returning Visitor, I want to be able to get a variety of new recipe options.
* As a Returning Visitor, I want to be able to see and access my added recipes.
* As a Returning Visitor, I want to be able to access my profile.
* As a Returning Visitor, I want to be able to edit or delete my added recipes.
* As a Returning Visitor, I want to be able to to get in touch with the company with any questions or suggestions I may have.

### 4. Frequent User Goals 

* As a Frequent Visitor, I want to check to see if there are any newly added recipes that have been created on the website that I can cook. 
* As a Frequent Visitor, I want to be able to log in & log out of my profile with ease. 

### Design:

I opted for a clean and fresh look & feel for this website. The background is kept white to allow for the imagery of the food to stand out, while the bright green buttons add a nice pop of color to break up the whitespace without being too distracting for the user. 

* Color Scheme:
   * The main colors used are 2 shades of Green, Dark Grey, and White. 

* Typography:
   * All Headers use Open Sans & Helvetica Neue. These are both sans-serif font with nice letter-spacing - which makes it easy-to-read & clean.
   * Arial is my secondary font, used for paragraphs. It has a lighter font-weight, which pairs nicely with other sans-serif fonts and is easy to read on smaller devices.
   * Sans-Serif is used as the backup font for both Open Sans, Helvetica Neue & Arial.

* Imagery:
   * A bright, colorful image showing popular Pakistani dishes is used for the hero image to be eye-catching & inviting to the user. In general, Pakistani food consists of different shades of brown, yellows, reds and greens and I wanted the user to get a sense of this right off the bat. Images for the recipes are also bright & vibrant, allowing the food to speak for itself.

### Wireframes & Mockups:

* View website wireframes for desktop & mobile [here](https://drive.google.com/file/d/1I_eR45ittdz8OyTWI3xFV8nl4pDpnovN/view?usp=sharing)
 
---

<span id="features"></span>
## Features :clipboard:

The site contains certain features which are not visible or available to unregistered/logged in users. These features include the ability to add a recipe, edit it, store it, and delete it (CRUD operations). Content available to all users includes the ability to view all recipes including the 3 most recently added.

### Features visible to All Users:
* **All Recipes:** 
    * * The All Recipes page contains an assortment of recipes added by House of Masala, as well as the users of the website. Each recipe card displays an image of the dish, the name, short description prep time, yield, and a CTA button to view the recipe. The creator of the recipe is also visible. 
* **Register**
	* The register feature is one visible to all users as a link on the navigation bar. Once clicked, it leads to a form where users can create a unique username and password. If the username is already taken, a message saying “Username already exists” will flash at the top of the page. Once the user has registered successfully, they will be redirected to the homepage. A success message also flashes at the top of the page signalling a successful registration.
* **Login** 
    * The login feature is also visible to all users and can be found in the navigation bar. It enables users who already have a profile to login with their credentials. If the credentials don't match those entered during registration, an error message “Incorrect Username and/or Password” will flash across the screen. For users who have not registered yet, a CTA link at the bottom of the form directs them to register. Alternatively, if the login is successful and the username & password match those stored in the database, a welcome message will flash & the user will be redirected to the profile page. 
* **Recently Added Recipes**
	* The three most recently added recipes are also visible to all users on the homepage. This section retrieves the newest recipes from the database in descending order. A CTA link at the bottom of the section leads users to the All Recipes page to view all the recipes.
* **Footer**
    * Located at the bottom of each page of the website, the footer consists of a contact us section with an email address, a short about section, and social media links leading to Pakistani food accounts intended to give users more food inspiration & recipe choices.
* **Navbar**
	* The navigation bar at the top of each page of the website enables the user to easily access all pages of the website. On smaller devices, the navbar transforms into a burger menu, where links are only visible in a dropdown menu. There are two different views of the navigation bar - one view to all users, and the other to those users who are logged in to the website. 

### Features visible to Logged In/Registered Users:
* **Profile** 
    * When a user logs into their account, they are redirected to the Profile page, which is specific to that individual user. Upon entry, the user is greeted with a Welcome user message. On this page the user can see his/her added recipes (if any). If they have added a recipe, they will also see an edit & delete button on the recipe cards, where they can make changed to, or delete their recipe. These buttons are only visible to the user on the recipes added by that user.
* **Add A Recipe**
    * This feature is only visible to registered & logged in users, giving them the option to add their own recipe. Once clicked, a form appears with several input fields to fill out. Once they’ve filled in all the fields, a success message flashes on the top of the screen & the user is redirected to All Recipes, where their newly added recipe is displayed. The user will not be able to submit the form until they’ve filled in all the input fields with the specified number of characters. These specifications were put in place to avoid an incomplete recipe from being uploaded to the website.
* **Logout** 
	* The logout link is only visible to users who are logged in to the website. Located in the top navbar, it provides users to easily log out of their session
* **Edit Recipe**
	* The Edit Recipe functionality can be accessed via the user’s profile page. Here the user can view all their added recipes displayed on cards. The edit feature labelled as “Edit” appears as an orange button on the card. Once clicked, it leads to a populated form where the user can either make a change & be redirected to the recipes page, or click on cancel & remain on the profile page. If they decide to update the form & submit their changes, a flash message appears at the top of the screen letting them know their change was successful. 
* **Delete Recipe**
	* The “Delete” button can be accessed via the user’s profile page and is located on their added recipe cards. It is only visible to users who are logged in, allowing them to delete their own recipe.


### Features to implement in the Future

* Functionality to let users like or save recipes they’d like to make later 
* A warning dialog box that adds an extra step before a user deletes a recipe 
* Function to allow user to drag & drop an image instead of having to copy paste the img url

---
<span id="technologies"></span>
## Technologies Used :wrench:

### 1. Languages

This User Centric Frontend Project focused on the use of the following languages:
* HTML5 - for website structure 
* CSS3 - for styling 
* JavaScript - for running interactive features 
* Python for automating tasks & scripting, including:
    * Flask 
    * Flask pymongo
    * Jinja templating
    * BSON
    * Werkzeug
    * Dnspython

### 2. Other Programs & Frameworks Used 

* FontAwesome - for all icons used on the buttons
* Balsamiq - for creating wireframes 
* Bootstrap 4.4.1 - for assisting in responsiveness and layout of website 
* Startup Bootstrap - for website theme 
* MongoDB - database for storing user info & recipes 

### 3. IDE's 

This website was developed on GitPod.

### 4. External Hosting

This website is saved in a repository on GitHub.

---

<span id="testing"></span>
## Testing :flashlight:

### 1. Testing Tools

* [The W3C Markup Validation Service](https://validator.w3.org/) - for testing my HTML code
   * Result: No errors 
* [The W3C CSS Validation Service: W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - for testing my CSS code
   * Result: No errors
* Chrome Dev Tools - for testing:
   * Mobile responsiveness
   * CSS styling changes before implementing it in the code
   * Network to assess whether it was picking up Javascript (status: 200)

### 2. Testing User Stories (UX Section)

### A. First-Time Visitor Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
    * Upon entering the site, users are presented with a bright, catchy and easily readable banner image, which introduces the Company name and purpose of the site. 
    * In the footer, a short about us blurb gives the user further details about the company & its mission.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content most relevant to me.
    * The website is designed to be very clean and straight to the point. The navigation bar enables the user to visit different pages on the website with ease. CTA buttons also link to relevant content, pages & functions.
* As a First Time Visitor, I want to be able to register my profile.
	* The user is able to register via the navigation bar. If they accidentally click on Login, a link at the bottom of the form also redirects the user to the register page.
* As a First Time Visitor, I want to be able to gather key information about each recipe to be able to create the desired recipe at home.
	* All recipe cards contain a button leading the recipe page, where the recipe is presented to the user in great detail.
* As a First Time Visitor, I want to be able to add a new recipe with ease.
	* Once the user registers their profile, they are able to navigate to the Add a Recipe page via the navigation bar. 
* As a First Time Visitor, I want to be able to access, edit or delete my created recipe.
	* Once the user has registered & created a recipe, they are able to view the recipes they added on their profile page (accessible via the navbar). Each recipe card created by them, includes an edit & delete button allowing them to update the recipe or delete it. 
* As a First Time Visitor, I want to be able to visit their social media pages to determine how big a following the company has & how trusted it is.
    * In the footer, social media icons lead to the company's social media pages.

### B. Returning Visitor Goals

* As a Returning Visitor, I want to be able to log in to my profile with the credentials that were registered.
    * Users can login easily via the navigation bar with their credentials. 
* As a Returning Visitor, I want to be able to log out of my profile.
	* Once in session, users can log out of the website via a link in the navbar. This will lead back to the login form in case they want to log back in.
* As a Returning Visitor, I want to be able to get a variety of new recipe options.
	* Via the homepage, the section “Recently Added Recipes” allows the user to quickly see if new recipes have been added since the last time they visited the website. 
	* The user can also check “All Recipes” page to see all the recipes. 
* As a Returning Visitor, I want to be able to see and access my added recipes.
	* Once in session, the user can visit their profile page, via the navbar, to see and access their own created recipes.
* As a Returning Visitor, I want to be able to access my profile.
	* Once in session, the user can access their profile via the top navbar.
* As a Returning Visitor, I want to be able to edit or delete my added recipes.
	* Once the user has logged in, they are able to view the recipes they added on their profile page (accessible via the navbar). Each recipe card created by them, includes an edit & delete button allowing them to update the recipe or delete it. 
* As a Returning Visitor, I want to be able to to get in touch with the company with any questions or suggestions I may have.
    * In the footer, the user can find the email address of the company to get in touch with suggestions or questions.

### C. Frequent Visitor Goals

* As a Frequent Visitor, I want to check to see if there are any newly added recipes that have been created on the website that I can cook. 
    * At this point the user is familiar with the layout of the website & can recognize new recipes that have been added.
* As a Frequent Visitor, I want to be able to log in & log out of my profile with ease. 
	* The user is also familiar with the placement of the login and logout buttons located in the top navbar. 

### 3. Further Testing

This website has been tested by friends and family to check for:
* bugs or disabled links
* clear user experience & navigation
* picture loading speed
* login/register/logout functionalities
* edit, add, delete recipe functionalities
* correct flash message displays

### 4. Browser & Device Testing

This website has been tested on the following Desktop devices:
*  MacBook Pro 2013 - Chrome & Safari
*  Microsoft Edge - Chrome

This website has been tested on the following Mobile/Tablet devices:
* iPhone 11 - Safari
* iPhone 6 - Safari
* iPhone 6s - Safari
* iPad Air 2 - Safari

### 5. Bugs & Problems

No bugs were spotted during testing.

During the development stage, I encountered an issue with my gitignore file, which was leaving the env.py file exposed. This was quickly resolved by creating a duplicate env file, removing it from the gitignore file & then re-adding it after pushing the code to Github.

---

<span id="deployment"></span>
## Deployment :rocket:

### Deployment to Heroku

This project was deployed to Heroku by following the steps below:
1. Create a requirements.txt by typing in the terminal command line: pip3 freeze --local > requirements.txt
2. Create a Procfile by typing in the terminal command line with: echo web: python app.py > Procfile.
3. Remove the trailing whitespace in the Procfile.
4. Type in the commands in the terminal: git add -A, Git commit -m "Your message" & Git push to push these changes into GitHub.
5. Navigate to the [Heroku website](https://dashboard.heroku.com/apps)
6. Create a new app by selecting the button labelled “New” on the dashboard and give the app a unique name.
7. Select the region you're situated in.
7. In the Deploy tab, select Github. Make sure you're connected to the right account.
8. Type in the name of the repository you wish to connect to 
9. In the Settings tab, click on Reveal Config Vars and set as below:
    * IP = 0.0.0.0
    * MONGO_DBNAME = [name of your MongoDB]
    * PORT = 5000
    * MONGO_URI = unique link to your Mongo database
    * and finally your SECRET_KEY.
10. Once added, click "Hide Config Vars"
11. Navigate to the Deploy tab and select Enable Automatic Deploys.
12. At the bottom of the page, click on Deploy Branch, ensuring the master branch is selected.

### Forking the GitHub Repository
Forking the GitHub Repository creates a copy of the original repository in our GitHub account to view and/or make changes without affecting the original repository. This can be done through the following steps:

1. Log in to GitHub and find the GitHub Repository
2. At the top of the Repository - just above & to the right of "Settings" on the menu, locate the "Fork" Button.
3. Click this to create a copy of the original repository in your GitHub account.

### Live Site
* This website is stored in a repository on [Github](https://github.com/ZahraSadiq/Milestone2-AntwerpHotSpots.git)
   * It was developed on GitPod, with changes regularly pushed to GitHub's repository using one main master branch.
   * Both the deployed and developed versions of this website are identical.

This site is hosted on Heroku.
* You can view the live site [here](https://house-of-masala.herokuapp.com/)
* The url for the site is: https://house-of-masala.herokuapp.com/

---
<span id="credits"></span>
## Credits :pencil2:

### 1. Code Snippets

* The python code in this project is based on The Task Manager Mini project by Code institute.
* The website is built with Clean Blog theme from Startup Bootstrap and mimics some of the interactive & design elements created for the theme.

### 2. Media

* Icons from: [FontAwesome](https://fontawesome.com/icons?d=gallery)
* [Banner image](https://www.foodies.pk/blog/introduction-to-pakistani-cuisine/) 
* Recipe images were sourced from:
    * [Chicken Karahi Keema](https://fatimacooks.net/recipe/chicken-karahi-keema/)
    * [Prawn Pilau](https://www.ruchikrandhap.com/wp-content/uploads/2017/08/Prawn-Pulao-1-1024x683.jpg) 
    * [Kheer](https://www.whiskaffair.com/wp-content/uploads/2019/04/Rice-Kheer-2-3.jpg) 
    * [Bhunni Mash Daal](https://kfoods.com/images1/newrecipeicon/bhuni-daal-mash_12184.jpg) 
    * [Mutton Pilau](https://fatimacooks.net/mutton-pulao-recipe-yakhni-pilau-rice/)
    * [Aloo Palak](https://i2.wp.com/spicepaw.com/wp-content/uploads/2020/01/Aloo-Palak-1.jpg?fit=3124%2C3129&ssl=1) 

### 3. Content

* Recipes for the following were sourced from:
    * [Chicken Karahi Keema](https://fatimacooks.net/recipe/chicken-karahi-keema/)
    * [Prawn Pilau](https://fatimacooks.net/recipe/prawn-pilau-biryani-rice/)
    * [Kheer](https://fatimacooks.net/recipe/cardamom-kheer/)
    * [Bhunni Mash Daal](https://fatimacooks.net/bhuni-mash-daal/)
    * [Mutton Pilau](https://fatimacooks.net/mutton-pulao-recipe-yakhni-pilau-rice/)
    * [Aloo Palak](https://fatimacooks.net/aloo-palak-recipe-spinach-potato-curry/) 
  
### 4. Acknowledgements

* **Oluwafemi Medale (My CI Mentor):** Thanks for your advice and support.