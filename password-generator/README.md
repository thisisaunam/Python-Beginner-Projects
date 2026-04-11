# password generator

a command-line based password generator built using python.  
this project evolves from a basic random generator (v1) to a customizable and validated system (v2).

---

## overview

this project focuses on building a flexible password generator that allows users to:

* customize character types  
* control password length  
* generate multiple passwords in one session  
* evaluate password strength  

it reflects progression from basic python concepts to structured program design.

---

## features

### version 1
* takes password length as input  
* generates random password using letters, numbers, and symbols  
* uses `random` module  

### version 2
* allows user to choose:
  1. uppercase letters  
  2. lowercase letters  
  3. digits  
  4. symbols  
* ensures at least one alphabet is selected  
* handles invalid input using exception handling (`try-except`)  
* supports multiple password generations in a loop  
* evaluates password strength based on composition  

---

## how to run

run the file using:

```bash
python password_generator_v2.py
```
---

## notes 

* v1 focuses on basic random generation
* v2 introduces validation, customization, and logic-based evaluation

future improvements may include:
* guaranteed inclusion of selected character types
* saving generated passwords to a file
* enhanced strength analysis
