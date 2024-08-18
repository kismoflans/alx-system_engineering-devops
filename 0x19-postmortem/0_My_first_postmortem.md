Postmortem Report: Outage of Web Service CRM

Issue Summary:

Duration: The outage occurred from 14:00 to 15:30 (UTC) on August 17, 2024.
Impact: The CRM web service was completely down during this period, affecting approximately 70% of users. Users experienced timeout errors when trying to access the service, which led to a significant disruption in their activities.
Root Cause: The root cause was identified as a failure in the database connection pool management. The connection pool reached its maximum capacity, leading to excessive connection timeouts and service unavailability.
Timeline:

14:00 - Issue detected by automated monitoring alert indicating high response times and increased error rates.
14:05 - The issue was initially investigated by the on-call engineer, who reviewed the application logs and observed a surge in connection errors.
14:20 - The team started investigating the database server, suspecting it might be a resource issue.
14:40 - It was discovered that the connection pool was exhausted, but the team initially overlooked the database configuration and focused on potential application code issues.
15:00 - After further investigation, the team realized that the database connection pool settings were insufficient for the traffic volume. The issue was escalated to the database administration team.
15:20 - The database team adjusted the connection pool settings and restarted the database service, which resolved the issue.
15:30 - Service was fully restored, and normal operation resumed.
Root Cause and Resolution:

Cause: The underlying issue was a misconfigured connection pool in the database. The connection pool size was set too low to handle the peak load, causing the system to exhaust available connections and resulting in timeout errors.
Resolution: The connection pool configuration was increased to accommodate the peak traffic volumes. The database server was restarted to apply the new settings. Additionally, performance monitoring was enhanced to better handle traffic spikes.
Corrective and Preventative Measures:

Improvements Needed:
Review and adjust connection pool settings based on traffic patterns and peak usage.
Implement more robust monitoring and alerting for database performance issues.
Tasks to Address the Issue:
Task 1: Review and update the database connection pool configuration. (Assigned to Database Admin Team, Deadline: August 20, 2024)
Task 2: Enhance database performance monitoring to include connection pool metrics and alerts for high usage. (Assigned to DevOps Team, Deadline: August 22, 2024)
Task 3: Conduct a load testing exercise to simulate peak traffic and ensure the system can handle it. (Assigned to QA Team, Deadline: August 25, 2024)
Conclusion:
This outage highlighted the need for proper configuration and monitoring of critical system components. By addressing the root cause and implementing the corrective measures, we aim to prevent similar issues in the future and ensure higher system reliability.
