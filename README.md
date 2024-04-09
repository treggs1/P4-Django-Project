# CodeInstitute P4 - Justing Cooper Photography

This is an e-commerce platform dedicated to Justin Cooper Photography. It enables them to showcase and sell their prints online. They have the flexibility to upload new products, as well as edit or remove existing ones. Customers can seamlessly make purchases through the store, and they have the option to create an account for tracking their current orders and accessing records of previous ones. Having an account simplifies the checkout process for future purchases. Additionally, the site owner can efficiently monitor and track orders.


## UX

RefArchive is designed for accessibility and ease of use, it has a clean layout with a simple colour palette.

### Colour Scheme

The colour sceme was created using colours in the Bootstrap framework Using contrasting light and dark colours for background and text.

### Typography

Fonts are from Google Fonts.

Great Vibes - used for main site logo.
Gruppo - used for site headings.
Quicksand - used for all other text on the site.
## User Stories

- As a new site user, I would like to easily browse through different categories of prints offered by Justin Cooper Photography, allowing me to quickly find what I'm interested in.
- As a new site user, I would like to have a straightforward registration process that enables me to create an account efficiently, ensuring I can easily track my orders and access my purchase history.
- As a new site user, I would like to have clear and intuitive navigation menus that help me explore the website effortlessly, making it convenient to find the information I need.
- As a new site user, I would like to have access to detailed product descriptions and high-quality images for each print, enabling me to make informed purchasing decisions.
- As a new site user, I would like to have a seamless checkout experience, ensuring a smooth and secure transaction process.
## Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Wireframes

| Device | Screenshot |
| --- | --- |
| Mobile | ![screenshot](documentation/wireframes/p3-mobile.png) |
| Desktop/Tablet | ![screenshot](documentation/wireframes/p3-desktop.png) |

## Existing Features

add here

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org/) used for backend coding.
- [Django](https://www.djangoproject.com/) used as a python framework for the site.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Heroku](https://www.heroku.com/) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [JSHint](https://jshint.com/) - used to validate JS code.
- [W3 HTML validator](https://validator.w3.org/nu/) - used to validate HTML.
- [W3 Jigsaw](https://jigsaw.w3.org/css-validator/validator) - used to validate CSS.
- [AmIResponsive?](https://ui.dev/amiresponsive?url=https://ref-archive-b7110f3b2973.herokuapp.com) - used to create AmIResponsive image for README.md
- [Balsamiq](https://balsamiq.com/wireframes/) - used to create wireframes during project planning.
## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
1. Log in to Heroku - or set up a new account.
2. From the dashboard, click 'Create new app'.
3. Name your app - it will need to be unique. Select Region, then 'Create'.
4. Click on the 'Settings' tab.
5. Scroll down to Config Vars and click 'Reveal Config Vars'.
6. In the 'Key' field enter 'PORT', and in the 'Value' field enter '8000'.
7. If there is a credentials file, this will also need to be entered into the Config Vars setting.
8. Staying within 'Settings', scroll down to Buildpacks and click on 'Add Buildpacks'.
9. Select 'python' first and click 'Save changes'.
10. Then do the same again and this time select 'nodejs' and click 'Save changes'.
11. Ensure the buildpacks are in the order of python first and nodejs second. 
12. Scroll to the top and select 'Deploy'.
13. In 'Deployment method' select 'GitHub' and confirm you want to connect.
14. Enter your GitHub repository into the search bar, and then 'Connect'.
15. Under 'Automatic deploys', click on 'Enable Automatic Deploys' if you want the app to update every time you push changes to GitHub.
16. Finally, click on 'Deploy Branch' under 'Manual deploy' to deploy your app. Once completed, you will be able to view your deployed link.

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/treggs1/P4-django-project) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/treggs1/P4-django-project`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/treggs1/P4-django-project)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/treggs1/P4-django-project)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://readme.so/) | README and TESTING | tool to help generate the Markdown files | 