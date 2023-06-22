import logging
import json
import azurefunctions as func

data={
  "basics": {
    "name": "Abia Javed",
    "label": "AI student",
    "image": "",
    "email": "abia.javed27@gmail.com",
    "phone": "000-000-000",
    "url": "https://abiajaved.com",
    "summary": "A summary of Abia Javed…",
    "location": {
      "address": "Satellite town",
      "postalCode": "RWP 46000",
      "city": "Rawalpindi",
      "countryCode": "PAK",
      "region": "Punjab"
    },
    
    
    "profiles": [{
      "network": "Twitter",
      "username": "Abia",
      "url": "https://twitter.com/abia"
    }]
  },
  
  
  "work": [{
    "name": "Company",
    "position": "CEO",
    "url": "https://company.com",
    "startDate": "2023-01-01",
    "endDate": "2024-01-01",
    "summary": "Description…",
    "highlights": [
      "Started the company"
    ]
  }],
  
  
  "education": [{
    "institution": "FAST NUCES",
    "position": "Student",
    "url": "https://fastnuces.com/",
    "startDate": "2021-09-01",
    "endDate": "2025-12-01",
    "summary": "Description…",
    "Degree": [
      "Graduated as an AI Scientist"
    ]
  }],
 
  "awards": [{
    "title": "Award",
    "date": "2023-10-01",
    "awarder": "Company",
    "summary": "Women in tech"
  }],
  
  "certificates": [{
    "name": "Certificate",
    "date": "2022-06-07",
    "issuer": "Company",
    "url": "https://certificate.com"
  }],
  
  "publications": [{
    "name": "Publication",
    "publisher": "medium",
    "releaseDate": "2024-10-01",
    "url": "https://publication.com",
    "summary": "Description…"
  }],
  
  "skills": [{
    "name": "Cyber security",
    "level": "Master",
    "keywords": [
      "Information Security",
      "Information Technology",
      "Malware Anaysis"
    ]
  }],
  
  "languages": [{
    "language": "English",
    "fluency": "Native speaker"
  }],
  
  "interests": [{
    "name": "Writing",
    "keywords": [
      "Blogging",
      "Journalling"
    ]
  }],
  
  "references": [{
    "name": "Abia Javed",
    "reference": "Reference…"
  }],
  
  "projects": [{
    "name": "Project",
    "startDate": "2019-01-01",
    "endDate": "2021-01-01",
    "summary": "Summary...",
    "highlights": [
      "Volunteer in different events"
    ],
    "url": "https://project.com/"
  }]
}
