# 0x01-shell_permissions

### 0-iam_betty
switches the current user to the user betty

### 1-who_am_i
prints the effective username of the current user

### 2-groups
prints all the groups the current user is part of

### 3-new_owner
changes the owner of the file hello to the user betty

### 4-empty
creates an empty file called hello

### 5-execute
adds execute permission to the owner of the file hello

### 6-multiple_permissions
adds execute permission to the owner and group owner and
read permission to other users to the file hello

### 7-everybody
adds execute permission to the owner, group owner and other
users to the file hello

### 8-James_Bond
adds, to the file hello, no permission to the owner, no
permission to the group owner and all permissions to other
users

### 9-John_Doe
sets the mode of the file hello as follows
```-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```

### 10-mirror_permissions
sets the mode of the file hello to the same as that of olleh

### 11-directories_permissions
adds execute permission to all subdirectories of the current
directory to the owner, group owner and all the other users.

### 12-directory_permissions
creates a directory called my_dir with permissions 751 in the
working directory

### 13-change_group
changes the group owner of the file hello to school
