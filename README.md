# Merge-Monitor

A GitHub Action that blocks PRs if they modify any files listed in lockedFiles.txt.

# How to use:

When you add the github action to your repo, on the lockedFiles.txt add the name of the files that you don't want outsiders to change

If you want to allow a pull request to go through even if it modifies locked files, you can add a special label: BYPASS_LABEL
By adding the label you skip the check

# Demos:

### If there has been changes:
![closeTest](https://github.com/user-attachments/assets/d6c91727-e20c-428c-a20e-51cba4b0938a)

### No changes 
![ok](https://github.com/user-attachments/assets/193c153c-23dc-4e1a-a960-feb0769b3f74)

You can also use label only if you want to make changes to files that isn't allowed

### Using label
![withLabel](https://github.com/user-attachments/assets/562f8ff4-a6e5-4d3e-8cae-a7e0dde2d5df)
