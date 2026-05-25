# FastAPI Review API

```mermaid
stateDiagram-v2
    [*] --> Pending: POST /submit
    Pending --> Approved: POST /approve
    Pending --> Rejected: POST /reject
    Approved --> [*]
    Rejected --> [*]
    Pending --> Pending: invalid retry 409
    Approved --> Approved: double approve 409
```
