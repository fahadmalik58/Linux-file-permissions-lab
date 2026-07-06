# Linux File Permissions Lab

A hands-on cybersecurity and Linux administration project that demonstrates how Linux file permissions work, how to secure files and directories, and how improper permissions can create security risks.

This project is intended for educational purposes and can be performed on Ubuntu, Kali Linux, Debian, or any Linux distribution.

---

# Project Overview

Linux uses a permission-based security model that controls access to files and directories.

This lab teaches students how Linux permissions work by creating users, groups, files, and directories while applying different permission settings using standard Linux commands.

The lab also demonstrates common permission-related security issues and how to fix them.

---

# Objectives

After completing this lab, students will be able to:

- Understand Linux permission model
- Read symbolic permissions
- Read numeric permissions
- Use chmod
- Use chown
- Use chgrp
- Create users
- Create groups
- Change file ownership
- Secure sensitive files
- Configure shared directories
- Apply least privilege principle

---

# Learning Outcomes

Students will learn:

- Linux security fundamentals
- File ownership
- User permissions
- Group permissions
- Others permissions
- Special permissions
- SUID
- SGID
- Sticky Bit
- Secure file sharing
- Basic Linux administration

---

# Technologies Used

- Ubuntu Linux
- Kali Linux (Optional)
- Bash Shell
- Linux Terminal
- chmod
- chown
- chgrp
- ls
- mkdir
- touch
- nano

---

# Project Structure

```
linux-file-permissions-lab/
│
├── README.md
├── screenshots/
│   ├── permissions.png
│   ├── chmod.png
│   ├── ownership.png
│   └── sticky-bit.png
│
├── scripts/
│   ├── setup_lab.sh
│   ├── create_users.sh
│   ├── permission_examples.sh
│   └── cleanup.sh
│
├── exercises/
│   ├── exercise1.md
│   ├── exercise2.md
│   ├── exercise3.md
│   └── solutions.md
│
└── notes/
    ├── chmod.md
    ├── chown.md
    ├── permissions.md
    └── security_tips.md
```

---

# Prerequisites

Before starting, ensure you have:

- Ubuntu or Kali Linux
- Terminal access
- sudo privileges
- Basic Linux command knowledge

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/linux-file-permissions-lab.git
```

Navigate into the project:

```bash
cd linux-file-permissions-lab
```

Give execution permission to scripts:

```bash
chmod +x scripts/*.sh
```

Run the setup script:

```bash
./scripts/setup_lab.sh
```

---

# Lab Exercises

## Exercise 1 — Understanding Permissions

Create a file:

```bash
touch file.txt
```

View permissions:

```bash
ls -l
```

Example output:

```text
-rw-r--r-- 1 user user 0 file.txt
```

Breakdown:

```
Owner : rw-
Group : r--
Others: r--
```

---

## Exercise 2 — Changing Permissions

Make file executable:

```bash
chmod +x file.txt
```

Numeric mode:

```bash
chmod 755 file.txt
```

Verify:

```bash
ls -l
```

---

## Exercise 3 — Changing Ownership

Create new user:

```bash
sudo adduser student
```

Change owner:

```bash
sudo chown student file.txt
```

Verify:

```bash
ls -l
```

---

## Exercise 4 — Changing Group

Create group:

```bash
sudo groupadd developers
```

Assign group:

```bash
sudo chgrp developers file.txt
```

---

## Exercise 5 — Directory Permissions

Create directory:

```bash
mkdir project
```

Change permissions:

```bash
chmod 755 project
```

---

## Exercise 6 — Shared Directory

```bash
mkdir shared

chmod 775 shared
```

---

## Exercise 7 — Sticky Bit

```bash
chmod +t shared
```

Verify:

```bash
ls -ld shared
```

Example:

```text
drwxrwxrwt
```

---

## Exercise 8 — SUID

```bash
chmod u+s program
```

Verify:

```bash
ls -l
```

Example:

```text
-rwsr-xr-x
```

---

## Exercise 9 — SGID

```bash
chmod g+s project
```

---

## Exercise 10 — Remove Permissions

```bash
chmod 000 secret.txt
```

Only root can access the file.

---

# Permission Commands

| Command | Description |
|----------|-------------|
| ls -l | View permissions |
| chmod | Change permissions |
| chown | Change owner |
| chgrp | Change group |
| umask | Default permissions |
| stat | View file information |

---

# Numeric Permission Table

| Number | Permission |
|---------|------------|
| 0 | --- |
| 1 | --x |
| 2 | -w- |
| 3 | -wx |
| 4 | r-- |
| 5 | r-x |
| 6 | rw- |
| 7 | rwx |

---

# Common Permission Examples

| Command | Meaning |
|----------|----------|
| chmod 777 file | Everyone has full access |
| chmod 755 file | Owner full access |
| chmod 644 file | Standard file permission |
| chmod 600 file | Private file |
| chmod 700 directory | Private directory |

---

# Security Best Practices

- Never use 777 unless absolutely necessary.
- Follow the Principle of Least Privilege.
- Limit write permissions.
- Secure sensitive files with 600.
- Restrict private directories using 700.
- Regularly audit file permissions.
- Avoid unnecessary SUID/SGID binaries.
- Use groups instead of giving permissions to everyone.

---

# Screenshots

Include screenshots of:

- File permissions
- chmod examples
- chown command
- Sticky bit
- SGID
- SUID
- Shared directory
- User creation

Store them in:

```
screenshots/
```

---

# Troubleshooting

### Permission denied

```bash
chmod +x filename
```

---

### Operation not permitted

Run command with sudo:

```bash
sudo command
```

---

### User does not exist

Create user:

```bash
sudo adduser username
```

---

### Group does not exist

```bash
sudo groupadd developers
```

---

# Future Improvements

- ACL (Access Control Lists)
- SELinux demonstration
- AppArmor configuration
- Permission auditing script
- Interactive Bash menu
- Python permission checker
- Automated permission reports

---

# Author

**Fadi Malik**

Cybersecurity Student

Linux Administrator

---

# License

This project is licensed under the MIT License.

---

## Educational Purpose

This project is developed solely for educational and laboratory purposes to help students understand Linux file permissions and secure system administration practices. It does not include offensive or malicious functionality.
