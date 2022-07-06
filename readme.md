# Models

- Users
    - id: INT (auto increment, unique)
    - firstName: Char (max_length=100)
    - lastName: Char (max_length=100)
    - email: Char (max_length=100, unique)
    - password: Char (max_length=100)
    - admin Bool: ()
    - created_at: DateTime (default=django.utils.timezone.now)


- Promo
    - id: INT (auto increment, unique)
    - name: Char (max_length=100, unique)
    - admin_id: ForeignKeys(Users.ID)
    - created_at: DateTime (default=django.utils.timezone.now)


- Recipe
    - id: INT (auto increment, unique)
    - title: Char (max_length=100, unique)
    - admin_id: ForeignKeys(Users.ID)
    - created_at: DateTime (default=django.utils.timezone.now)
    - preview_at: DateTime (default=django.utils.timezone.now)


- Attendees
    - id: INT (auto increment, unique)
    - user_id: ForeignKeys(Users.ID)
    - arrival_time: DateTime (default=django.utils.timezone.now)
    - departure_time: DateTime (default=django.utils.timezone.now)


- UsersInPromo
    - id: INT (auto increment, unique)
    - user_id: ForeignKeys(Users.ID)
    - promo_id: ForeignKeys(Promo.ID)

# Functionality

[x] Create Models  
[x] Create Route  
[x] Display View  
[?] Avoid duplicate name in DB  
[] Request, POST, PATCH, DELETE  
[] User registration/login   
[] User can create a recipe(ONE PER DAY !)  
[] Create mechanism check system for USER (Press button for arrival and departure time)  
[] User can view only own attendances informations  
[] Chef can view all attendances informations  
[] People not connected cannot see any informations  
[] Redirection

## Bonus

[] Create 404 Page  
[] User can edit their own profile and delete their own recipe  
[] Chef can edit all profile and all recipe  
[] Create a promo system so that learners and chef can be splitted into different subgroups.


    



