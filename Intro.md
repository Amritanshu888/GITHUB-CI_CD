## Github Actions - CI/CD Pipelines
- Github Actions is a powerful automation tool provided by Github that enables developers to automate tasks related to their software development workflows. It allows for the creation of custom worflows , which can be triggered by various events , such as pushes to a repository , pull requests , or scheduled events. These workflows can be used for various purposes , including Continious Integration(CI), Continious Deployment (CD) , testing and more.

- Github actions is a CI/CD tool which automates the entire software development workflows. This is already provided by Github.

- Whenever i talk abt github ---> this is basically my code repository ---> i.e. we commit our code over here , we create branches.
- We work in a collaborative way over here.
- Git : It is a distributed version control system.(Super important for developers , why ?? Bcoz here u will be able to track ur source code files).
- In a specific project many developers will be collaborating , let's say i have a project over here in which lot of developers are working. Dev A --> Working on a story A , Dev B --> Working on story B. Dev C ---> Working on story C. Here each story is a different module , which needs to be finally integrated with the entire data science project.
- This is how we work in a company we work in a collaborative way.
- If developer A has created 3 files : There should be a way of tracking the entire source code which is written by develpoer A. Similarily w.r.t to developer B and C also.
- After writing the code in the local environment , they try to commit this entire code in the Github Repository. To commit to github repo we can specifically use git.
- Git will help us to track entire source code files. W.r.t this u may also get some conflicts , let's say Developer A has created some file (app.py) and dev B pulled this specific code and started writing the code in the same file as well. Now when they both commit in the github repo they might get some conflict.
- Then we resolve this conflict and then this is where my git will be super important as its a distributed version control.
- If u want to switch to a different branch , switching branches , merging branches , everywhere this Git will be super-beneficial.

## Git : It is a Distributed Version Control System.

## Github Actions
- Its already provided by git and its a CI/CD tool.
- CI/CD Tool: Means Continious Integration and Continious Deployment.
- Continious Integration (CI) and Continious Deployment (CD) are two key practices in modern software development , and Github Actions can facilitate both :
- Continious Integration (CI): CI is a practice where developers frequently merge their code changes into a shared repository. Each merge triggers an automated build and testing process to ensure changes do not break the existing functionality. With Github Actions , developers can set up workflows to automatically build and test their code every time they push changes to the repository or create a pull request.
- Continious Deployment (CD): CD extends the concept of CI by automating the deployment of code to production environments after it passes all the required tests. Github Actions can be configured to automatically deploy applications to various environments , such as staging or production , once the code passes CI checks. This practice reduces the time between development and deployement , allowing faster delivery of features and updates.

## Example
- Let's say we have a data science project , where we have three stories 1. Story A and 2. Story B 3. Story C .
- Let's suppose this is my main branch. Story A assigned to dev A , now if he wants to work on Story A , so now in agile methodology they create a branch(new branch , replica of this main branch) from this main branch , this sub-branch we will name as Story A branch , as we don't want to disturb the main branch. After developing the entire branch(new) what they do is that they will also write test cases , to verify whether the story is working or not. After writing the test cases we will do build on our local to see that everything is working fine. To test previous usecases in brain branch we have test cases.
- Once we verify everything is working fine we will merge this in the main branch. After merging is done our story will get merged in the main branch.
- B4 merging we have certain important things that we follow in this workflow.
- Main branch has its previous functionalities the merge should not break those functionalities.
- For this we have to 1. run all the test cases and then 2. build our entire project to make ensure its working fine.(Checks we need to do b4 we merge to our main branch).
- If we don't do checks the story/module that we have developed if there is some problem in that such as a code written which will break all the previous functionalities then it will be really bad.
- Workflow : The above 2 can be a part of the workflow, and this will only be done when we merge our story A branch to the main branch.
- Similarily we do for story B and C and then merge it after testing.
- When the merge is specifically happing and there is a common file that both dev A and B have changed ---> a conflict will happen. ---> Resolve it i.e. codes of both the developers needs to be mrged b4 commiting it to the main branch.

## Workflow that we start here
- We need to :
- Execute all the Test cases.
- Review the code with the best practices.
- Another workflow where i will be building the projects.


- Why are we doing this : So that entire process of this continious integration (the above 3 mentioned).
- Workflow basically means : Whenever we are commiting something we basically want to make sure that we run some automated build and testing process, to ensure that the changes do not break the existing functionality.

