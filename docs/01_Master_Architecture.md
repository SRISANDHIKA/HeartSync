# HeartSync Master Architecture

## System Overview

```text
                    USERS
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     Patients       Doctors       Administrators
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼

          FRONTEND (HTML + CSS + Bootstrap)
                       │
                       ▼

              DJANGO APPLICATION
                       │
 ┌──────────┬──────────┬──────────┬──────────┐
 │          │          │          │          │
 ▼          ▼          ▼          ▼          ▼

Auth     Patient     Doctor    Appointment    AI
Module    Module     Module      Module      Module

 │          │          │          │          │
 └──────────┴──────────┴──────────┴──────────┘
                       │
                       ▼

              PostgreSQL Database
                       │
                       ▼

                 Azure Cloud
```

### Undersatnding the flow

When a patient books an appointment

Patient
   │
   ▼
Browser
   │
   ▼
Django
   │
   ▼
PostgreSQL
   │
   ▼
Success Response
   │
   ▼
Patient Sees Confirmation