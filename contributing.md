## For Developers
The first thing you are going to need to do is get the package, install the dependencies, and then setup
a virtual environment to be able to test the build.

### Git Package
Move to an appropriate location on your computer (I recommend using a directory as a workspace for your
development projects e.g., ~/workspace/) and run:
```bash
git clone git@github.com:berkeleyapplied/baa_messages.git
```
###Install Dependencies
Now we will need to go into that directory (herein referred to as [repo_location]) and run the setup
baa_messages:
```bash
cd [repo_location]
./bin/setup.sh
```
Note, this setup script is currently setup for Mac computers.  if you are running on a different OS, please
see the setup.sh script and install the appropriate packages

### Setting up a Virtual Environment for Build Testing
Its best to use a virtual environment to contribute to the development of this library.  If you are unfamiliar
with virtual environments, see [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Before you commit your code, setup a blank virtual environment and install the package to
make sure that nothing you have done has broken the install:
```bash
virtualenv my_venv
source my_venv/bin/activate
sudo pip install -r requirements.txt
sudo pip install .
./bin/run_tests.sh
```
If this works then the build works in a clean environment and you can move on to committing your changes.


To exit the virtual environment, inside the venv type:
```bash
deactivate
```
Once you are done making changes, and you have deactivated the venv session, you can simply remove the
my_venv directory to blow away that virtual environment.  (Please be sure not to check in
that directory as it will be different for different development environments)

## Testing the Installation
If you would like to run the unit tests, separate from the commit, you can do the following:
```bash
cd [repo_location]
python setup.py test
```
Note: When you commit your code git will run a few tests to ensure that everything meets the specs required to contribute,
if you find bugs in this process, please add a bug report [here](https://github.com/berkeleyapplied/baa_messages)

# GIT Flow
-------------------------------
A guide for Baa_messages's Git workflow. This workflow is based on a agile sprint model, where there will be (bi-)weekly releases to production with a number of features that have been completed & acceptance tested during the sprint.

Primary Branches
----------------

There are two primary branches in the repository:

- `master`
- `stage`

The `master` branch will always reflect what's on production. **No exceptions**.

All completed features will be submitted to the `stage` branch via pull requests.

Create a Feature or Bug Fix
---------------------------


Branch off: `dev`
Merge Into: `dev`
Naming: `<initials>-<branch name>`

For non-urgent features or bug fixes, branch off the `dev` branch and create a feature or bug fix branch:

    git checkout dev
    git pull
    git checkout -b <initials>-<branch name>

From within your feature branch, rebase regularly to incorporate the latest changes from `dev`:

    git fetch origin
    git rebase origin/dev

Resolve conflicts & create commits as you go along.

When your feature is ready for merging into `dev`, [use `git rebase` interactively] to squash all your commits into one.

Share your branch.

    git push origin <branch name>

[Create a pull request] from this branch and request a code review. **Make sure you create a PR that merges into the `dev` branch, not the `master` branch**.

_Your PR should merge INTO `development` FROM your feature branch._

When fixing a bug include **Fixes #45** where 45 is the issue number.

[Create a pull request]: https://help.github.com/articles/using-pull-requests/
[use `git rebase` interactively]: https://help.github.com/articles/about-git-rebase/
[Close a bug with a commit message]: https://help.github.com/articles/closing-issues-via-commit-messages/

Merging in a Feature
--------------------

Once you've fixed any issues in your PR, make sure to squash commits into one and force push your branch. To make sure you're not overwriting anyone else's code, use [`--force-with-lease`].

A PR must have at least one :+1: before merging. When you've gotten approval to merge, merge the feature branch into `dev`

    git checkout development
    git merge --no-ff <initials>-<branch name>
    git push origin development

Once this is done, delete your branch.

    git push origin --delete <initials>-<branch-name>
    git branch --delete <initials>-<branch-name>

[`--force-with-lease`]: https://developer.atlassian.com/blog/2015/04/force-with-lease/

Staging
_______
The staging branch is for previewing completed developments. It is used by tools that rely on a working version of baa_messages to
properly function. If there is a breaking change in baa_messages we will need to fix these issues in the reliant codebase and release
a version of each into stage for testing together.

  git checkout stage
  git merge --no-ff dev
  git push origin stage

End-of-Sprint Release
---------------------

The `stage` branch is now full of tested features that are ready for deployment. To release, create a pull request that will be merging the `stage` branch into the `master` branch.

_Your PR should merge INTO `master` FROM `stage`._

Set the title of the PR to be:

    YYYY-MM-DD Release

In the description of the PR, you can add details like:

- Features in the PR
- Sprint Cards
- Related error notifications

This can act as the weekly release report. Once the report is complete, you can hit the "Merge Pull Request" button. Once merged, the release will be auto-deployed to production.

Hotfixes: Urgent Production Issues
----------------------------------

Branch off: `master`
Merge Into: `master`, `stage` and `development`
Naming: `<initials>-hotfix-<branch name>`

For issues that cannot wait until the end of a sprint cycle, create hotfix branch from the `master` branch:

    git checkout master
    git pull
    git checkout -b <initials>-hotfix-<branch name>

Add your fix and rebase from `master` regularly to keep up to date. Once your fix is complete, squash your commits into one and submit another pull request. This time, make sure you are merging into the `master` branch.

Your PR should merge INTO `master` and `stage` FROM your hotfix branch.

Once you've gotten approval, merge your hotfix branch into the `master` branch.

    git checkout master
    git merge --no-ff <initials>-hotfix-<branch name>
    git push origin master

Merge your hotfix branch into stage as well.

    git checkout dev
    git merge --no-ff <initials>-hotfix-<branch name>
    git push origin stage

Merge your hotfix branch into development as well.

    git checkout dev
    git merge --no-ff <initials>-hotfix-<branch name>
    git push origin dev

Once this is done, delete your branch.

    git push origin --delete <initials>-hotfix-<branch-name>
    git branch --delete <initials>-hotfix-<branch-name>
