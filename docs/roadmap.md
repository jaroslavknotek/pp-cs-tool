Roadmap
---

This document contains some stuff

## Goals

- Structure my notes
- Model relation between them
- Password protected
- Local and cloud backup
- Easy reading and writing
- Stored in MD format 
  -Allows editing file without the application
 
### Use cases - How should first prototype work

Initial upload
1. Notes are stored in markdown (MD).
2. Mds are archived with password
3. Uploaded to OneDrive(OD)
4. Local backup
5. \[Delete local copy\]
 
Edit
1. Notes is downloaded from OD.
2. Extract MDs with password
3. Import MD to XMind
4. Edit
5. Export XMind to MD
6. Archive with password
7. Upload to OD
8. Local backup
9. \[Delete local copy\]

Analysis
- Positive
  - Can be edited with notepad
  - Simple implementation
  - Support offline mode
    - If local copy is not deleted
- Negative
  - Need of XMind
  - Does not support multi relations (Graph)
  - User has to do too many step
    - Not suitable for collaborative workflow
    
### Possible Improvements

- Store data in graph database
  - Relation between records
    - Annotation
  - How fine grained would that be
  - Technology 
    - Neo4j
    - SPARQL
  - Won't be editable with notepad


## TODOS

- Read all files from `notes` not only the on in the root
  - I should change the path to the `archived`
  - Save path to `.md` journals in xmind?
  - Implement support for english vocab
  - Impelemen reminder
    - of some notes 
  - Create a persistent layer(graph database) and use xmind only as a GUI
    - https://github.com/xmindltd/xmind-sdk-python/blob/master/README.md
  - Add https://github.com/neo4j-examples/movies-python-py2neo-2.0/blob/master/example.py
  
### DONE
- I should ask for the password using console
- Add logging