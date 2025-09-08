Description:

This database is designed to organize and analyze crime-related data for innvestigative and reporting purpose.
The goal is to provide a structured way to track case progress, monitor crime activities and to identify patterns within the city. 

Entity: Crime Incident

  Attributes
  
          Date
          Location
          Type of Crime

  Instances
  
          March 27, 2024
          1229 Reserve Avenue, Silver City, 25050
          Homocide

          November 5, 2024
          Citizen Park, Silver City, 25050
          Assault

Entity: Suspect

  Attributes
  
          First Name
          Last Name
          Age

  Instances
  
          John
          Roger
          41

          Isabella
          Smith
          29

Entity: Case File

  Attributes
  
          Case Number 
          Status 
          Officer Assigned

  Instances
  
          25681550541255
          Closed
          Officer Alex

          75652255265242
          Under-Investigation
          Officer Paige

Entity: Officer

  Attributes
  
          Badge Number
          Name
          Rank
          
  Instances
  
          CF-021
          Alex Johnson
          Dectective

          CF-035
          Paige Williams
          Sergeant


-------------------------------------------------------

Questions/Use Cases

1. Which officer is assigned to each cases?
2. What type of crimes is most frequently reporded in each district of the city?
3. What is the ratio of male to female suspect?



