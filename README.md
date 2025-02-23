## Student Management

This is Custom Module for Student Enrollment Management build using frappe.

#### License

mit


## Getting Started

### Local Setup

1. [Install Bench Prerequisites](https://docs.frappe.io/framework/user/en/installation).

2. Initialize Bench:
    ```sh
    bench init <folder-name> --frappe-branch version-15 --python python3.11 
    ```
    Replace folder-name with your folder name

3. Move to Bench directory:
    ```sh
    cd <folder-name>
    ```

4. Clone ERPNext:
    ```sh
    bench get-app erpnext --branch version-15
    ```

5. Clone Student Management:
    ```sh
    bench get-app https://github.com/bibinprofessional/Student-Management.git --branch develop
    ```

6. Create New Site:
    ```sh
    bench new-site <site-name>
    ```
    Replace site-name with your site name

7. Add Site to Hosts
    ```sh
    bench --site <site-name> add-to-hosts
    ```

8. Install ERPNext to site
    ```sh
    bench --site <site-name> install-app erpnext
    ```

7. Install Student Management to site
    ```sh
    bench --site <site-name> install-app student_management
    ```

8. Enable Scheduler
    ```sh
    bench --site <site-name> enable-scheduler
    ```

9. Start Bench
    ```sh
    bench start
    ```
    You can open your site at (http://site-name:port-no/)


## Key Things to follow

-   **Create User:** Create a User With Valid email id and assign System Manager role and set password. Now login with that credentials. This is because email notifications will be sent only to valid email id.
    
-   **Add Email Account:** Add a Email Account and make it as default outgoing. Open Notification list(Student Enrollment Aproved) add this email as sender
-   **Add Courses:** As part of setup only 2 courses are added. You can add more courses in Courses Doctype


## Key Things to know

-   **Student Management Workspace:** Created a workspace called Student Management which can be seen in SideBar. This workspace has shortcuts to doctype, dashboards and reports. Clicking on report will take to report page where you can click on show report to see the specific report.

-   **Added as Fixtures:** Needed worflows, notification, dashboard are added as fixtures. So you can continue without creating new.

-   **Test cases:** Unit Test cases are written to test validation logics. You can run these tests using the following command.
        ```
        bench --site <site-name> run-tests --doctype "Student Enrollment"
        ```
        Replace site-name with your site name

-   **Rest Api Integration:** Two apis are written with authentication. Only authorized user can access these apis. Authorization should be passed in header (token api_key:api_secret).

    -   **create_student_enrollment:** This is a get api with 4 mandatory params (student_name, enrollment_date, course, email). This returns the name of the created student enrollment record. This Api can be accessed at 
    ```
    http://site-name:port-no/api/method/student_management.api.create_student_enrollment
    ```
    -   **get_student_enrollments:** This is a get api with 2 optional params(status,course). This returns the list of records based on filter. If no params are given it returns all created records. This Api can be accessed at 
    ```
    http://site-name:port-no/api/method/student_management.api.get_student_enrollments
    ```