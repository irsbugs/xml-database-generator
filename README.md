# xml-database-generator

*pet_club.py* will generate an xml file that simulates a database for members of a Pet Club. This xml file may then be used to aid in learning BaseX.

The program defaults to generating a Pet Club with 4 x members. A command line argument allows the setting of the number of members. 

Each Pet Club member receives a unique integer ID. The ID's start at 1, but are randomly assigned.

If the python module corporate_ipsum is downloaded from https://github.com/ldo/corporate_ipsum then this will be used to generate a random quotation for each member.

The xml file generated for a two member Pet Club will be like the following but with completely different data:

  $ python3 pet_club.py 2
  Created:
  <!-- File Name:pet_club_2.xml            Size:766        Members:2          Duration:0.003      -->

  $ cat pet_club_2.xml
  <?xml version="1.0" encoding="UTF-8"?>
  <pet_club>
    <member>
      <member_id>2</member_id>
      <surname>Moore</surname>
      <first>Geneva</first>
      <initial>Z.</initial>
      <gender>female</gender>
      <dob>2010-07-06</dob>
      <pet>budgie</pet>
      <colour>green</colour>
      <quote>Proactively deliver leveraged information.</quote>
    </member>
    <member>
      <member_id>1</member_id>
      <surname>Stanley</surname>
      <first>Darin</first>
      <initial>Y.</initial>
      <gender>male</gender>
      <dob>1974-03-24</dob>
      <pet>dog</pet>
      <colour>grey</colour>
      <quote>Credibly incubate revolutionary methods of empowerment.</quote>
    </member>
  </pet_club>
  <!-- File Name:pet_club_2.xml            Size:766        Members:2          Duration:0.003      -->