## Continious Deployment
- We created a github repository now our code is in the github repo(this is our main branch, basically developers from the local commit in the github repository after resolving the conflicts)-------> in companies they create different different environments : Dev environment , QA environment,(these environments can be different different server , instances),UAT environment , Production environment.
- Once developers commit all the code the data science project is ready ---> we need to deploy this project somewhere , but we can't directly deploy it into production there should be a certain number of steps that need to be followed , Boz we thoroughly need to test this data science project.
- We need to give our data science project to QA for testing : b4 we do the testing , we probably deploy this to our dev environment(it can be our server,AWS EC2 instance,Azure instance) , here we will be using something as dockers(bcoz dockers usually helps u to create images and do the deployment in such a way that u don't have to worry abt issues that arise due to different server configuration).When we do the deployment in the dev the development team starts testing it .
- Once the development team has tested , then from the same github repo we can again create a seperate continious deployment mechanism where we deploy the code directly to our QA environment. Then the QA team will do the testing. After they find out all the bugs they solve all those thing and then commit everything to the github ---> again they try to deploy it to the QA. Once QA team verifies all the bugs , then we go to the next environment i.e. UAT --> its a pre-prod environment (here the QA we again do the testing) and finally when everything works fine they take the UAT environment and directly deploy it in the production environment and this is ur live website or live application which is running in the cloud(with some domian name).


- The above is a workflow we follow in CD(Continious Deployment).

## Developers Workflow
- A developer's workflow refers to the series of steps , practices , and tools that a developer or a team of developers follows to write , test , collaborate on , and deploy code effectively. This workflow is designed to streamline the software development process , enhance productivity , reduce errors , and ensure high-quality code output. A well defined developer's workflow incorporates various stages of development , from coding to deployment , and often integrates tools for version control , code review , testing , and continious integration/continious deployment (CI/CD).

## Key Stages
- 1. Coding : Here a developer uses an integrated development environment(IDE) -- Eg. VS Code/Or any text editor. We can write in any programming languages. During this stage a developer follows some coding standards , best practices.
- 2. Version Control : Like Git --> This will manage the entire codebase. This git tool specifically , it helps u to collaborate (allows multiple developers to collaborate). Bcoz of this collaboration u will be able to quickly , efficiently complete the projects itself.
Collaborating : Scenarios like u have overwritten some other developers code. So its necessary to use the version control system.
- Here main thing that u should know is probably how to commit , how to create branches , how to push the branch , how to pull the branch , how to resolve the conflict(that happens in ur code).
- 3. Code Review : Whenever there is a main branch , whenever a developer creates a new story (this will basically be the new branch itself) and in this particular branch developer A starts working on that particular story and then later on this branch is basically merged(to the main branch) , before this branch is merged it's a good practice that we do some kind of code review. We do code reviews like : Peer Code review , Architect code review (different code reviews happen in a specific team) , the main reason is basically to follow the best standard practices for this particular code review. We will take the feedback on ur code , solve the issues and by this we will be able to improve our code quality.
- 4. Testing : Here we are talking about automated testing. How this(Automated Testing) happens specifically in developer workflow ?? There are multiple ways :
- First : Unit Testing. Where we write unit test cases.
- Second : Integration Testing(it is basically done so that the previous stories/modules that are developed should not break).
- Third : Design end to end test cases (just to find whether everything is working fine or not).
- Since this automated testing is a part of the entire workflow (the above ways should also get automatically triggered , whenever we try to merge the code to the main branch itsef).
- 5. Continious Integration (CI) : Bcoz in a project we have multiple developers , so in every commit of a code we should be reviewing it , building the project , testing the use cases(automated testing). And the developer should also be notified to fix the issues b4 merging .
- 6. Continious Deployment (CD) : After the merge is done successfully we deploy it in different different environments/server let's say QA server , dev server ,  UAT , prod --> are the servers we use.

## Developer Workflow with Real World Example
- Let's say u are developer A working in a team for some data science project , let's say u are in sprint 3 and u got some request of feature development.
- Now as a developer u pick a task , it can be a bug , a new change request or multiple things. Once u pick up a task , u have ur main branch , u try to create a new branch for this particular story(the particular feature) are we start developing.
- Additional branch that u have created u will start writing ur code in the local environment by using some IDE.
- Next step : Push anD Pull request ----> usually done in github repo.
- Once the development is done(in local environment) what developer will do that from the local it will try to push into the remote repository(the new created one).
- Then we raise a pull request to probably commit in the main repository. Initially we created the branches now we are raising a pull request to merge the changes in the main branch. B4 doing this other team members will get that request and they will be reviewing the pull request for code quality , style and any other issues.
- This way they are following some particular workflow before commiting/merging to the main branch.
- By now we are still in the Continious Integration (CI) phase.
- Then next step : Automated CI pipeline. What it does ??
- Once a pull request is opended a CI(Continious Integration) pipeline is automatically triggered . What this will do ?? This pipeline builds the application and runs all test cases. This test cases can be Unit test cases , Integration test cases , etc . 
- If this pipeline passes , the PR(Pull Request) is approved and the code will be merged into the main branch.
- Next step : Continious Deployment
- In CD upon merging the PR(Post request --> basically a event )(Event can be a post/ pull request , whenever a event occurs a workflow gets triggered based on that particular event--> CI/CD workflow) a CD pipeline is triggered. This workflow follows some steps/process. In this workflow a pipeline is basically triggered , upon merging the PR once the merge basically happens a CD pipeline is triggered and this automatically deploys the application to any dev/staging environment for testing.
- Once the testing is done then later on it can be deployed in the production environment.

## Note:
- If Github Actions is not there , we really need to do all this activities manually which is really bad , bcoz we really need to focus on the coding part --> all this checks can be automated with the help of github actions.

## Benefits of Developer's Workflow
- 1. Improved Collaboration : Clear workflow and processes facilitate better collaboration among team members , making it easier to understand who is responsible for what.
- 2. Higher Code Quality : Code reviews , automated tests , and CI/CD practices help maintain a high standard of code quality.
- 3. Reduced Erros : Automated testing and deployment reduce the likelihood of human error , ensuring more reliable releases.
- 4. Faster Delivery : Streamlined workflows enable faster development and release cycles , allowing teams to deliver new features and fixes more quickly.
- 5. Continious Feedback Loop : Regular monitoring and feedback helps teams quickly identify and address issues , continiously improving the product.

## Github Action Workflow
## Project - Automate Testing for a Python Project

## Steps :
1. Create a new repo on github named : GITHUB-CI_CD
## Commands:
- echo "# GITHUB-CI_CD" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Amritanshu160/GITHUB-CI_CD.git
- git push -u origin main

- Use git init and add the readme file also through the command , in readme add some information.

- After creating the readme file(manually) use the command : git add . ----> it is going to add all the files that is available(in ur current directory).
- After this ur files will be in added mode.
- Then we commit it : git commit -m "first commit"
- Add the branch : git branch -M main
- Then add the origin : git remote add origin https://github.com/Amritanshu160/GITHUB-CI_CD.git
- Then push the data from origin to main : git push -u origin main.

- Note:
- Once u add the origin u don't have to add it again , also ur commited files will be visible in ur github only after u complete all of these above mentioned steps.


## Note :
- In requirements.txt we have a library named pytest which is required for unit testing.
- Will write python code in src folder and will create test cases in test folder.
- I have to use specifically test folder bcoz what pytest does is that : It looks inside the entire code repository where test folder is there and from that it will probably pickup all the .py files w.r.t the unit test cases that u have specifically written.
- In src folder we will create __init__.py file so that we can import them wherever i want.

## After u add the test cases :
- git add .  ----> Will get all the files in the current directory.
- git commit -m "Unit test case updated"
- git push origin main

## Github Actions
- When u go to ur specific repo in github u have the options of actions on the top.
- There u will have a lot of actions.
- In actions in Python Application --> click Configure
- It will automatically create folders : GITHUB-CI_CD/.github/workflows/python-app.yml
- Whatever github actions or configurations we setup we setup in a yml file and we need to understand what exactly is this yml file.
- In ur current directory u have to create folders just like how they are created above : GITHUB-CI_CD/.github/workflows/python-app.yml
- yml file u can choose any name of ur choice , instead of python-app.yml we have chosen unittest.yml file.
- We will be writing the code in unittest.yml file. ---> for the workflow.
- Complete writing ur code , copy it , and then paste it in python-app.yml file (remove its content and paste the code u have written).
- We are pasting the code in unittest.yml here : GITHUB-CI_CD/.github/workflows/python-app.yml --> in the python-app.yml file.
- The name can be anything instead of python-app.yml we can keep any name.
- Commit the changes in ur github as soon as u do that --> ur entire workflow should get triggered. When u are commiting the changes basically a push/pull request is happening.
- When u commit choose the option : Commit directly to the main branch(a push request is basically going).

- Now when u will go to ur repo main page , u will see a id there in ur repo(basically workflow is triggered) , click it .
- Go to the actions some brown symbol is coming up with python-app.yml file name there , if green is their workflow has ran.
- If u click Create python-app.yml , u will see their that test has been executed.
- By clicking on test u will be able to see the entire workflow procedure like how it has been executed.
- test named box is there after u click Create python-app.yml file , this is bcoz we have setted the job name as 'test' in our unittest.yml file.
- And this is running on : ubuntu-latest.
- Ur job name is test which u have setted in unittest.yml file , u can check various stages of workflow after clicking on test , u can explore each stage from there.

## Note:
- Whatever commits i make now , let's say i make a commit in the Readme file , or any code file , it will just automatically trigger that particular action /workflow, even normally if u go to the actions section in ur repo , it is automatically triggering it , and then again it is going to check all the unit test cases.
- This is important as in a project multiple developers will be working , so suppose if a developer creates a new story and has commited the code it needs to probably run all the unit test cases , so that we can understand that nothing is getting broken.
