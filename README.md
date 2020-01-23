# xml-database-generator

*pet_club.py* will generate an xml file that simulates a database for members of a Pet Club. This xml file may then be used to aid in learning to use BaseX or the python module BaseXClient.

The program defaults to generating a Pet Club with 4 x members. A command line argument allows the setting of the number of members. 

Each Pet Club member receives a unique integer ID. The ID's start at 1, but are randomly assigned.

If the python module corporate_ipsum is downloaded from https://github.com/ldo/corporate_ipsum then this will be used to generate a random quotation for each member.

It is possible that two members may have the same first name, middle initial and surname, but *highly unlikely* that they will also share the same date of birth.

The xml file generated for a two member Pet Club will be like the following but with completely different data:

```
$ python3 pet_club.py 2
Created:
<!-- File Name:pet_club_2.xml            Size:751        Members:2          Duration:0.003      -->

$ cat pet_club_2.xml
<?xml version="1.0" encoding="UTF-8"?>
<pet_club>
  <member>
    <member_id>2</member_id>
    <surname>Olson</surname>
    <first>Robert</first>
    <initial>S.</initial>
    <gender>male</gender>
    <dob>2004-07-25</dob>
    <pet>cat</pet>
    <colour>white</colour>
    <quote>Compellingly formulate unique platforms.</quote>
  </member>
  <member>
    <member_id>1</member_id>
    <surname>Houston</surname>
    <first>Judy</first>
    <initial>P.</initial>
    <gender>female</gender>
    <dob>1981-01-21</dob>
    <pet>cat</pet>
    <colour>white</colour>
    <quote>Professionally disseminate real-time storage.</quote>
  </member>
</pet_club>
<!-- File Name:pet_club_2.xml            Size:751        Members:2          Duration:0.003      -->
```

## Notes on a generating the xml file on a laptop with SSD: 
* 100,000 members in the Pet Club took less than 10 seconds and created a 30MB file.
* 1,000,000 members in the Pet club took 1 min 30 seconds and created a 300MB file. 
