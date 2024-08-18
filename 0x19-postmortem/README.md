# Postmortem: Apache 500 Error on WordPress Site

## Issue Summary

- **Duration:**  
  The outage lasted for 2 hours, from 10:00 AM to 12:00 PM UTC on August 18, 2024.

- **Impact:**  
  The entire WordPress site hosted on Apache was returning a 500 Internal Server Error. Approximately 100% of the users were unable to access the site, resulting in significant disruption.

- **Root Cause:**  
  A missing PHP module (`php-mysql`) was causing a fatal error when Apache attempted to load the WordPress site, leading to the 500 error.

## Timeline

- **10:00 AM:**  
  Issue detected via a monitoring alert that the site was returning 500 errors.

- **10:05 AM:**  
  The issue was confirmed by an engineer who attempted to access the site and received the same error.

- **10:10 AM:**  
  Initial investigation began, focusing on Apache configuration files and logs to identify any recent changes or misconfigurations.

- **10:25 AM:**  
  Misleading path: The investigation incorrectly assumed that the issue was related to file permissions, leading to a temporary focus on checking and modifying permissions for critical directories.

- **10:40 AM:**  
  The incident was escalated to the DevOps team for further investigation.

- **11:00 AM:**  
  The DevOps team attached `strace` to the Apache process to trace system calls and signals, revealing that the error occurred due to a missing PHP module.

- **11:15 AM:**  
  The missing `php-mysql` module was identified as the root cause.

- **11:30 AM:**  
  The module was installed, and Apache was restarted.

- **11:35 AM:**  
  The site was tested, and the 500 error was resolved.

- **12:00 PM:**  
  Monitoring confirmed that the site was fully operational, and the incident was officially closed.

## Root Cause and Resolution

- **Root Cause:**  
  The Apache server was configured to serve a WordPress site that relies on PHP to interact with a MySQL database. The `php-mysql` module, which is essential for this interaction, was missing. Without this module, PHP was unable to connect to the database, causing a fatal error and resulting in the 500 Internal Server Error.

- **Resolution:**  
  The issue was resolved by installing the missing `php-mysql` module using the package manager. Once installed, the Apache server was restarted to apply the changes, and the site resumed normal operation.

## Corrective and Preventative Measures

- **Improvements:**
  - **Monitoring Enhancements:** Implement additional monitoring to detect missing dependencies or modules on critical services.
  - **Documentation:** Update deployment documentation to include a checklist of required modules and extensions for PHP-based applications.
  - **Automation:** Automate the installation and verification of required PHP modules during deployment to prevent similar issues in the future.

- **Tasks:**
  - [ ] Patch Apache and PHP configuration files to ensure all necessary modules are included.
  - [ ] Implement a Puppet script to automate the installation of the `php-mysql` module.
  - [ ] Add a monitoring check for missing PHP modules that are critical to the operation of web services.
  - [ ] Conduct a review and update the runbook for handling similar outages, including instructions on using `strace` for debugging.
  - [ ] Schedule a training session for the team on using `strace` and other debugging tools effectively.

